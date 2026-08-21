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
# DATA LOADING & EXACT COLUMN MAPPING
# ============================================================
df = load_fmcg_data()

if df is None or df.empty:
    st.error("⚠️ Failed to load dataset. Please check your data directory.")
    st.stop()

# Clean whitespace from headers
df.columns = df.columns.str.strip()

# Handle dates and target numeric data
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors="coerce")
df = df.dropna(subset=["Date", "Product_Name", "Category", "Units_Sold"]).copy()

# ============================================================
# SIDEBAR FILTERS
# ============================================================
with st.sidebar:
    st.markdown("### 🔍 Dashboard EDA Filters")

    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    selected_date_range = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="eda_date_filter",
    )

    all_categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
    selected_category = st.selectbox(
        "Product Category", all_categories, index=0, key="eda_category_filter"
    )

    if selected_category != "All":
        filtered_products = sorted(
            df[df["Category"] == selected_category]["Product_Name"].dropna().unique().tolist()
        )
    else:
        filtered_products = sorted(df["Product_Name"].dropna().unique().tolist())

    all_products = ["All"] + filtered_products
    selected_product = st.selectbox(
        "Product Name", all_products, index=0, key="eda_product_filter"
    )

# Apply Filters
filtered_df = df.copy()

if isinstance(selected_date_range, tuple) and len(selected_date_range) == 2:
    start_date, end_date = selected_date_range
    filtered_df = filtered_df[
        (filtered_df["Date"].dt.date >= start_date)
        & (filtered_df["Date"].dt.date <= end_date)
    ]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

if selected_product != "All":
    filtered_df = filtered_df[filtered_df["Product_Name"] == selected_product]

if filtered_df.empty:
    st.warning("⚠️ No data matches the selected filter criteria. Please adjust your filters.")
    st.stop()

# ============================================================
# HEADER & EXECUTIVE METRICS
# ============================================================
render_html(
    f"""
    <div class="hero">
        <h1>📊 {t("historical_sales")} & Feature Analysis</h1>
        <p>Exploratory Data Analysis covering all SME demand factors: pricing elasticity, calendar effects, promotional discounts, weather severity, and correlations.</p>
    </div>
    """
)

st.divider()

total_units_sold = float(filtered_df["Units_Sold"].sum())
daily_sales = filtered_df.groupby("Date")["Units_Sold"].sum()
avg_daily_sales = float(daily_sales.mean())
peak_sales_day = float(daily_sales.max())
unique_products = filtered_df["Product_Name"].nunique()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric(t("total_units"), f"{total_units_sold:,.0f}")
with kpi2:
    st.metric(t("average_daily"), f"{avg_daily_sales:,.1f}")
with kpi3:
    st.metric("Peak Daily Demand", f"{peak_sales_day:,.0f}")
with kpi4:
    st.metric(t("products"), f"{unique_products:,}")

# ============================================================
# 1. TIME SERIES DEMAND & UNITS SOLD DISTRIBUTION
# ============================================================
st.divider()

render_html(
    """
    <div class="section-title">📈 1. Target Demand Trends & Distribution</div>
    """
)

col_ts, col_dist = st.columns([2, 1])

with col_ts:
    st.subheader("Daily Demand Trend (Units_Sold)")
    daily_trend = (
        filtered_df.groupby("Date", as_index=False)["Units_Sold"]
        .sum()
        .sort_values("Date")
    )
    daily_trend["7D_MA"] = daily_trend["Units_Sold"].rolling(7, min_periods=1).mean()

    fig_trend = go.Figure()
    fig_trend.add_trace(
        go.Scatter(
            x=daily_trend["Date"],
            y=daily_trend["Units_Sold"],
            mode="lines",
            name="Daily Units Sold",
            line=dict(color="#3B82F6", width=1),
            opacity=0.4,
        )
    )
    fig_trend.add_trace(
        go.Scatter(
            x=daily_trend["Date"],
            y=daily_trend["7D_MA"],
            mode="lines",
            name="7-Day Moving Avg",
            line=dict(color="#10B981", width=2.5),
        )
    )
    fig_trend.update_layout(
        template="plotly_dark",
        paper_bgcolor="#070B18",
        plot_bgcolor="#070B18",
        font={"color": "#CBD5E1"},
        xaxis_title="Date",
        yaxis_title="Units Sold",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=30, b=20),
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_dist:
    st.subheader("Units_Sold Distribution")
    fig_hist = px.histogram(
        filtered_df,
        x="Units_Sold",
        nbins=30,
        marginal="box",
        color_discrete_sequence=["#8B5CF6"],
    )
    fig_hist.update_layout(
        template="plotly_dark",
        paper_bgcolor="#070B18",
        plot_bgcolor="#070B18",
        font={"color": "#CBD5E1"},
        xaxis_title="Units Sold",
        yaxis_title="Frequency",
        margin=dict(l=20, r=20, t=30, b=20),
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# ============================================================
# 2. PRICING & PROMOTIONAL ELASTICITY
# ============================================================
st.divider()

render_html(
    """
    <div class="section-title">🏷️ 2. Pricing & Discount Impact</div>
    """
)

col_price, col_promo = st.columns(2)

with col_price:
    st.subheader("Unit_Price_NGN vs. Units_Sold")
    if "Unit_Price_NGN" in filtered_df.columns:
        fig_price = px.scatter(
            filtered_df,
            x="Unit_Price_NGN",
            y="Units_Sold",
            color="Category",
            hover_data=["Product_Name"],
            opacity=0.7,
            trendline="ols",
        )
        fig_price.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            xaxis_title="Unit Price (₦)",
            yaxis_title="Units Sold",
            margin=dict(l=10, r=10, t=30, b=10),
        )
        st.plotly_chart(fig_price, use_container_width=True)

with col_promo:
    st.subheader("Discount_Percent & Is_Promotion Impact")
    if "Discount_Percent" in filtered_df.columns and "Is_Promotion" in filtered_df.columns:
        fig_promo = px.box(
            filtered_df,
            x="Is_Promotion",
            y="Units_Sold",
            color="Discount_Percent",
            points="outliers",
            color_discrete_sequence=px.colors.sequential.Viridis,
        )
        fig_promo.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            xaxis_title="Is Promotion Active (0 = No, 1 = Yes)",
            yaxis_title="Units Sold",
            margin=dict(l=10, r=10, t=30, b=10),
        )
        st.plotly_chart(fig_promo, use_container_width=True)

# ============================================================
# 3. CALENDAR & SEASONAL DRIVERS
# ============================================================
st.divider()

render_html(
    """
    <div class="section-title">📅 3. Calendar & Seasonal Drivers</div>
    """
)

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Is_Payday_Period Uplift")
    if "Is_Payday_Period" in filtered_df.columns:
        payday_summary = (
            filtered_df.groupby("Is_Payday_Period", as_index=False)["Units_Sold"]
            .mean()
        )
        payday_summary["Label"] = payday_summary["Is_Payday_Period"].map(
            {0: "Regular Period", 1: "Payday Window (25th-2nd)"}
        )
        fig_payday = px.bar(
            payday_summary,
            x="Label",
            y="Units_Sold",
            color="Label",
            color_discrete_sequence=["#F59E0B", "#10B981"],
        )
        fig_payday.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            xaxis_title="",
            yaxis_title="Avg Units Sold",
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=10),
        )
        st.plotly_chart(fig_payday, use_container_width=True)

with c2:
    st.subheader("Day_of_Week & Is_Weekend")
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
            filtered_df.groupby(["Day_of_Week", "Is_Weekend"], as_index=False)[
                "Units_Sold"
            ]
            .mean()
        )
        dow_summary["Day_of_Week"] = pd.Categorical(
            dow_summary["Day_of_Week"], categories=days_order, ordered=True
        )
        dow_summary = dow_summary.sort_values("Day_of_Week")

        fig_dow = px.bar(
            dow_summary,
            x="Day_of_Week",
            y="Units_Sold",
            color="Is_Weekend",
            color_discrete_sequence=["#3B82F6", "#8B5CF6"],
        )
        fig_dow.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            xaxis_title="",
            yaxis_title="Avg Units Sold",
            margin=dict(l=10, r=10, t=30, b=10),
        )
        st.plotly_chart(fig_dow, use_container_width=True)

with c3:
    st.subheader("Season & Is_Holiday")
    if "Season" in filtered_df.columns and "Is_Holiday" in filtered_df.columns:
        season_summary = (
            filtered_df.groupby(["Season", "Is_Holiday"], as_index=False)[
                "Units_Sold"
            ]
            .mean()
        )
        fig_season = px.bar(
            season_summary,
            x="Season",
            y="Units_Sold",
            color="Is_Holiday",
            barmode="group",
            color_discrete_sequence=["#EC4899", "#14B8A6"],
        )
        fig_season.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            xaxis_title="",
            yaxis_title="Avg Units Sold",
            margin=dict(l=10, r=10, t=30, b=10),
        )
        st.plotly_chart(fig_season, use_container_width=True)

# ============================================================
# 4. RAINFALL SEVERITY & CORRELATION MATRIX
# ============================================================
st.divider()

render_html(
    """
    <div class="section-title">🌧️ 4. Weather Impact & Feature Correlations</div>
    """
)

col_rain, col_corr = st.columns(2)

with col_rain:
    st.subheader("Rainfall_Severity vs. Demand")
    if "Rainfall_Severity" in filtered_df.columns:
        rain_summary = (
            filtered_df.groupby("Rainfall_Severity", as_index=False)["Units_Sold"]
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
            font={"color": "#CBD5E1"},
            xaxis_title="Rainfall Severity",
            yaxis_title="Avg Units Sold",
            coloraxis_showscale=False,
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig_rain, use_container_width=True)

with col_corr:
    st.subheader("Pipeline Feature Correlation Matrix")
    numeric_cols = filtered_df.select_dtypes(include=["number"]).columns.tolist()

    if len(numeric_cols) > 1:
        corr_matrix = filtered_df[numeric_cols].corr()

        fig_corr = px.imshow(
            corr_matrix,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale="Viridis",
            labels=dict(color="Correlation"),
        )
        fig_corr.update_layout(
            template="plotly_dark",
            paper_bgcolor="#070B18",
            plot_bgcolor="#070B18",
            font={"color": "#CBD5E1"},
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig_corr, use_container_width=True)