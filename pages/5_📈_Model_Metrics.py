from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from styles import apply_global_styles


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "smartstock_fmcg_sales.csv"
MODEL_PATH = BASE_DIR / "model" / "best_gradient_boosting_model.pkl"
FEATURES_PATH = BASE_DIR / "model" / "model_features.pkl"
PERF_PATH = BASE_DIR / "model" / "model_performance.pkl"

st.set_page_config(
    page_title="SmartStock AI - Model Performance",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_global_styles()

st.html(
    """
    <div class="hero">
        <h1>🧠 Model Performance</h1>
        <p>Evaluate the production Gradient Boosting demand model on a chronological holdout set and inspect its most influential features.</p>
    </div>
    """
)


@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        return None
    data = pd.read_csv(DATA_PATH)
    data.columns = data.columns.str.strip()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Units_Sold"] = pd.to_numeric(data["Units_Sold"], errors="coerce")
    return data.dropna(subset=["Date", "Product_Name", "Units_Sold"]).copy()


@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        features = list(joblib.load(FEATURES_PATH))
        saved_metrics = joblib.load(PERF_PATH) if PERF_PATH.exists() else {}
        if not hasattr(model, "predict"):
            raise TypeError("Saved model does not expose predict().")
        expected = getattr(model, "n_features_in_", None)
        if expected is not None and expected != len(features):
            raise ValueError(f"Model expects {expected} features but feature file contains {len(features)}.")
        return model, features, saved_metrics if isinstance(saved_metrics, dict) else {}
    except Exception as exc:
        return None, None, {"_error": str(exc)}


df_raw = load_data()
model, feature_cols, saved_metrics = load_artifacts()

if df_raw is None:
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()
if model is None:
    st.error("The production model or feature artifacts could not be loaded.")
    st.code(saved_metrics.get("_error", "Unknown artifact error."))
    st.stop()

# Match the training pipeline: calendar features, grouped lags, then one-hot
# encoding for Category, Season and Rainfall_Severity with drop_first=True.
df = df_raw.sort_values(["Product_Name", "Date"]).reset_index(drop=True)
df["Day_of_Week"] = df["Date"].dt.dayofweek
df["Day_of_Month"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Quarter"] = df["Date"].dt.quarter

df["Lag_1"] = df.groupby("Product_Name")["Units_Sold"].shift(1)
df["Lag_7"] = df.groupby("Product_Name")["Units_Sold"].shift(7)
df["Rolling_Mean_7"] = df.groupby("Product_Name")["Units_Sold"].transform(
    lambda x: x.shift(1).rolling(7).mean()
)
df["Rolling_Std_7"] = df.groupby("Product_Name")["Units_Sold"].transform(
    lambda x: x.shift(1).rolling(7).std()
)

df = df.dropna().reset_index(drop=True)

categorical = [c for c in ["Category", "Season", "Rainfall_Severity"] if c in df.columns]
encoded = pd.get_dummies(df, columns=categorical, drop_first=True)
drop_cols = ["Date", "Product_Name", "Units_Sold", "Day_of_Week"]
X = encoded.drop(columns=[c for c in drop_cols if c in encoded.columns], errors="ignore")
y = df["Units_Sold"].astype(float)

for feature in feature_cols:
    if feature not in X.columns:
        X[feature] = 0
X = X[feature_cols].astype(float)

if len(X) < 10:
    st.error("Not enough rows remain after lag feature engineering for evaluation.")
    st.stop()

split = int(len(X) * 0.8)
X_test = X.iloc[split:].reset_index(drop=True)
y_test = y.iloc[split:].reset_index(drop=True)
meta = df.iloc[split:].reset_index(drop=True)

try:
    predictions = np.asarray(model.predict(X_test), dtype=float)
except Exception as exc:
    st.error("The production model failed during evaluation.")
    st.code(str(exc))
    st.stop()

predictions = np.maximum(predictions, 0)
mae = float(mean_absolute_error(y_test, predictions))
rmse = float(np.sqrt(mean_squared_error(y_test, predictions)))
r2 = float(r2_score(y_test, predictions))

st.success(f"✅ Production Gradient Boosting model evaluated on the final 20% chronological holdout — {len(feature_cols)} features.")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Calculated MAE", f"{mae:.2f} units")
k2.metric("Calculated RMSE", f"{rmse:.2f} units")
k3.metric("Calculated R²", f"{r2:.4f}")
k4.metric("Test Rows", f"{len(X_test):,}")

if saved_metrics:
    st.caption(
        "Saved notebook metrics are shown for reference only; the values above are recalculated from the current production artifact."
    )
    saved_mae = saved_metrics.get("MAE", saved_metrics.get("mae"))
    saved_rmse = saved_metrics.get("RMSE", saved_metrics.get("rmse"))
    saved_r2 = saved_metrics.get("R2", saved_metrics.get("r2"))
    if any(value is not None for value in [saved_mae, saved_rmse, saved_r2]):
        s1, s2, s3 = st.columns(3)
        s1.metric("Saved MAE", f"{float(saved_mae):.2f}" if saved_mae is not None else "—")
        s2.metric("Saved RMSE", f"{float(saved_rmse):.2f}" if saved_rmse is not None else "—")
        s3.metric("Saved R²", f"{float(saved_r2):.4f}" if saved_r2 is not None else "—")

st.markdown("---")
tab1, tab2, tab3 = st.tabs(["📉 Predictions vs Actuals", "📊 Residuals", "💡 Feature Importance"])

with tab1:
    evaluation = pd.DataFrame({
        "Date": meta["Date"],
        "Product": meta["Product_Name"],
        "Actual": y_test,
        "Predicted": predictions,
    })
    selected = st.selectbox("Product", ["All"] + sorted(evaluation["Product"].unique().tolist()))
    if selected == "All":
        plot_df = evaluation.groupby("Date", as_index=False)[["Actual", "Predicted"]].sum()
    else:
        plot_df = evaluation[evaluation["Product"] == selected]
    fig = px.line(plot_df, x="Date", y=["Actual", "Predicted"], template="plotly_white", title="Actual vs Predicted Demand")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    residuals = y_test.to_numpy() - predictions
    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(x=predictions, y=residuals, labels={"x": "Predicted Units", "y": "Residual"}, title="Residuals vs Predicted", template="plotly_white")
        fig.add_hline(y=0, line_dash="dash")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(residuals, nbins=30, title="Residual Distribution", labels={"value": "Residual"}, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    if hasattr(model, "feature_importances_"):
        importances = np.asarray(model.feature_importances_, dtype=float)
        if len(importances) == len(feature_cols):
            importance_df = pd.DataFrame({"Feature": feature_cols, "Importance": importances}).sort_values("Importance", ascending=False).head(15)
            fig = px.bar(importance_df, x="Importance", y="Feature", orientation="h", title="Top 15 Feature Drivers", template="plotly_white")
            fig.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Feature importance count does not match the saved feature list.")
    else:
        st.info("This model type does not expose feature_importances_.")

st.markdown("---")
st.subheader("📦 Performance by Product")
rows = []
for product, group in meta.groupby("Product_Name"):
    idx = group.index.to_numpy()
    actual = y_test.iloc[idx].to_numpy()
    pred = predictions[idx]
    rows.append({
        "Product": product,
        "Rows": len(idx),
        "MAE": mean_absolute_error(actual, pred),
        "RMSE": np.sqrt(mean_squared_error(actual, pred)),
        "R²": r2_score(actual, pred) if len(idx) >= 2 else np.nan,
    })
product_metrics = pd.DataFrame(rows).sort_values("MAE")
st.dataframe(product_metrics.style.format({"MAE": "{:.2f}", "RMSE": "{:.2f}", "R²": "{:.4f}"}), use_container_width=True, hide_index=True)

report = pd.DataFrame([{
    "Model": type(model).__name__,
    "Features": len(feature_cols),
    "Test Rows": len(X_test),
    "MAE": mae,
    "RMSE": rmse,
    "R2": r2,
}])
st.download_button("📥 Download Evaluation Report", report.to_csv(index=False).encode("utf-8"), "smartstock_model_evaluation.csv", "text/csv", use_container_width=True)
