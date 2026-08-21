import pandas as pd
import plotly.express as px
import streamlit as st

from styles import apply_global_styles, render_sidebar_logo, render_header_banner
from utils.data_loader import load_fmcg_data, load_model_artifacts
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
render_sidebar_logo()

# ============================================================
# HELPER FUNCTIONS
# ============================================================


def render_html(content):
    st.html(content)


# ============================================================
# LOAD APPLICATION DATA & ARTIFACTS
# ============================================================

df = load_fmcg_data()

model, model_features, metrics = None, None, None
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
    df.columns = df.columns.str.strip()
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    if "Units_Sold" in df.columns:
        df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors="coerce")
    df = df.dropna(
        subset=["Date", "Product_Name", "Category", "Units_Sold"]
    ).copy()

# ============================================================
# SIDEBAR (SYSTEM STATUS)
# ============================================================

with st.sidebar:
    st.divider()

    st.subheader("🔎 Pipeline Artifacts Status")

    if dataset_available:
        st.success(f"✅ {t('dataset')} {t('online')}")
    else:
        st.error(f"❌ {t('dataset')} {t('not_loaded')}")

    if model_available:
        st.success(f"✅ {t('production_model')} {t('online')}")
    else:
        st.error(f"❌ {t('production_model')} {t('not_loaded')}")

    if feature_available:
        st.success(f"✅ {t('feature_count')} {t('online')}")
    else:
        st.error(f"❌ {t('feature_count')} {t('not_loaded')}")

# ============================================================
# HERO INTRODUCTION BANNER
# ============================================================

render_header_banner(
    title=f'🇳🇬 📈 {t("hero_title")}',
    subtitle=t("hero_description")
)

# ============================================================
# PAGE NAVIGATION & MAP OVERVIEW
# ============================================================

st.divider()

render_html(
    """
    <div class="section-title">🗺️ SmartStock Application Navigation</div>
    <div class="section-description">Overview of pages and what you can accomplish in each section of the app.</div>
    """
)

page_col1, page_col2 = st.columns(2)

with page_col1:
    with st.container(border=True):
        st.subheader("1. 📊 Sales Dashboard & EDA")
        st.write(
            "Explore historical sales data across FMCG product categories. View unit trends, season patterns, weekend spikes, and correlation matrices computed during exploratory data analysis."
        )

    with st.container(border=True):
        st.subheader("2. 🔮 Demand Forecast")
        st.write(
            "Generate forward-looking daily and weekly demand predictions. Select specific products, promotion toggles, and weather parameters to simulate unit demand driven by our ML model."
        )

with page_col2:
    with st.container(border=True):
        st.subheader("3. 📦 Inventory Advisory & Restock")
        st.write(
            "Translates predicted demand into inventory actions. Calculates safety stock levels, optimal reorder thresholds, lead-time requirements, and alerts for payday stockout risks."
        )

    with st.container(border=True):
        st.subheader("4. 📈 Model Metrics & Pipeline")
        st.write(
            "Inspect the underlying ML architecture trained in `smartstock_ML_Pipeline.ipynb`. Review validation metrics (MAE, RMSE, R²), residual plots, and feature importances."
        )

# ============================================================
# ML PIPELINE OVERVIEW (`smartstock_ML_Pipeline.ipynb`)
# ============================================================

st.divider()

render_html(
    """
    <div class="section-title">⚙️ Machine Learning Pipeline Architecture</div>
    <div class="section-description">How data moves from raw FMCG logs to production model inference.</div>
    """
)

pipe_step1, pipe_step2, pipe_step3, pipe_step4 = st.columns(4)

with pipe_step1:
    with st.container(border=True):
        st.markdown("#### 1. Data Ingestion")
        st.caption("`load_fmcg_data()`")
        st.write(
            "Cleans raw sales records, standardizes dates, and handles missing observations across stores."
        )

with pipe_step2:
    with st.container(border=True):
        st.markdown("#### 2. Feature Engineering")
        st.caption("Calendar & Lag Features")
        st.write(
            "Generates 22 features including payday indicators, promotional flags, rainfall, and festive seasonality."
        )

with pipe_step3:
    with st.container(border=True):
        st.markdown("#### 3. Model Training")
        st.caption("Gradient Boosting Regressor")
        st.write(
            "Trains and tunes regressor models on historical demand, evaluating against MAE, RMSE, and R² targets."
        )

with pipe_step4:
    with st.container(border=True):
        st.markdown("#### 4. Artifact Export")
        st.caption("Joblib / Model Artifacts")
        st.write(
            "Exports model pipelines (`model.pkl`, `features.pkl`, `metrics.json`) for Streamlit runtime inference."
        )

# ============================================================
# HIGHLIGHT DATA KPIs
# ============================================================

if dataset_available:
    st.divider()
    render_html(
        f"""<div class="section-title">📊 Dataset Summary Highlights</div>"""
    )

    total_units = float(df["Units_Sold"].sum())
    daily_demand = df.groupby("Date")["Units_Sold"].sum()
    average_daily_demand = float(daily_demand.mean())
    product_count = int(df["Product_Name"].nunique())
    category_count = int(df["Category"].nunique())

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(t("total_units"), f"{total_units:,.0f}")
    with kpi2:
        st.metric(t("average_daily"), f"{average_daily_demand:,.0f}")
    with kpi3:
        st.metric(t("products"), f"{product_count:,}")
    with kpi4:
        st.metric(t("categories"), f"{category_count:,}")

# ============================================================
# RECOMMENDED WORKFLOW
# ============================================================

st.divider()

render_html(
    """
    <div class="section-title">🚀 Getting Started Workflow</div>
    """
)

st.info(
    """
    * **Language Selection**: Choose preferred language (**English, Nigerian Pidgin, Yoruba, Hausa, Igbo**) from the top sidebar.
    
    1. Go to **`2_📊_Dashboard_EDA.py`** to examine past sales trends.
    2. Go to **`3_🔮_Demand_Forecast.py`** to test real-time model predictions.
    3. Go to **`4_📦_Inventory_Advisory.py`** to get stock reorder levels.
    4. Go to **`5_📈_Model_Metrics.py`** to review model evaluations from `smartstock_ML_Pipeline.ipynb`.
    5. Go to **`6_ℹ️_About.py`** to read about the project background, problem statement, and SME context.
    """
)

# ============================================================
# FOOTER
# ============================================================

st.divider()

render_html(f"""<div class="footer">{t("footer")}</div>""")