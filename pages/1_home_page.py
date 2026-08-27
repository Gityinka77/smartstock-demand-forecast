import pandas as pd
import streamlit as st

from styles import (
    apply_global_styles,
    render_header_banner,
)

from utils.data_loader import (
    load_fmcg_data,
    load_model_artifacts,
)

from utils.i18n import t


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock - Home & Introduction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# GLOBAL STYLES & BRANDING
# ============================================================

apply_global_styles()


# ============================================================
# IMPORTANT:
# The SmartStock basket logo and language selector are
# controlled centrally by app.py.
#
# DO NOT render the sidebar logo or language selector here.
# ============================================================


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def render_html(content):
    st.html(content)


# ============================================================
# LOAD APPLICATION DATA & ARTIFACTS
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


# ============================================================
# CLEAN DATASET
# ============================================================

if dataset_available:

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

    df = df.dropna(
        subset=[
            "Date",
            "Product_Name",
            "Category",
            "Units_Sold",
        ]
    ).copy()


# ============================================================
# SIDEBAR — SYSTEM STATUS
# ============================================================

with st.sidebar:

    st.divider()

    st.subheader(
        f"🔎 {t('pipeline_status')}"
    )

    if dataset_available:

        st.success(
            f"✅ {t('data_ready')} — {t('online')}"
        )

    else:

        st.error(
            f"❌ {t('data_ready')} — {t('not_loaded')}"
        )


    if model_available:

        st.success(
            f"✅ {t('production_model')} — {t('online')}"
        )

    else:

        st.error(
            f"❌ {t('production_model')} — {t('not_loaded')}"
        )


    if feature_available:

        st.success(
            f"✅ {t('feature_count')} — {t('online')}"
        )

    else:

        st.error(
            f"❌ {t('feature_count')} — {t('not_loaded')}"
        )


# ============================================================
# HERO INTRODUCTION BANNER
# ============================================================

render_header_banner(
    title=f'🇳🇬 📈 {t("hero_title")}',
    subtitle=t("hero_description"),
)


# ============================================================
# PAGE NAVIGATION & MAP OVERVIEW
# ============================================================

st.divider()

render_html(
    f"""
    <div class="section-title">
        🗺️ {t("application_navigation")}
    </div>

    <div class="section-description">
        {t("application_navigation_description")}
    </div>
    """
)


page_col1, page_col2 = st.columns(2)


# ============================================================
# COLUMN 1
# ============================================================

with page_col1:

    with st.container(border=True):

        st.subheader(
            f"1. 📊 {t('sales_dashboard_title')}"
        )

        st.write(
            t("sales_dashboard_description")
        )


    with st.container(border=True):

        st.subheader(
            f"2. 🔮 {t('demand_forecast_title')}"
        )

        st.write(
            t("demand_forecast_description")
        )


# ============================================================
# COLUMN 2
# ============================================================

with page_col2:

    with st.container(border=True):

        st.subheader(
            f"3. 📦 {t('inventory_advisory_title')}"
        )

        st.write(
            t("inventory_advisory_description")
        )


    with st.container(border=True):

        st.subheader(
            f"4. 📈 {t('model_metrics_title')}"
        )

        st.write(
            t("model_metrics_description")
        )


# ============================================================
# ML PIPELINE OVERVIEW
# ============================================================

st.divider()

render_html(
    f"""
    <div class="section-title">
        ⚙️ {t("ml_pipeline")}
    </div>

    <div class="section-description">
        {t("ml_pipeline_description")}
    </div>
    """
)


pipe_step1, pipe_step2, pipe_step3, pipe_step4 = st.columns(4)


# ============================================================
# STEP 1 — DATA INGESTION
# ============================================================

with pipe_step1:

    with st.container(border=True):

        st.markdown(
            f"#### 1. {t('data_ingestion')}"
        )

        st.caption(
            "`load_fmcg_data()`"
        )

        st.write(
            t("data_ingestion_description")
        )


# ============================================================
# STEP 2 — FEATURE ENGINEERING
# ============================================================

with pipe_step2:

    with st.container(border=True):

        st.markdown(
            f"#### 2. {t('feature_engineering')}"
        )

        st.caption(
            t("calendar_lag_features")
        )

        st.write(
            t("feature_engineering_description")
        )


# ============================================================
# STEP 3 — MODEL TRAINING
# ============================================================

with pipe_step3:

    with st.container(border=True):

        st.markdown(
            f"#### 3. {t('model_training')}"
        )

        st.caption(
            t("gradient_boosting")
        )

        st.write(
            t("model_training_description")
        )


# ============================================================
# STEP 4 — ARTIFACT EXPORT
# ============================================================

with pipe_step4:

    with st.container(border=True):

        st.markdown(
            f"#### 4. {t('artifact_export')}"
        )

        st.caption(
            t("model_artifacts")
        )

        st.write(
            t("artifact_export_description")
        )


# ============================================================
# DATASET SUMMARY HIGHLIGHTS
# ============================================================

if dataset_available:

    st.divider()

    render_html(
        f"""
        <div class="section-title">
            📊 {t("dataset_summary")}
        </div>
        """
    )

    total_units = float(
        df["Units_Sold"].sum()
    )

    daily_demand = (
        df.groupby("Date")["Units_Sold"].sum()
    )

    average_daily_demand = float(
        daily_demand.mean()
    )

    product_count = int(
        df["Product_Name"].nunique()
    )

    category_count = int(
        df["Category"].nunique()
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
            f"{average_daily_demand:,.0f}",
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
# RECOMMENDED WORKFLOW
# ============================================================

st.divider()

render_html(
    f"""
    <div class="section-title">
        🚀 {t("getting_started")}
    </div>
    """
)


st.info(
    f"""
    * **{t("language")}**: {t("choose_language")}

    1. **{t("dashboard")}** — {t("sales_dashboard_description")}

    2. **{t("forecast")}** — {t("demand_forecast_description")}

    3. **{t("stock")}** — {t("inventory_advisory_description")}

    4. **{t("model")}** — {t("model_metrics_description")}

    5. **{t("about")}** — {t("about_project")}
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

render_html(
    f"""
    <div class="footer">
        {t("footer")}
    </div>
    """
)