import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from styles import apply_global_styles
from utils.data_loader import load_fmcg_data
from utils.i18n import t


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock - Dashboard & EDA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_global_styles()


def render_html(content: str) -> None:
    st.html(content)


# ============================================================
# DATA LOADING
# ============================================================

df = load_fmcg_data()

if df is None or df.empty:

    st.error(
        f"⚠️ {t('error')}: {t('no_data')}"
    )

    st.stop()


# ============================================================
# CLEAN DATA
# ============================================================

df.columns = df.columns.str.strip()

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce",
    )

df["Units_Sold"] = pd.to_numeric(
    df["Units_Sold"],
    errors="coerce",
)

df = df.dropna(
    subset=[
        "Date",
        "Product_Name",
        "Category",
        "Units_Sold",
    ]
).copy()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

with st.sidebar:

    st.markdown(
        f"### 🔍 {t('filters')}"
    )

    min_date = df["Date"].min().date()

    max_date = df["Date"].max().date()


    selected_date_range = st.date_input(
        t("date_range"),
        value=(
            min_date,
            max_date,
        ),
        min_value=min_date,
        max_value=max_date,
        key="eda_date_filter",
    )


    all_categories = (
        [t("all_categories")]
        +
        sorted(
            df["Category"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    selected_category = st.selectbox(
        t("category"),
        all_categories,
        index=0,
        key="eda_category_filter",
    )


    if selected_category != t("all_categories"):

        filtered_products = sorted(
            df[
                df["Category"]
                == selected_category
            ]["Product_Name"]
            .dropna()
            .unique()
            .tolist()
        )

    else:

        filtered_products = sorted(
            df["Product_Name"]
            .dropna()
            .unique()
            .tolist()
        )


    all_products = (
        [t("all_products")]
        +
        filtered_products
    )


    selected_product = st.selectbox(
        t("product"),
        all_products,
        index=0,
        key="eda_product_filter",
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if (
    isinstance(
        selected_date_range,
        tuple,
    )
    and
    len(selected_date_range) == 2
):

    start_date, end_date = (
        selected_date_range
    )

    filtered_df = filtered_df[
        (
            filtered_df["Date"].dt.date
            >= start_date
        )
        &
        (
            filtered_df["Date"].dt.date
            <= end_date
        )
    ]


if selected_category != t("all_categories"):

    filtered_df = filtered_df[
        filtered_df["Category"]
        == selected_category
    ]


if selected_product != t("all_products"):

    filtered_df = filtered_df[
        filtered_df["Product_Name"]
        == selected_product
    ]


if filtered_df.empty:

    st.warning(
        f"⚠️ {t('no_results')} "
        f"{t('information')}."
    )

    st.stop()


# ============================================================
# HEADER
# ============================================================

render_html(
    f"""
    <div class="hero">

        <h1>
            📊 {t("dashboard_title")} &
            {t("exploratory_analysis")}
        </h1>

        <p>
            {t("dashboard_description")}
        </p>

    </div>
    """
)


# ============================================================
# EXECUTIVE METRICS
# ============================================================

st.divider()


total_units_sold = float(
    filtered_df["Units_Sold"].sum()
)


daily_sales = (
    filtered_df
    .groupby("Date")["Units_Sold"]
    .sum()
)


avg_daily_sales = float(
    daily_sales.mean()
)


peak_sales_day = float(
    daily_sales.max()
)


unique_products = (
    filtered_df["Product_Name"]
    .nunique()
)


kpi1, kpi2, kpi3, kpi4 = (
    st.columns(4)
)


with kpi1:

    st.metric(
        t("total_units"),
        f"{total_units_sold:,.0f}",
    )


with kpi2:

    st.metric(
        t("average_daily"),
        f"{avg_daily_sales:,.1f}",
    )


with kpi3:

    st.metric(
        t("maximum_demand"),
        f"{peak_sales_day:,.0f}",
    )


with kpi4:

    st.metric(
        t("products"),
        f"{unique_products:,}",
    )


# ============================================================
# 1. TIME SERIES DEMAND & DISTRIBUTION
# ============================================================

st.divider()


render_html(
    f"""
    <div class="section-title">
        📈 1. {t("demand_trend")} &
        {t("sales_distribution")}
    </div>
    """
)


col_ts, col_dist = st.columns(
    [2, 1]
)


# ------------------------------------------------------------
# DAILY DEMAND TREND
# ------------------------------------------------------------

with col_ts:

    st.subheader(
        t("daily_demand")
    )


    daily_trend = (
        filtered_df
        .groupby(
            "Date",
            as_index=False,
        )["Units_Sold"]
        .sum()
        .sort_values("Date")
    )


    daily_trend["7D_MA"] = (
        daily_trend["Units_Sold"]
        .rolling(
            7,
            min_periods=1,
        )
        .mean()
    )


    fig_trend = go.Figure()


    fig_trend.add_trace(
        go.Scatter(
            x=daily_trend["Date"],
            y=daily_trend["Units_Sold"],
            mode="lines",
            name=t("daily_demand"),
            line=dict(
                color="#3B82F6",
                width=1,
            ),
            opacity=0.4,
        )
    )


    fig_trend.add_trace(
        go.Scatter(
            x=daily_trend["Date"],
            y=daily_trend["7D_MA"],
            mode="lines",
            name=t("average_daily"),
            line=dict(
                color="#10B981",
                width=2.5,
            ),
        )
    )


    fig_trend.update_layout(

        template="plotly_dark",

        paper_bgcolor="#070B18",

        plot_bgcolor="#070B18",

        font={
            "color": "#CBD5E1"
        },

        xaxis_title=t("start_date"),

        yaxis_title=t("total_units"),

        hovermode="x unified",

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20,
        ),
    )


    st.plotly_chart(
        fig_trend,
        use_container_width=True,
    )


# ------------------------------------------------------------
# DISTRIBUTION
# ------------------------------------------------------------

with col_dist:

    st.subheader(
        t("sales_distribution")
    )


    fig_hist = px.histogram(
        filtered_df,
        x="Units_Sold",
        nbins=30,
        marginal="box",
    )


    fig_hist.update_layout(

        template="plotly_dark",

        paper_bgcolor="#070B18",

        plot_bgcolor="#070B18",

        font={
            "color": "#CBD5E1"
        },

        xaxis_title=t("total_units"),

        yaxis_title=t("records"),

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20,
        ),
    )


    st.plotly_chart(
        fig_hist,
        use_container_width=True,
    )


# ============================================================
# 2. PRICING & PROMOTIONAL IMPACT
# ============================================================

st.divider()


render_html(
    f"""
    <div class="section-title">
        🏷️ 2. {t("discount")} &
        {t("promotion")} Impact
    </div>
    """
)


col_price, col_promo = st.columns(2)


# ------------------------------------------------------------
# PRICE VS DEMAND
# ------------------------------------------------------------

with col_price:

    st.subheader(
        f"{t('unit_price') if 'unit_price' in globals() else 'Unit Price'} "
        f"vs. {t('total_units')}"
    )


    if "Unit_Price_NGN" in filtered_df.columns:

        fig_price = px.scatter(
            filtered_df,
            x="Unit_Price_NGN",
            y="Units_Sold",
            color="Category",
            hover_data=[
                "Product_Name"
            ],
            opacity=0.7,
            trendline="ols",
        )


        fig_price.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title="Unit Price (₦)",

            yaxis_title=t("total_units"),

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10,
            ),
        )


        st.plotly_chart(
            fig_price,
            use_container_width=True,
        )


# ------------------------------------------------------------
# PROMOTION / DISCOUNT
# ------------------------------------------------------------

with col_promo:

    st.subheader(
        f"{t('discount_percentage')} & "
        f"{t('promotion')}"
    )


    if (
        "Discount_Percent"
        in filtered_df.columns
        and
        "Is_Promotion"
        in filtered_df.columns
    ):

        fig_promo = px.box(
            filtered_df,
            x="Is_Promotion",
            y="Units_Sold",
            color="Discount_Percent",
            points="outliers",
        )


        fig_promo.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title=t("promotion"),

            yaxis_title=t("total_units"),

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10,
            ),
        )


        st.plotly_chart(
            fig_promo,
            use_container_width=True,
        )


# ============================================================
# 3. CALENDAR & SEASONAL DRIVERS
# ============================================================

st.divider()


render_html(
    f"""
    <div class="section-title">
        📅 3. {t("payday")} &
        {t("seasonality")}
    </div>
    """
)


c1, c2, c3 = st.columns(3)


# ------------------------------------------------------------
# PAYDAY
# ------------------------------------------------------------

with c1:

    st.subheader(
        t("payday")
    )


    if "Is_Payday_Period" in filtered_df.columns:

        payday_summary = (
            filtered_df
            .groupby(
                "Is_Payday_Period",
                as_index=False,
            )["Units_Sold"]
            .mean()
        )


        payday_summary["Label"] = (
            payday_summary[
                "Is_Payday_Period"
            ]
            .map(
                {
                    0: t("normal_rainfall"),
                    1: t("payday"),
                }
            )
        )


        fig_payday = px.bar(
            payday_summary,
            x="Label",
            y="Units_Sold",
            color="Label",
        )


        fig_payday.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title="",

            yaxis_title=t(
                "average_demand"
            ),

            showlegend=False,

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10,
            ),
        )


        st.plotly_chart(
            fig_payday,
            use_container_width=True,
        )


# ------------------------------------------------------------
# DAY OF WEEK
# ------------------------------------------------------------

with c2:

    st.subheader(
        t("weekends")
    )


    if "Day_of_Week" in filtered_df.columns:

        days_order = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]


        dow_summary = (
            filtered_df
            .groupby(
                [
                    "Day_of_Week",
                    "Is_Weekend",
                ],
                as_index=False,
            )["Units_Sold"]
            .mean()
        )


        dow_summary[
            "Day_of_Week"
        ] = pd.Categorical(
            dow_summary[
                "Day_of_Week"
            ],
            categories=days_order,
            ordered=True,
        )


        dow_summary = (
            dow_summary
            .sort_values(
                "Day_of_Week"
            )
        )


        fig_dow = px.bar(
            dow_summary,
            x="Day_of_Week",
            y="Units_Sold",
            color="Is_Weekend",
        )


        fig_dow.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title=t(
                "weekends"
            ),

            yaxis_title=t(
                "average_demand"
            ),

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10,
            ),
        )


        st.plotly_chart(
            fig_dow,
            use_container_width=True,
        )


# ------------------------------------------------------------
# SEASON / HOLIDAY
# ------------------------------------------------------------

with c3:

    st.subheader(
        t("seasonality")
    )


    if (
        "Season" in filtered_df.columns
        and
        "Is_Holiday" in filtered_df.columns
    ):

        season_summary = (
            filtered_df
            .groupby(
                [
                    "Season",
                    "Is_Holiday",
                ],
                as_index=False,
            )["Units_Sold"]
            .mean()
        )


        fig_season = px.bar(
            season_summary,
            x="Season",
            y="Units_Sold",
            color="Is_Holiday",
            barmode="group",
        )


        fig_season.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title=t(
                "seasonality"
            ),

            yaxis_title=t(
                "average_demand"
            ),

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10,
            ),
        )


        st.plotly_chart(
            fig_season,
            use_container_width=True,
        )


# ============================================================
# 4. WEATHER & CORRELATIONS
# ============================================================

st.divider()


render_html(
    f"""
    <div class="section-title">
        🌧️ 4. {t("rainfall")} &
        {t("correlation_matrix")}
    </div>
    """
)


col_rain, col_corr = st.columns(2)


# ------------------------------------------------------------
# RAINFALL
# ------------------------------------------------------------

with col_rain:

    st.subheader(
        t("rainfall_severity")
    )


    if (
        "Rainfall_Severity"
        in filtered_df.columns
    ):

        rain_summary = (
            filtered_df
            .groupby(
                "Rainfall_Severity",
                as_index=False,
            )["Units_Sold"]
            .mean()
        )


        fig_rain = px.bar(
            rain_summary,
            x="Rainfall_Severity",
            y="Units_Sold",
            color="Units_Sold",
            color_continuous_scale="Tealgrn",
        )


        fig_rain.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            xaxis_title=t(
                "rainfall_severity"
            ),

            yaxis_title=t(
                "average_demand"
            ),

            coloraxis_showscale=False,

            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20,
            ),
        )


        st.plotly_chart(
            fig_rain,
            use_container_width=True,
        )


# ------------------------------------------------------------
# CORRELATION MATRIX
# ------------------------------------------------------------

with col_corr:

    st.subheader(
        t("correlation_matrix")
    )


    numeric_cols = (
        filtered_df
        .select_dtypes(
            include=["number"]
        )
        .columns
        .tolist()
    )


    if len(numeric_cols) > 1:

        corr_matrix = (
            filtered_df[
                numeric_cols
            ]
            .corr()
        )


        fig_corr = px.imshow(
            corr_matrix,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale="Viridis",
            labels={
                "color":
                    t("correlation_matrix")
            },
        )


        fig_corr.update_layout(

            template="plotly_dark",

            paper_bgcolor="#070B18",

            plot_bgcolor="#070B18",

            font={
                "color": "#CBD5E1"
            },

            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20,
            ),
        )


        st.plotly_chart(
            fig_corr,
            use_container_width=True,
        )