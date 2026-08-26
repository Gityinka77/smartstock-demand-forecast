import os

import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from styles import apply_global_styles
from utils.forecast_engine import recursive_forecast


st.set_page_config(
    page_title="SmartStock AI - Demand Forecast",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_global_styles()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "smartstock_fmcg_sales.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model", "best_gradient_boosting_model.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "model", "model_features.pkl")


@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        return None
    data = pd.read_csv(DATA_PATH)
    data.columns = data.columns.str.strip()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Units_Sold"] = pd.to_numeric(data["Units_Sold"], errors="coerce")
    data["Unit_Price_NGN"] = pd.to_numeric(data["Unit_Price_NGN"], errors="coerce")
    return data.dropna(subset=["Date", "Product_Name", "Category", "Units_Sold"]).copy()


@st.cache_resource
def load_model_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        features = list(joblib.load(FEATURE_PATH))
        if not hasattr(model, "predict"):
            raise TypeError("Saved model does not expose predict().")
        if not features:
            raise ValueError("Saved model feature list is empty.")
        expected = getattr(model, "n_features_in_", None)
        if expected is not None and expected != len(features):
            raise ValueError(
                f"Model expects {expected} features but feature file contains {len(features)}."
            )
        return model, features, None
    except Exception as exc:
        return None, None, str(exc)


df = load_data()
model, model_features, model_error = load_model_artifacts()

st.html(
    """
    <div class="hero">
        <h1>🔮 Demand Forecast</h1>
        <p>Forecast future product demand with the production Gradient Boosting model and transparent Nigerian SME business assumptions.</p>
    </div>
    """
)

if df is None:
    st.error("Sales dataset could not be found.")
    st.info(f"Expected file: {DATA_PATH}")
    st.stop()

if model is None:
    st.error("The production forecasting model could not be loaded.")
    st.code(model_error or "Unknown model loading error.")
    st.stop()

required = [
    "Date", "Product_Name", "Category", "Unit_Price_NGN",
    "Is_Payday_Period", "Season", "Is_Promotion", "Discount_Percent",
    "Is_Weekend", "Is_Holiday", "Rainfall_Severity", "Units_Sold",
]
missing = [column for column in required if column not in df.columns]
if missing:
    st.error("The dataset is missing required forecasting columns.")
    st.code("\n".join(missing))
    st.stop()

st.success(f"✅ Production model loaded successfully — {len(model_features)} features.")

with st.sidebar:
    st.title("⚙️ Forecast Settings")
    products = sorted(df["Product_Name"].astype(str).unique())
    selected_product = st.selectbox("Product", products)
    forecast_days = st.slider("Forecast Horizon (days)", 7, 90, 30)
    st.markdown("---")
    promotion = st.checkbox("Promotion Active", value=False)
    discount = st.slider("Discount (%)", 0, 20, 0, 5)
    if not promotion:
        discount = 0
    rainfall = st.selectbox("Rainfall Severity", ["None", "Light", "Heavy"])

product_df = (
    df[df["Product_Name"].astype(str) == selected_product]
    .sort_values("Date")
    .copy()
)
if product_df.empty:
    st.error("No historical records were found for the selected product.")
    st.stop()

category = str(product_df["Category"].mode().iloc[0])
unit_price = float(product_df["Unit_Price_NGN"].median())
historical_average = float(product_df["Units_Sold"].mean())
last_date = product_df["Date"].max()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Historical Records", f"{len(product_df):,}")
k2.metric("Average Daily Demand", f"{historical_average:,.1f}")
k3.metric("Unit Price", f"₦{unit_price:,.0f}")
k4.metric("Last Historical Date", last_date.strftime("%d %b %Y"))

history = product_df.groupby("Date", as_index=False)["Units_Sold"].sum().sort_values("Date")

fig_history = go.Figure()
fig_history.add_trace(go.Scatter(
    x=history["Date"], y=history["Units_Sold"], mode="lines",
    name="Historical Demand", line=dict(width=3),
))
fig_history.update_layout(
    title=f"Historical Demand — {selected_product}",
    template="plotly_white", height=430,
    margin=dict(l=20, r=20, t=60, b=20),
)
st.plotly_chart(fig_history, use_container_width=True, config={"displaylogo": False, "responsive": True})

st.markdown("---")
st.subheader("🚀 Generate Forecast")
st.caption(
    "The forecast uses recursive lag features, the saved model feature order, "
    "and the assumptions selected in the sidebar. The payday window is 25th–2nd."
)

if st.button("Generate Demand Forecast", type="primary", use_container_width=True):
    try:
        forecast_df = recursive_forecast(
            model=model,
            model_features=model_features,
            product_category=category,
            start_date=last_date,
            demand_history=product_df["Units_Sold"].astype(float).tolist(),
            unit_price=unit_price,
            forecast_days=forecast_days,
            promotion=promotion,
            discount_percent=discount,
            rainfall=rainfall,
        )
    except Exception as exc:
        st.error("The model prediction failed.")
        st.code(str(exc))
        st.stop()

    if forecast_df.empty:
        st.warning("No forecast records were generated.")
        st.stop()

    total = int(forecast_df["Forecast Demand"].sum())
    average = float(forecast_df["Forecast Demand"].mean())
    peak = int(forecast_df["Forecast Demand"].max())
    minimum = int(forecast_df["Forecast Demand"].min())

    st.subheader("📌 Forecast Summary")
    a, b, c, d = st.columns(4)
    a.metric("Total Forecast", f"{total:,} units")
    b.metric("Average Daily", f"{average:,.1f} units")
    c.metric("Peak Daily", f"{peak:,} units")
    d.metric("Lowest Daily", f"{minimum:,} units")

    combined = go.Figure()
    combined.add_trace(go.Scatter(
        x=history["Date"], y=history["Units_Sold"], mode="lines",
        name="Historical Demand", line=dict(width=3),
    ))
    combined.add_trace(go.Scatter(
        x=forecast_df["Date"], y=forecast_df["Forecast Demand"], mode="lines+markers",
        name="Forecast Demand", line=dict(width=3),
    ))
    combined.update_layout(
        title=f"Historical & {forecast_days}-Day Forecast — {selected_product}",
        template="plotly_white", height=500,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(combined, use_container_width=True, config={"displaylogo": False, "responsive": True})

    st.subheader("📋 Daily Forecast")
    display_df = forecast_df.copy()
    display_df["Date"] = display_df["Date"].dt.strftime("%Y-%m-%d")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    csv_data = forecast_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Forecast CSV",
        data=csv_data,
        file_name=f"{selected_product.lower().replace(' ', '_')}_forecast.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.info(
        f"Inventory planning baseline: {int(total * 1.10):,} units including a simple 10% buffer. "
        "Use the Inventory Advisory page for lead-time and safety-stock calculations."
    )
