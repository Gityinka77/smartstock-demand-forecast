import os

import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from styles import apply_global_styles
from utils.forecast_engine import recursive_forecast


st.set_page_config(
    page_title="SmartStock AI - Inventory Advisory",
    page_icon="📦",
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
    return data.dropna(subset=["Date", "Product_Name", "Category", "Units_Sold", "Unit_Price_NGN"]).copy()


@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        features = list(joblib.load(FEATURE_PATH))
        if not hasattr(model, "predict"):
            raise TypeError("Saved model does not expose predict().")
        expected = getattr(model, "n_features_in_", None)
        if expected is not None and expected != len(features):
            raise ValueError(f"Model expects {expected} features but feature file contains {len(features)}.")
        return model, features, None
    except Exception as exc:
        return None, None, str(exc)


df = load_data()
model, model_features, error = load_artifacts()

st.html(
    """
    <div class="hero">
        <h1>📦 Inventory Advisory</h1>
        <p>Translate forecast demand into reorder-point, lead-time and safety-stock decisions for Nigerian SMEs.</p>
    </div>
    """
)

if df is None:
    st.error("Sales dataset could not be found.")
    st.info(f"Expected file: {DATA_PATH}")
    st.stop()
if model is None:
    st.error("The production forecasting model could not be loaded.")
    st.code(error or "Unknown model loading error.")
    st.stop()

required = [
    "Date", "Product_Name", "Category", "Unit_Price_NGN", "Units_Sold",
    "Is_Payday_Period", "Season", "Is_Promotion", "Discount_Percent",
    "Is_Weekend", "Is_Holiday", "Rainfall_Severity",
]
missing = [c for c in required if c not in df.columns]
if missing:
    st.error("The dataset is missing inventory/forecast columns.")
    st.code("\n".join(missing))
    st.stop()

with st.sidebar:
    st.title("⚙️ Stock Settings")
    products = sorted(df["Product_Name"].astype(str).unique())
    selected_product = st.selectbox("Product", products)
    current_stock = st.number_input("Current Stock (units)", min_value=0, value=100, step=1)
    forecast_days = st.slider("Forecast Horizon (days)", 7, 90, 30)
    lead_time_days = st.number_input("Supplier Lead Time (days)", 1, 90, 7)
    safety_stock_days = st.number_input("Safety Stock Coverage (days)", 0, 30, 3)
    st.markdown("---")
    promotion = st.checkbox("Promotion Assumption", value=False)
    discount = st.slider("Expected Discount (%)", 0, 20, 0, 5)
    if not promotion:
        discount = 0
    rainfall = st.selectbox("Rainfall Assumption", ["None", "Light", "Heavy"])

product_df = (
    df[df["Product_Name"].astype(str) == selected_product]
    .sort_values("Date")
    .copy()
)
category = str(product_df["Category"].mode().iloc[0])
unit_price = float(product_df["Unit_Price_NGN"].median())
last_date = product_df["Date"].max()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Product", selected_product)
k2.metric("Category", category)
k3.metric("Unit Price", f"₦{unit_price:,.0f}")
k4.metric("Current Stock", f"{current_stock:,} units")

st.caption(
    "Reorder point logic: expected demand during supplier lead time + safety-stock coverage. "
    "It is not a purchase order and should be reviewed against supplier constraints."
)

if st.button("🚀 Calculate Reorder Recommendation", type="primary", use_container_width=True):
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
        st.error("Demand prediction failed.")
        st.code(str(exc))
        st.stop()

    average_daily = float(forecast_df["Forecast Demand"].mean())
    peak_daily = float(forecast_df["Forecast Demand"].max())
    total_forecast = int(forecast_df["Forecast Demand"].sum())

    lead_time_demand = average_daily * lead_time_days
    safety_stock = average_daily * safety_stock_days
    reorder_point = lead_time_demand + safety_stock
    reorder_quantity = max(0.0, reorder_point - current_stock)

    if current_stock < lead_time_demand:
        status = "🔴 REORDER NOW"
        description = "Current stock is below estimated demand during supplier lead time."
    elif current_stock < reorder_point:
        status = "🟡 MONITOR / REORDER"
        description = "Current stock covers lead-time demand but not the selected safety-stock buffer."
    else:
        status = "🟢 HEALTHY STOCK"
        description = "Current stock covers lead-time demand and the selected safety-stock buffer."

    st.markdown("---")
    st.subheader("📊 Stock Decision")
    st.html(
        f"""
        <div class="hero">
            <h2>{status}</h2>
            <p>{description}</p>
        </div>
        """
    )

    a, b, c, d = st.columns(4)
    a.metric("Forecast Demand", f"{total_forecast:,} units")
    b.metric("Avg Daily Demand", f"{average_daily:,.1f}")
    c.metric("Reorder Point", f"{reorder_point:,.0f} units")
    d.metric("Recommended Reorder", f"{reorder_quantity:,.0f} units")

    st.subheader("📦 Inventory Requirement Breakdown")
    x, y, z = st.columns(3)
    x.metric("Lead-Time Demand", f"{lead_time_demand:,.0f} units")
    y.metric("Safety Stock", f"{safety_stock:,.0f} units")
    z.metric("Peak Forecast Day", f"{peak_daily:,.0f} units")

    st.markdown("---")
    st.subheader("📊 Stock vs Requirement")
    chart_df = pd.DataFrame({
        "Measure": ["Current Stock", "Lead-Time Demand", "Safety Stock", "Reorder Point"],
        "Units": [current_stock, lead_time_demand, safety_stock, reorder_point],
    })
    fig = go.Figure(go.Bar(x=chart_df["Measure"], y=chart_df["Units"], text=[f"{v:,.0f}" for v in chart_df["Units"]], textposition="auto"))
    fig.update_layout(template="plotly_white", height=430, showlegend=False, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Historical vs Forecast")
    history = product_df.groupby("Date", as_index=False)["Units_Sold"].sum().sort_values("Date").tail(90)
    combined = go.Figure()
    combined.add_trace(go.Scatter(x=history["Date"], y=history["Units_Sold"], mode="lines", name="Historical"))
    combined.add_trace(go.Scatter(x=forecast_df["Date"], y=forecast_df["Forecast Demand"], mode="lines+markers", name="Forecast"))
    combined.update_layout(template="plotly_white", height=480, hovermode="x unified", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(combined, use_container_width=True)

    st.subheader("📋 Daily Forecast")
    display = forecast_df.copy()
    display["Date"] = display["Date"].dt.strftime("%Y-%m-%d")
    st.dataframe(display, use_container_width=True, hide_index=True)

    report = pd.DataFrame([{
        "Product": selected_product,
        "Category": category,
        "Current Stock": current_stock,
        "Forecast Horizon Days": forecast_days,
        "Total Forecast Demand": total_forecast,
        "Average Daily Demand": average_daily,
        "Peak Daily Demand": peak_daily,
        "Lead Time Days": lead_time_days,
        "Lead Time Demand": lead_time_demand,
        "Safety Stock Days": safety_stock_days,
        "Safety Stock": safety_stock,
        "Reorder Point": reorder_point,
        "Recommended Reorder Quantity": reorder_quantity,
        "Status": status,
    }])
    st.download_button(
        "📥 Download Reorder Report",
        data=report.to_csv(index=False).encode("utf-8"),
        file_name=f"stock_reorder_report_{selected_product.lower().replace(' ', '_')}.csv",
        mime="text/csv",
        use_container_width=True,
    )
