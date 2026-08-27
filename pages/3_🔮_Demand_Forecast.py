import os

import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from styles import apply_global_styles
from utils.i18n import t


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock Demand Forecast",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_global_styles()


# ============================================================
# PAGE-SPECIFIC VISUAL STYLES
# ============================================================

st.markdown(
    """
    <style>

    .forecast-page-header {
        background:
            linear-gradient(
                135deg,
                #1E40AF 0%,
                #2563EB 48%,
                #0891B2 100%
            );
        border: 1px solid rgba(30, 64, 175, 0.30);
        border-radius: 20px;
        padding: 32px 36px;
        margin-bottom: 26px;
        box-shadow:
            0 12px 30px rgba(15, 23, 42, 0.12);
    }

    .forecast-page-header h1 {
        color: #FFFFFF !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        margin: 0 0 10px 0 !important;
        line-height: 1.2;
    }

    .forecast-page-header p {
        color: #EFF6FF !important;
        font-size: 16px !important;
        line-height: 1.7;
        margin: 0 !important;
        max-width: 950px;
    }

    .forecast-result-card {
        background:
            linear-gradient(
                135deg,
                #172554 0%,
                #1E3A8A 55%,
                #164E63 100%
            );
        border:
            1px solid
            rgba(59, 130, 246, 0.30);
        border-radius: 18px;
        padding: 24px 28px;
        margin: 18px 0 25px 0;
        box-shadow:
            0 12px 30px
            rgba(15, 23, 42, 0.14);
    }

    .forecast-result-title {
        color: #FFFFFF !important;
        font-size: 21px !important;
        font-weight: 800 !important;
        margin-bottom: 8px;
    }

    .forecast-result-description {
        color: #E0F2FE !important;
        font-size: 14px !important;
        line-height: 1.7;
    }

    .forecast-result-description strong {
        color: #FFFFFF !important;
    }

    .forecast-description {
        color: #475569 !important;
        font-size: 14px;
        line-height: 1.65;
        margin-top: -8px;
        margin-bottom: 18px;
    }

    .planning-note {
        background: #E0F2FE;
        border:
            1px solid
            #BAE6FD;
        border-radius: 14px;
        padding: 16px 18px;
        color: #164E63;
        font-size: 14px;
        line-height: 1.65;
        margin: 18px 0 20px 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "smartstock_fmcg_sales.csv",
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "best_gradient_boosting_model.pkl",
)


FEATURE_PATH = os.path.join(
    BASE_DIR,
    "model",
    "model_features.pkl",
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    if not os.path.exists(DATA_PATH):
        return None

    try:

        data = pd.read_csv(DATA_PATH)

        data.columns = (
            data.columns
            .str.strip()
        )

        if "Date" in data.columns:

            data["Date"] = pd.to_datetime(
                data["Date"],
                errors="coerce",
            )

        numeric_columns = [
            "Units_Sold",
            "Unit_Price_NGN",
            "Discount_Percent",
        ]

        for column in numeric_columns:

            if column in data.columns:

                data[column] = pd.to_numeric(
                    data[column],
                    errors="coerce",
                )

        return data

    except Exception:

        return None


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):

        return (
            None,
            None,
            "Model file not found.",
        )

    if not os.path.exists(FEATURE_PATH):

        return (
            None,
            None,
            "Model feature file not found.",
        )

    try:

        model = joblib.load(
            MODEL_PATH
        )

        features = joblib.load(
            FEATURE_PATH
        )

        return (
            model,
            list(features),
            None,
        )

    except Exception as error:

        return (
            None,
            None,
            str(error),
        )


# ============================================================
# LOAD APPLICATION ARTIFACTS
# ============================================================

df = load_data()

model, model_features, model_error = (
    load_model()
)


# ============================================================
# PAGE HEADER
# ============================================================

st.html(
    f"""
    <div class="forecast-page-header">

        <h1>
            📈 {t("forecast")}
        </h1>

        <p>
            Forecast future product demand using the trained
            Gradient Boosting machine-learning model and
            configurable future business assumptions.
        </p>

    </div>
    """
)


# ============================================================
# DATASET CHECK
# ============================================================

if df is None:

    st.error(
        f"❌ {t('dataset')} "
        f"{t('not_loaded')}"
    )

    st.stop()


# ============================================================
# MODEL CHECK
# ============================================================

if model is None:

    st.error(
        f"❌ {t('production_model')} "
        f"{t('not_loaded')}"
    )

    with st.expander(
        t("information")
    ):

        st.code(
            model_error
            if model_error
            else "Unknown model loading error."
        )

    st.stop()


# ============================================================
# FEATURE CHECK
# ============================================================

if model_features is None:

    st.error(
        f"❌ {t('feature_count')} "
        f"{t('not_loaded')}"
    )

    st.stop()


if len(model_features) == 0:

    st.error(
        f"❌ {t('feature_count')} "
        f"{t('not_loaded')}"
    )

    st.stop()


# ============================================================
# VERIFY MODEL FEATURE COUNT
# ============================================================

expected_feature_count = len(
    model_features
)


actual_model_features = getattr(
    model,
    "n_features_in_",
    None,
)


if (
    actual_model_features is not None
    and
    actual_model_features
    != expected_feature_count
):

    st.error(
        "Model feature count does not match "
        "the saved feature definition."
    )

    st.write(
        f"Model expects: "
        f"{actual_model_features}"
    )

    st.write(
        f"Feature file contains: "
        f"{expected_feature_count}"
    )

    st.stop()


# ============================================================
# REQUIRED DATA COLUMNS
# ============================================================

required_columns = [

    "Date",
    "Product_Name",
    "Category",
    "Unit_Price_NGN",
    "Is_Payday_Period",
    "Season",
    "Is_Promotion",
    "Discount_Percent",
    "Is_Weekend",
    "Is_Holiday",
    "Rainfall_Severity",
    "Units_Sold",

]


missing_columns = [

    column

    for column in required_columns

    if column not in df.columns

]


if missing_columns:

    st.error(
        "The sales dataset is missing required columns."
    )

    st.write(
        "Missing columns:"
    )

    st.code(
        "\n".join(
            missing_columns
        )
    )

    st.stop()


# ============================================================
# CLEAN DATA
# ============================================================

df = df.dropna(
    subset=[
        "Date",
        "Product_Name",
        "Units_Sold",
    ]
).copy()


df = df.sort_values(
    [
        "Product_Name",
        "Date",
    ]
).reset_index(
    drop=True
)


# ============================================================
# MODEL STATUS
# ============================================================

st.success(
    f"✅ {t('production_model')} "
    f"{t('online')} "
    f"— {expected_feature_count} features."
)


# ============================================================
# SIDEBAR FORECAST SETTINGS
# ============================================================

with st.sidebar:

    st.title(
        "⚙️ Forecast Settings"
    )

    st.caption(
        "Configure the product, forecast horizon "
        "and future business assumptions."
    )

    st.markdown("---")


# ============================================================
# PRODUCT SELECTION
# ============================================================

products = sorted(
    df["Product_Name"]
    .dropna()
    .astype(str)
    .unique()
)


selected_product = st.sidebar.selectbox(
    "Select Product",
    products,
)


# ============================================================
# FORECAST HORIZON
# ============================================================

forecast_days = st.sidebar.slider(
    "Forecast Horizon (Days)",
    min_value=7,
    max_value=90,
    value=30,
    step=1,
)


# ============================================================
# FUTURE BUSINESS ASSUMPTIONS
# ============================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "📌 Future Business Assumptions"
)


future_promotion = st.sidebar.checkbox(
    "Promotion Active",
    value=False,
)


future_discount = st.sidebar.slider(
    "Discount Percentage",
    min_value=0,
    max_value=20,
    value=0,
    step=5,
)


if not future_promotion:

    future_discount = 0


# ============================================================
# WEATHER ASSUMPTION
# ============================================================

future_rainfall = st.sidebar.selectbox(
    "Rainfall Severity",
    [
        "None",
        "Light",
        "Heavy",
    ],
    index=0,
)


# ============================================================
# SIDEBAR SUMMARY
# ============================================================

st.sidebar.markdown("---")


st.sidebar.caption(
    f"Selected Product: {selected_product}"
)


st.sidebar.caption(
    f"Forecast Horizon: {forecast_days} days"
)


# ============================================================
# PRODUCT DATA
# ============================================================

product_df = df[
    df["Product_Name"]
    .astype(str)
    == selected_product
].copy()


if product_df.empty:

    st.error(
        "No historical data was found "
        "for the selected product."
    )

    st.stop()


product_df = product_df.sort_values(
    "Date"
).reset_index(
    drop=True
)


# ============================================================
# PRODUCT INFORMATION
# ============================================================

product_category = (
    product_df["Category"]
    .dropna()
    .mode()
    .iloc[0]
)


unit_price = float(
    product_df["Unit_Price_NGN"]
    .median()
)


historical_average = float(
    product_df["Units_Sold"]
    .mean()
)


# ============================================================
# HISTORICAL DEMAND SECTION
# ============================================================

st.subheader(
    f"📊 {t('historical_demand')} — "
    f"{selected_product}"
)


st.html(
    f"""
    <div class="forecast-description">
        {t("historical_demand")}
        provides the baseline used by the
        forecasting model.
    </div>
    """
)


# ============================================================
# HISTORICAL KPIs
# ============================================================

kpi1, kpi2, kpi3, kpi4 = (
    st.columns(4)
)


with kpi1:

    st.metric(
        "Historical Records",
        f"{len(product_df):,}",
    )


with kpi2:

    st.metric(
        t("average_daily"),
        f"{historical_average:,.1f}",
    )


with kpi3:

    historical_total = (
        product_df["Units_Sold"]
        .sum()
    )

    st.metric(
        t("total_units"),
        f"{historical_total:,.0f}",
    )


with kpi4:

    st.metric(
        "Unit Price",
        f"₦{unit_price:,.0f}",
    )


# ============================================================
# HISTORICAL CHART DATA
# ============================================================

historical_chart = (
    product_df
    .groupby("Date")["Units_Sold"]
    .sum()
    .reset_index()
    .sort_values("Date")
)


# ============================================================
# HISTORICAL PLOTLY CHART
# ============================================================

fig_history = go.Figure()


fig_history.add_trace(
    go.Scatter(
        x=historical_chart["Date"],
        y=historical_chart["Units_Sold"],
        mode="lines",
        name="Historical Demand",
        line=dict(
            color="#2563EB",
            width=3,
        ),
        hovertemplate=(
            "<b>%{x|%d %b %Y}</b><br>"
            "Units Sold: %{y:,.0f}"
            "<extra></extra>"
        ),
    )
)


fig_history.update_layout(

    template="plotly_white",

    title=dict(
        text="Historical Demand Trend",
        font=dict(
            color="#0F172A",
            size=20,
        ),
    ),

    xaxis=dict(

        title=dict(
            text="Date",
            font=dict(
                color="#334155",
                size=14,
            ),
        ),

        tickfont=dict(
            color="#475569",
            size=12,
        ),

        gridcolor="#CBD5E1",

        zeroline=False,

        linecolor="#94A3B8",

        mirror=True,
    ),

    yaxis=dict(

        title=dict(
            text="Units Sold",
            font=dict(
                color="#334155",
                size=14,
            ),
        ),

        tickfont=dict(
            color="#475569",
            size=12,
        ),

        gridcolor="#CBD5E1",

        zeroline=False,

        linecolor="#94A3B8",

        mirror=True,
    ),

    paper_bgcolor="#E5E7EB",

    plot_bgcolor="#E5E7EB",

    font=dict(
        color="#0F172A",
    ),

    hovermode="x unified",

    hoverlabel=dict(
        bgcolor="#FFFFFF",
        bordercolor="#94A3B8",
        font=dict(
            color="#0F172A",
            size=13,
        ),
    ),

    legend=dict(
        font=dict(
            color="#0F172A",
            size=13,
        ),
        bgcolor="rgba(255,255,255,0.75)",
        bordercolor="#CBD5E1",
        borderwidth=1,
    ),

    margin=dict(
        l=25,
        r=25,
        t=70,
        b=35,
    ),

    height=470,
)


st.plotly_chart(
    fig_history,
    use_container_width=True,
    config={
        "displaylogo": False,
        "responsive": True,
    },
)


# ============================================================
# FORECAST ACTION
# ============================================================

st.markdown("---")


st.subheader(
    "🔮 Generate Forecast"
)


st.html(
    f"""
    <div class="forecast-description">

        Forecast the next
        <strong>{forecast_days} days</strong>
        for
        <strong>{selected_product}</strong>
        using the production model.

    </div>
    """
)


generate_forecast = st.button(
    "🚀 Generate Demand Forecast",
    type="primary",
    use_container_width=True,
)


# ============================================================
# FORECAST ENGINE
# ============================================================

if generate_forecast:

    last_date = product_df[
        "Date"
    ].max()


    future_dates = pd.date_range(
        start=(
            last_date
            +
            pd.Timedelta(days=1)
        ),
        periods=forecast_days,
        freq="D",
    )


    historical_demand = (
        product_df[
            "Units_Sold"
        ]
        .astype(float)
        .tolist()
    )


    forecast_records = []


    for future_date in future_dates:

        lag_1 = (
            historical_demand[-1]
            if len(historical_demand) >= 1
            else historical_average
        )


        lag_7 = (
            historical_demand[-7]
            if len(historical_demand) >= 7
            else historical_average
        )


        last_7_values = (
            historical_demand[-7:]
        )


        rolling_mean_7 = (
            float(
                np.mean(last_7_values)
            )
            if last_7_values
            else historical_average
        )


        rolling_std_7 = (
            float(
                np.std(
                    last_7_values,
                    ddof=1,
                )
            )
            if len(last_7_values) >= 2
            else 0.0
        )


        day_of_month = future_date.day
        month = future_date.month
        quarter = future_date.quarter


        is_weekend = int(
            future_date.weekday() >= 5
        )


        is_payday = int(
            future_date.day >= 25
        )


        is_holiday = int(
            (
                future_date.month == 12
                and future_date.day
                in [
                    24,
                    25,
                    26,
                    31,
                ]
            )
            or
            (
                future_date.month == 1
                and future_date.day == 1
            )
            or
            (
                future_date.month == 10
                and future_date.day == 1
            )
            or
            (
                future_date.month == 5
                and future_date.day == 1
            )
        )


        season = (
            "Rainy"
            if 4 <= month <= 10
            else "Dry"
        )


        row = pd.DataFrame(
            0.0,
            index=[0],
            columns=model_features,
        )


        direct_features = {

            "Unit_Price_NGN":
                unit_price,

            "Is_Payday_Period":
                is_payday,

            "Is_Promotion":
                int(future_promotion),

            "Discount_Percent":
                future_discount,

            "Is_Weekend":
                is_weekend,

            "Is_Holiday":
                is_holiday,

            "Month":
                month,

            "Lag_1":
                lag_1,

            "Lag_7":
                lag_7,

            "Rolling_Mean_7":
                rolling_mean_7,

            "Rolling_Std_7":
                rolling_std_7,

            "Day_of_Month":
                day_of_month,

            "Quarter":
                quarter,
        }


        for feature_name, value in (
            direct_features.items()
        ):

            if feature_name in row.columns:

                row.at[
                    0,
                    feature_name
                ] = value


        category_feature = (
            f"Category_{product_category}"
        )


        if category_feature in row.columns:

            row.at[
                0,
                category_feature
            ] = 1.0


        season_feature = (
            f"Season_{season}"
        )


        if season_feature in row.columns:

            row.at[
                0,
                season_feature
            ] = 1.0


        rainfall_feature = (
            f"Rainfall_Severity_"
            f"{future_rainfall}"
        )


        if rainfall_feature in row.columns:

            row.at[
                0,
                rainfall_feature
            ] = 1.0


        row = row.astype(float)


        try:

            prediction = float(
                model.predict(row)[0]
            )

        except Exception as error:

            st.error(
                "The model prediction failed."
            )

            with st.expander(
                "Prediction error details"
            ):

                st.code(
                    str(error)
                )

                st.write(
                    list(row.columns)
                )

            st.stop()


        prediction = max(
            0,
            prediction
        )


        forecast_records.append(
            {
                "Date":
                    future_date,

                "Product":
                    selected_product,

                "Category":
                    product_category,

                "Forecast Demand":
                    prediction,

                "Promotion":
                    (
                        "Yes"
                        if future_promotion
                        else "No"
                    ),

                "Discount (%)":
                    (
                        future_discount
                        if future_promotion
                        else 0
                    ),

                "Rainfall":
                    future_rainfall,
            }
        )


        historical_demand.append(
            prediction
        )


    forecast_df = pd.DataFrame(
        forecast_records
    )


    forecast_df[
        "Forecast Demand"
    ] = (
        forecast_df[
            "Forecast Demand"
        ]
        .round(0)
        .astype(int)
    )


    total_forecast = (
        forecast_df[
            "Forecast Demand"
        ].sum()
    )


    average_forecast = (
        forecast_df[
            "Forecast Demand"
        ].mean()
    )


    peak_forecast = (
        forecast_df[
            "Forecast Demand"
        ].max()
    )


    minimum_forecast = (
        forecast_df[
            "Forecast Demand"
        ].min()
    )


    # ========================================================
    # FORECAST SUMMARY
    # ========================================================

    st.markdown("---")


    st.subheader(
        "📌 Forecast Summary"
    )


    st.html(
        f"""
        <div class="forecast-description">

            Forecast summary for the next
            <strong>{forecast_days} days</strong>
            under the selected business assumptions.

        </div>
        """
    )


    (
        forecast_kpi1,
        forecast_kpi2,
        forecast_kpi3,
        forecast_kpi4,
    ) = st.columns(4)


    with forecast_kpi1:

        st.metric(
            "Total Forecast",
            f"{total_forecast:,.0f} units",
        )


    with forecast_kpi2:

        st.metric(
            t("average_daily"),
            f"{average_forecast:,.1f} units",
        )


    with forecast_kpi3:

        st.metric(
            "Peak Daily Demand",
            f"{peak_forecast:,.0f} units",
        )


    with forecast_kpi4:

        st.metric(
            "Lowest Daily Demand",
            f"{minimum_forecast:,.0f} units",
        )


    promotion_text = (
        "an active promotion"
        if future_promotion
        else "no promotion"
    )


    st.html(
        f"""
        <div class="forecast-result-card">

            <div class="forecast-result-title">
                📈 Forecast generated successfully
            </div>

            <div class="forecast-result-description">

                The model generated a
                <strong>{forecast_days}-day</strong>
                demand forecast for
                <strong>{selected_product}</strong>.

                The forecast assumes
                <strong>{promotion_text}</strong>,
                a discount of
                <strong>{future_discount}%</strong>,
                and
                <strong>{future_rainfall.lower()}</strong>
                rainfall conditions.

            </div>

        </div>
        """
    )


    # ========================================================
    # COMBINED HISTORICAL + FORECAST CHART
    # ========================================================

    st.markdown("---")


    st.subheader(
        "📈 Historical & Forecast Demand"
    )


    st.html(
        f"""
        <div class="forecast-description">

            Historical demand is shown together with the
            model-generated forecast for
            <strong>{selected_product}</strong>.

        </div>
        """
    )


    combined_fig = go.Figure()


    combined_fig.add_trace(
        go.Scatter(
            x=historical_chart["Date"],
            y=historical_chart["Units_Sold"],
            mode="lines",
            name="Historical Demand",
            line=dict(
                color="#2563EB",
                width=3,
            ),
            hovertemplate=(
                "<b>%{x|%d %b %Y}</b><br>"
                "Historical Demand: "
                "%{y:,.0f} units"
                "<extra></extra>"
            ),
        )
    )


    combined_fig.add_trace(
        go.Scatter(
            x=forecast_df["Date"],
            y=forecast_df["Forecast Demand"],
            mode="lines+markers",
            name="Forecast Demand",
            line=dict(
                color="#EA580C",
                width=3,
            ),
            marker=dict(
                color="#EA580C",
                size=7,
                line=dict(
                    color="#FFFFFF",
                    width=1.5,
                ),
            ),
            hovertemplate=(
                "<b>%{x|%d %b %Y}</b><br>"
                "Forecast Demand: "
                "%{y:,.0f} units"
                "<extra></extra>"
            ),
        )
    )


    combined_fig.update_layout(

        template="plotly_white",

        title=dict(
            text=(
                f"Historical & "
                f"{forecast_days}-Day Forecast — "
                f"{selected_product}"
            ),
            font=dict(
                color="#0F172A",
                size=20,
            ),
        ),

        xaxis=dict(

            title=dict(
                text="Date",
                font=dict(
                    color="#334155",
                    size=14,
                ),
            ),

            tickfont=dict(
                color="#475569",
                size=12,
            ),

            gridcolor="#CBD5E1",

            zeroline=False,

            linecolor="#94A3B8",

            mirror=True,
        ),

        yaxis=dict(

            title=dict(
                text="Units",
                font=dict(
                    color="#334155",
                    size=14,
                ),
            ),

            tickfont=dict(
                color="#475569",
                size=12,
            ),

            gridcolor="#CBD5E1",

            zeroline=False,

            linecolor="#94A3B8",

            mirror=True,
        ),

        paper_bgcolor="#E5E7EB",

        plot_bgcolor="#E5E7EB",

        font=dict(
            color="#0F172A",
        ),

        hovermode="x unified",

        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#94A3B8",
            font=dict(
                color="#0F172A",
                size=13,
            ),
        ),

        legend=dict(
            font=dict(
                color="#0F172A",
                size=13,
            ),
            bgcolor=(
                "rgba(255,255,255,0.75)"
            ),
            bordercolor="#CBD5E1",
            borderwidth=1,
        ),

        margin=dict(
            l=25,
            r=25,
            t=70,
            b=35,
        ),

        height=500,
    )


    st.plotly_chart(
        combined_fig,
        use_container_width=True,
        config={
            "displaylogo": False,
            "responsive": True,
        },
    )


    # ========================================================
    # FORECAST TABLE & EXPORT
    # ========================================================

    st.markdown("---")


    st.subheader(
        "📋 Forecast Data & Export"
    )


    table_display = (
        forecast_df.copy()
    )


    table_display["Date"] = (
        table_display["Date"]
        .dt.strftime("%Y-%m-%d")
    )


    st.dataframe(
        table_display,
        use_container_width=True,
        hide_index=True,
    )


    csv_data = (
        forecast_df
        .to_csv(
            index=False
        )
        .encode("utf-8")
    )


    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv_data,
        file_name=(
            f"{selected_product.lower().replace(' ', '_')}"
            f"_forecast.csv"
        ),
        mime="text/csv",
        use_container_width=True,
    )


    # ========================================================
    # INVENTORY PLANNING NOTE
    # ========================================================

    st.html(
        f"""
        <div class="planning-note">

            💡 <strong>
                Inventory Planning Recommendation:
            </strong>

            Based on the model forecast, plan to stock at least

            <strong>
                {int(total_forecast * 1.10):,} units
            </strong>

            (includes a 10% safety margin buffer) for

            <strong>
                {selected_product}
            </strong>

            over the next
            {forecast_days} days.

        </div>
        """
    )