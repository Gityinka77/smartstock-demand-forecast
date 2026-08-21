import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st

from styles import apply_global_styles

# Flexible import fallback in case data_loader function naming varies
try:
    from utils.data_loader import (
        load_sales_data,
        detect_columns,
        load_model_artifacts
    )
except ImportError:
    from utils.data_loader import (
        load_data as load_sales_data,
        detect_columns,
        load_model_artifacts
    )


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock - Inventory Advisory",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# GLOBAL STYLES
# ============================================================

apply_global_styles()


# ============================================================
# PAGE-SPECIFIC STYLES
# ============================================================

st.markdown(
    """
    <style>
    .stock-header {
        background: linear-gradient(135deg, #0F172A 0%, #172554 55%, #164E63 100%);
        padding: 30px 32px;
        border-radius: 20px;
        margin-bottom: 25px;
        border: 1px solid rgba(129, 140, 248, 0.25);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
    }

    .stock-header-title {
        color: #FFFFFF !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        margin-bottom: 8px;
    }

    .stock-header-description {
        color: #CBD5E1 !important;
        font-size: 16px;
        line-height: 1.7;
        max-width: 950px;
    }

    .recommendation-box {
        background: linear-gradient(135deg, #111827, #172554);
        border: 1px solid rgba(99, 102, 241, 0.35);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 0 25px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.22);
    }

    .recommendation-box-title {
        color: #FFFFFF !important;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .recommendation-box-description {
        color: #CBD5E1 !important;
        font-size: 15px;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE HEADER
# ============================================================

st.html(
    """
    <div class="stock-header">
        <div class="stock-header-title">
            📦 Stock & Reorder
        </div>
        <div class="stock-header-description">
            Convert demand forecasts into practical inventory
            and reorder recommendations for your business.
        </div>
    </div>
    """
)


# ============================================================
# LOAD DATA & MODEL
# ============================================================

df = load_sales_data()
column_map = detect_columns(df) if df is not None else {}
model, model_features, model_error = load_model_artifacts()


# ============================================================
# VALIDATION CHECKS
# ============================================================

if df is None:
    st.error("Sales dataset could not be found.")
    st.info("Expected file: data/smartstock_fmcg_sales.csv")
    st.stop()

if model is None:
    st.error("The trained demand forecasting model could not be loaded.")
    if model_error:
        st.code(model_error)
    st.stop()

date_column = column_map.get("date")
product_column = column_map.get("product")
category_column = column_map.get("category")
demand_column = column_map.get("demand")
price_column = column_map.get("price")

required_columns = [date_column, product_column, category_column, demand_column, price_column]
missing_required = [col for col in required_columns if col is None]

if missing_required:
    st.error("The sales dataset does not contain all required columns for stock recommendations.")
    st.write("Detected columns:", df.columns.tolist())
    st.stop()


# ============================================================
# PREPARE DATA
# ============================================================

df = df.copy()
df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
df[demand_column] = pd.to_numeric(df[demand_column], errors="coerce")
df[price_column] = pd.to_numeric(df[price_column], errors="coerce")

df = df.dropna(subset=[date_column, product_column, demand_column, price_column]).copy()
df = df.sort_values([product_column, date_column]).reset_index(drop=True)

st.success("✅ Gradient Boosting demand model loaded successfully.")


# ============================================================
# INVENTORY SETTINGS
# ============================================================

st.markdown("---")
st.subheader("⚙️ Stock & Reorder Parameters")

settings_col1, settings_col2 = st.columns(2)

with settings_col1:
    products = sorted(df[product_column].dropna().astype(str).unique().tolist())
    selected_product = st.selectbox("Select Product", products)

with settings_col2:
    current_stock = st.number_input("Current Stock (units)", min_value=0, value=100, step=1)

planning_col1, planning_col2, planning_col3 = st.columns(3)

with planning_col1:
    forecast_days = st.slider("Forecast Horizon (days)", min_value=7, max_value=90, value=30, step=1)

with planning_col2:
    lead_time_days = st.number_input("Supplier Lead Time (days)", min_value=1, max_value=90, value=7, step=1)

with planning_col3:
    safety_stock_days = st.number_input("Safety Stock Coverage (days)", min_value=0, max_value=30, value=3, step=1)


# ============================================================
# FUTURE ASSUMPTIONS
# ============================================================

st.markdown("---")
st.subheader("🔮 Future Demand Assumptions")
st.caption("These assumptions are used because future promotions and rainfall are unknown at prediction time.")

assumption_col1, assumption_col2, assumption_col3 = st.columns(3)

with assumption_col1:
    promotion_assumption = st.selectbox("Promotion Assumption", ["No Promotion", "Promotion"])

with assumption_col2:
    discount_assumption = st.selectbox("Expected Discount", [0, 5, 10, 15, 20], format_func=lambda x: f"{x}%")

with assumption_col3:
    rainfall_assumption = st.selectbox("Rainfall Assumption", ["None", "Light", "Heavy"])


# ============================================================
# PRODUCT DATA & METRICS
# ============================================================

product_df = df[df[product_column].astype(str) == selected_product].copy()

if product_df.empty:
    st.error("No historical records were found for the selected product.")
    st.stop()

product_category = product_df[category_column].mode().iloc[0]
product_price = float(product_df[price_column].iloc[-1])
last_historical_date = product_df[date_column].max()

st.markdown("---")
st.subheader("📋 Product Information")

info1, info2, info3, info4 = st.columns(4)
with info1:
    st.metric("Product", selected_product)
with info2:
    st.metric("Category", str(product_category))
with info3:
    st.metric("Unit Price", f"₦{product_price:,.0f}")
with info4:
    st.metric("Last Sales Date", last_historical_date.strftime("%d %b %Y"))


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def is_future_holiday(date):
    if date.month == 12 and date.day in [24, 25, 26, 31]:
        return 1
    if date.month in [1, 5, 10] and date.day == 1:
        return 1
    return 0

def get_season(date):
    return "Rainy" if 4 <= date.month <= 10 else "Dry"


# ============================================================
# FORECAST ENGINE & RECOMMENDATION GENERATION
# ============================================================

generate_recommendation = st.button("🚀 Calculate Reorder Point", type="primary", use_container_width=True)

if generate_recommendation:
    history_demand = product_df.sort_values(date_column)[demand_column].astype(float).tolist()
    future_dates = pd.date_range(start=last_historical_date + pd.Timedelta(days=1), periods=forecast_days, freq="D")
    fallback_demand = float(np.mean(history_demand)) if len(history_demand) > 0 else 0.0

    forecast_records = []

    for future_date in future_dates:
        day_of_month = future_date.day
        month = future_date.month
        quarter = future_date.quarter
        is_weekend = int(future_date.weekday() >= 5)
        is_payday = int(day_of_month >= 25)
        is_holiday = is_future_holiday(future_date)
        season = get_season(future_date)

        is_promotion = 1 if promotion_assumption == "Promotion" else 0
        discount_percent = int(discount_assumption) if is_promotion else 0

        lag_1 = history_demand[-1] if len(history_demand) >= 1 else fallback_demand
        lag_7 = history_demand[-7] if len(history_demand) >= 7 else fallback_demand
        recent_7 = history_demand[-7:]

        rolling_mean_7 = float(np.mean(recent_7)) if len(recent_7) > 0 else fallback_demand
        rolling_std_7 = float(np.std(recent_7, ddof=1)) if len(recent_7) > 1 else 0.0

        feature_row = {
            "Unit_Price_NGN": product_price,
            "Is_Payday_Period": is_payday,
            "Is_Promotion": is_promotion,
            "Discount_Percent": discount_percent,
            "Is_Weekend": is_weekend,
            "Is_Holiday": is_holiday,
            "Month": month,
            "Lag_1": lag_1,
            "Lag_7": lag_7,
            "Rolling_Mean_7": rolling_mean_7,
            "Rolling_Std_7": rolling_std_7,
            "Day_of_Month": day_of_month,
            "Quarter": quarter,
            "Category_Beverages": 0,
            "Category_Dairy": 0,
            "Category_Grains": 0,
            "Category_Pantry": 0,
            "Category_Staples": 0,
            "Category_Toiletries": 0,
            "Season_Rainy": int(season == "Rainy"),
            "Rainfall_Severity_Light": int(rainfall_assumption == "Light"),
            "Rainfall_Severity_None": int(rainfall_assumption == "None")
        }

        category_feature = f"Category_{product_category}"
        if category_feature in feature_row:
            feature_row[category_feature] = 1

        input_df = pd.DataFrame([feature_row])
        
        for feature in model_features:
            if feature not in input_df.columns:
                input_df[feature] = 0

        input_df = input_df[model_features]

        try:
            prediction = float(model.predict(input_df)[0])
        except Exception as error:
            st.error("Demand prediction failed.")
            st.code(str(error))
            st.stop()

        prediction = max(0.0, prediction)

        forecast_records.append({
            "Date": future_date,
            "Forecast Demand": prediction,
            "Season": season,
            "Promotion": is_promotion,
            "Discount %": discount_percent,
            "Weekend": is_weekend,
            "Holiday": is_holiday,
            "Rainfall": rainfall_assumption
        })

        history_demand.append(prediction)

    forecast_df = pd.DataFrame(forecast_records)
    forecast_df["Forecast Demand"] = forecast_df["Forecast Demand"].round(0).astype(int)

    # Metrics and inventory math
    total_forecast = float(forecast_df["Forecast Demand"].sum())
    average_daily_demand = float(forecast_df["Forecast Demand"].mean())
    peak_daily_demand = float(forecast_df["Forecast Demand"].max())

    lead_time_demand = average_daily_demand * lead_time_days
    safety_stock = average_daily_demand * safety_stock_days
    required_stock = lead_time_demand + safety_stock
    reorder_quantity = max(0.0, required_stock - current_stock)
    stock_after_reorder = current_stock + reorder_quantity

    # Status evaluation
    if current_stock < lead_time_demand:
        status = "🔴 REORDER NOW"
        status_description = "Current stock is below estimated demand during supplier lead time."
    elif current_stock < required_stock:
        status = "🟡 MONITOR STOCK"
        status_description = "Current stock covers lead-time demand but lacks sufficient safety stock buffer."
    else:
        status = "🟢 HEALTHY STOCK"
        status_description = "Current stock meets lead-time demand and safety stock requirements."

    # UI Rendering
    st.markdown("---")
    st.subheader("📊 Stock Status & Reorder Summary")
    st.html(f"""
        <div class="recommendation-box">
            <div class="recommendation-box-title">{status}</div>
            <div class="recommendation-box-description">{status_description}</div>
        </div>
    """)

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Current Stock", f"{current_stock:,.0f} units")
    with kpi2:
        st.metric("Forecast Demand", f"{total_forecast:,.0f} units")
    with kpi3:
        st.metric("Required Stock", f"{required_stock:,.0f} units")
    with kpi4:
        st.metric("Recommended Reorder", f"{reorder_quantity:,.0f} units")

    st.markdown("---")
    st.subheader("📦 Inventory Requirement Breakdown")
    b1, b2, b3 = st.columns(3)
    with b1:
        st.metric("Lead-Time Demand", f"{lead_time_demand:,.0f} units")
    with b2:
        st.metric("Safety Stock Buffer", f"{safety_stock:,.0f} units")
    with b3:
        st.metric("Stock After Reorder", f"{stock_after_reorder:,.0f} units")

    # Inventory chart
    st.markdown("---")
    st.subheader("📊 Current Stock vs Required Stock")
    inv_df = pd.DataFrame({
        "Metric": ["Current Stock", "Lead-Time Demand", "Safety Stock", "Required Stock"],
        "Units": [current_stock, lead_time_demand, safety_stock, required_stock]
    })

    inv_fig = go.Figure(go.Bar(
        x=inv_df["Metric"],
        y=inv_df["Units"],
        text=[f"{v:,.0f}" for v in inv_df["Units"]],
        textposition="auto",
        textfont=dict(color="#FFFFFF", size=14)
    ))
    inv_fig.update_layout(
        title=dict(text=f"{selected_product} — Reorder Profile", font=dict(color="#FFFFFF", size=20)),
        xaxis=dict(title=dict(text="Inventory Measure", font=dict(color="#CBD5E1")), tickfont=dict(color="#CBD5E1")),
        yaxis=dict(title=dict(text="Units", font=dict(color="#CBD5E1")), tickfont=dict(color="#CBD5E1"), gridcolor="rgba(148,163,184,0.20)"),
        showlegend=False,
        template="plotly_dark",
        paper_bgcolor="#070B18",
        plot_bgcolor="#070B18"
    )
    st.plotly_chart(inv_fig, use_container_width=True)

    # Forecast timeline chart
    st.markdown("---")
    st.subheader("📈 Historical Sales vs Forecast Horizon")
    hist_chart = product_df.groupby(date_column)[demand_column].sum().reset_index().sort_values(date_column).tail(90)

    fc_fig = go.Figure()
    fc_fig.add_trace(go.Scatter(
        x=hist_chart[date_column],
        y=hist_chart[demand_column],
        mode="lines",
        name="Historical Demand",
        line=dict(width=3, color="#6366F1")
    ))
    fc_fig.add_trace(go.Scatter(
        x=forecast_df["Date"],
        y=forecast_df["Forecast Demand"],
        mode="lines+markers",
        name="Forecast Demand",
        line=dict(width=4, color="#FF6B35"),
        marker=dict(size=7, color="#FF6B35")
    ))
    fc_fig.update_layout(
        title=dict(text=f"{selected_product} — Historical and Forecast Demand", font=dict(color="#FFFFFF", size=20)),
        xaxis=dict(title=dict(text="Date", font=dict(color="#CBD5E1")), tickfont=dict(color="#CBD5E1"), gridcolor="rgba(148,163,184,0.15)"),
        yaxis=dict(title=dict(text="Units", font=dict(color="#CBD5E1")), tickfont=dict(color="#CBD5E1"), gridcolor="rgba(148,163,184,0.20)"),
        legend=dict(font=dict(color="#FFFFFF"), bgcolor="rgba(7,11,24,0.65)"),
        template="plotly_dark",
        paper_bgcolor="#070B18",
        plot_bgcolor="#070B18"
    )
    st.plotly_chart(fc_fig, use_container_width=True)

    # Forecast Details & Downloads
    st.markdown("---")
    st.subheader("📋 Detailed Daily Forecast")
    disp_df = forecast_df.copy()
    disp_df["Date"] = disp_df["Date"].dt.strftime("%d %b %Y")
    st.dataframe(disp_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("💡 Stock & Reorder Action Plan")
    if reorder_quantity > 0:
        st.warning(f"**Action Required: Reorder {reorder_quantity:,.0f} units.**\n\nPlace an order for **{reorder_quantity:,.0f} units** of **{selected_product}** to cover estimated sales during supplier lead time and maintain safety stock.")
    else:
        st.success(f"**Action Required: No immediate reorder needed.**\n\nYour current stock of **{current_stock:,.0f} units** is adequate to cover upcoming demand.")

    rec_csv = pd.DataFrame([{
        "Product": selected_product,
        "Category": product_category,
        "Current Stock": current_stock,
        "Forecast Horizon Days": forecast_days,
        "Total Forecast Demand": total_forecast,
        "Average Daily Demand": average_daily_demand,
        "Peak Daily Demand": peak_daily_demand,
        "Lead Time Days": lead_time_days,
        "Lead Time Demand": lead_time_demand,
        "Safety Stock Days": safety_stock_days,
        "Safety Stock": safety_stock,
        "Required Stock": required_stock,
        "Recommended Reorder Quantity": reorder_quantity,
        "Status": status
    }]).to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Reorder Report",
        data=rec_csv,
        file_name=f"stock_reorder_report_{selected_product}.csv",
        mime="text/csv",
        use_container_width=True
    )