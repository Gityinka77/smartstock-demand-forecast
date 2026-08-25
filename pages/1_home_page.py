import pandas as pd
import plotly.express as px
import streamlit as st

from styles import apply_global_styles, render_header_banner, render_sidebar_logo
from utils.data_loader import load_fmcg_data, load_model_artifacts
from utils.i18n import t


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock AI - Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# GLOBAL STYLES & BRANDING
# ============================================================

apply_global_styles()


# ============================================================
# LOAD DATA & MODEL ARTIFACTS
# ============================================================

df = load_fmcg_data()

model = None
model_features = None
metrics = None
model_available = False
feature_available = False

try:
    model, model_features, metrics = load_model_artifacts()
    model_available = model is not None
    feature_available = model_features is not None
except Exception:
    pass


dataset_available = df is not None

if dataset_available:
    df = df.copy()
    df.columns = df.columns.str.strip()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce",
        )

    if "Units_Sold" in df.columns:
        df["Units_Sold"] = pd.to_numeric(
            df["Units_Sold"],
            errors="coerce",
        )

    required = [
        "Date",
        "Product_Name",
        "Category",
        "Units_Sold",
    ]

    if all(col in df.columns for col in required):
        df = df.dropna(
            subset=required
        ).copy()
    else:
        dataset_available = False


# ============================================================
# SIDEBAR STATUS
# ============================================================

with st.sidebar:

    st.divider()
    st.subheader(f"🔎 {t('model_status')}")

    if dataset_available:
        st.success(
            f"✅ {t('dataset')} {t('online')}"
        )
    else:
        st.error(
            f"❌ {t('dataset')} {t('not_loaded')}"
        )

    if model_available:
        st.success(
            f"✅ {t('production_model')} {t('online')}"
        )
    else:
        st.error(
            f"❌ {t('production_model')} {t('not_loaded')}"
        )

    if feature_available:
        st.success(
            f"✅ {t('feature_count')} {t('online')}"
        )
    else:
        st.error(
            f"❌ {t('feature_count')} {t('not_loaded')}"
        )


# ============================================================
# HERO
# ============================================================

render_header_banner(
    title=f"🇳🇬 📈 {t('hero_title')}",
    subtitle=t("hero_description"),
)


# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

if dataset_available:

    st.divider()

    total_units = float(
        df["Units_Sold"].sum()
    )

    daily_demand = (
        df.groupby("Date")["Units_Sold"]
        .sum()
    )

    average_daily = float(
        daily_demand.mean()
    )

    product_count = int(
        df["Product_Name"].nunique()
    )

    category_count = int(
        df["Category"].nunique()
    )

    st.markdown(
        f"<div class='section-title'>📊 {t('historical_sales')}</div>",
        unsafe_allow_html=True,
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            t("total_units"),
            f"{total_units:,.0f}",
        )

    with kpi2:
        st.metric(
            t("average_daily"),
            f"{average_daily:,.0f}",
        )

    with kpi3:
        st.metric(
            t("products"),
            f"{product_count:,}",
        )

    with kpi4:
        st.metric(
            t("categories"),
            f"{category_count:,}",
        )


# ============================================================
# WHAT SMARTSTOCK DOES
# ============================================================

st.divider()

st.markdown(
    f"<div class='section-title'>💡 {t('what_smartstock_does')}</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='section-description'>{t('hero_description')}</div>",
    unsafe_allow_html=True,
)

what1, what2, what3 = st.columns(3)

with what1:
    with st.container(border=True):
        st.subheader(f"📊 {t('understand_demand')}")
        st.write(t("understand_demand_text"))

with what2:
    with st.container(border=True):
        st.subheader(f"🔮 {t('forecast_future')}")
        st.write(t("forecast_future_text"))

with what3:
    with st.container(border=True):
        st.subheader(f"📦 {t('stock_decisions')}")
        st.write(t("stock_decisions_text"))


# ============================================================
# HISTORICAL DEMAND & TOP PRODUCTS
# ============================================================

if dataset_available:

    st.divider()

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown(
            f"### 📈 {t('historical_demand')}"
        )

        trend_df = (
            df.groupby("Date")["Units_Sold"]
            .sum()
            .reset_index()
            .sort_values("Date")
        )

        fig_trend = px.line(
            trend_df,
            x="Date",
            y="Units_Sold",
            labels={
                "Date": "Date",
                "Units_Sold": "Units Sold",
            },
            template="plotly_white",
        )

        fig_trend.update_traces(
            line_width=3,
        )

        fig_trend.update_layout(
            margin=dict(l=10, r=10, t=20, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        st.plotly_chart(
            fig_trend,
            use_container_width=True,
        )

    with chart_col2:

        st.markdown(
            f"### 🏆 {t('top_products')}"
        )

        top_products = (
            df.groupby("Product_Name")["Units_Sold"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .sort_values()
            .reset_index()
        )

        fig_products = px.bar(
            top_products,
            x="Units_Sold",
            y="Product_Name",
            orientation="h",
            labels={
                "Units_Sold": "Units Sold",
                "Product_Name": "Product",
            },
            template="plotly_white",
        )

        fig_products.update_layout(
            margin=dict(l=10, r=10, t=20, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        st.plotly_chart(
            fig_products,
            use_container_width=True,
        )


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

if dataset_available:

    st.divider()

    st.markdown(
        f"### 💼 {t('business_insights')}"
    )

    total_by_product = (
        df.groupby("Product_Name")["Units_Sold"]
        .sum()
        .sort_values(ascending=False)
    )

    total_by_category = (
        df.groupby("Category")["Units_Sold"]
        .sum()
        .sort_values(ascending=False)
    )

    weekday_demand = (
        df.assign(
            DayOfWeek=df["Date"].dt.dayofweek
        )
        .groupby("DayOfWeek")["Units_Sold"]
        .mean()
    )

    highest_product = (
        str(total_by_product.index[0])
        if not total_by_product.empty
        else "—"
    )

    leading_category = (
        str(total_by_category.index[0])
        if not total_by_category.empty
        else "—"
    )

    weekday_avg = float(
        weekday_demand.loc[
            weekday_demand.index < 5
        ].mean()
        if not weekday_demand.loc[weekday_demand.index < 5].empty
        else 0
    )

    weekend_avg = float(
        weekday_demand.loc[
            weekday_demand.index >= 5
        ].mean()
        if not weekday_demand.loc[weekday_demand.index >= 5].empty
        else 0
    )

    weekend_effect = (
        ((weekend_avg - weekday_avg) / weekday_avg * 100)
        if weekday_avg > 0
        else 0
    )

    insight1, insight2, insight3 = st.columns(3)

    with insight1:
        with st.container(border=True):
            st.markdown(
                f"**🏆 {t('highest_product')}**"
            )
            st.markdown(
                f"### {highest_product}"
            )

    with insight2:
        with st.container(border=True):
            st.markdown(
                f"**📦 {t('leading_category')}**"
            )
            st.markdown(
                f"### {leading_category}"
            )

    with insight3:
        with st.container(border=True):
            st.markdown(
                f"**📅 {t('weekend_effect')}**"
            )
            st.markdown(
                f"### {weekend_effect:+.1f}%"
            )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.markdown(
    f"### 🧠 {t('model_performance')}"
)

if model_available:

    perf_col1, perf_col2, perf_col3 = st.columns(3)

    saved_metrics = metrics if isinstance(metrics, dict) else {}

    r2_value = saved_metrics.get(
        "R2",
        saved_metrics.get("r2", 0),
    )

    mae_value = saved_metrics.get(
        "MAE",
        saved_metrics.get("mae", None),
    )

    rmse_value = saved_metrics.get(
        "RMSE",
        saved_metrics.get("rmse", None),
    )

    with perf_col1:
        st.metric(
            t("official_r2"),
            f"{float(r2_value):.4f}" if r2_value is not None else "—",
        )

    with perf_col2:
        st.metric(
            "MAE",
            f"{float(mae_value):.2f}" if mae_value is not None else "—",
        )

    with perf_col3:
        st.metric(
            "RMSE",
            f"{float(rmse_value):.2f}" if rmse_value is not None else "—",
        )

    st.success(
        f"✅ {t('production_online')}"
    )

else:

    st.warning(
        f"⚠️ {t('production_unavailable')}"
    )


# ============================================================
# NIGERIAN SME CONTEXT
# ============================================================

st.divider()

with st.container(border=True):

    st.subheader(
        f"🇳🇬 {t('nigerian_context')}"
    )

    context_cols = st.columns(2)

    with context_cols[0]:
        st.markdown(
            f"""
            - 💰 {t('payday')}
            - 🎯 {t('promotions')}
            - 🏷️ {t('discounts')}
            - 📅 {t('weekends')}
            """
        )

    with context_cols[1]:
        st.markdown(
            f"""
            - 🎉 {t('festivals')}
            - 🌦️ {t('seasonality')}
            - 🌧️ {t('rainfall')}
            - 📦 {t('stock_decisions')}
            """
        )


# ============================================================
# WORKFLOW
# ============================================================

st.divider()

st.markdown("### 🚀 SmartStock Workflow")

workflow1, workflow2, workflow3, workflow4 = st.columns(4)

with workflow1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.write(t("understand_demand"))

with workflow2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.write(t("forecast_future"))

with workflow3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.write(t("stock_decisions"))

with workflow4:
    with st.container(border=True):
        st.markdown("### 4️⃣")
        st.write(t("read_about"))


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    f"<div class='footer'>{t('footer')}</div>",
    unsafe_allow_html=True,
)
