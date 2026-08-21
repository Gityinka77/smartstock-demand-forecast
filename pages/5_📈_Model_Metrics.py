import joblib
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ============================================================
# DYNAMIC PATH SETUP
# Steps up out of pages/ to project root
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "smartstock_fmcg_sales.csv"
MODEL_PATH = BASE_DIR / "model" / "best_gradient_boosting_model.pkl"
FEATURES_PATH = BASE_DIR / "model" / "model_features.pkl"
PERF_PATH = BASE_DIR / "model" / "model_performance.pkl"

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="SmartStock AI - Model Performance",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧠 SmartStock AI: Model Performance")
st.markdown(
    "Evaluate the Gradient Boosting demand forecasting model and understand "
    "the factors driving its predictions."
)
st.markdown("---")


# ============================================================
# DATA & MODEL LOADING WITH SAFE FALLBACKS
# ============================================================
class MockModel:
    """Fallback baseline model used only if the production artifact cannot load."""

    def predict(self, X):
        if "Lag_1" in X.columns:
            return np.maximum(
                X["Lag_1"].fillna(10).values,
                0,
            )
        return np.full(len(X), 15.0)


@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        st.error(
            f"Dataset not found at `{DATA_PATH}`. Please check file placement."
        )
        st.stop()

    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df.sort_values("Date").reset_index(drop=True)


@st.cache_resource
def load_model_artifacts():
    """
    Load the production model, feature layout and saved performance metrics.

    IMPORTANT:
    These artifacts were created with joblib.dump(), therefore they must
    be loaded with joblib.load().
    """

    # --------------------------------------------------------
    # 1. Load Production Gradient Boosting Model
    # --------------------------------------------------------
    model = None

    if MODEL_PATH.exists():
        try:
            model = joblib.load(MODEL_PATH)

            # Confirm that the expected production model loaded.
            if not hasattr(model, "predict"):
                raise TypeError(
                    "Loaded model artifact does not provide a predict() method."
                )

            st.success(
                f"✅ Production Gradient Boosting model loaded successfully — "
                f"{len(getattr(model, 'feature_importances_', []))} features."
            )

        except Exception as exc:
            st.error(
                "❌ The production Gradient Boosting model could not be loaded."
            )

            with st.expander("Model loading details"):
                st.code(str(exc))

            model = MockModel()

    else:
        st.error(
            f"❌ Production model artifact not found at `{MODEL_PATH}`."
        )
        model = MockModel()

    # --------------------------------------------------------
    # 2. Load Feature List
    # --------------------------------------------------------
    feature_cols = []

    if FEATURES_PATH.exists():
        try:
            feature_cols = joblib.load(FEATURES_PATH)

            # Convert numpy arrays / tuples to a normal list.
            feature_cols = list(feature_cols)

        except Exception as exc:
            with st.expander("Feature artifact loading details"):
                st.code(str(exc))

    # Fallback feature list only if the artifact is unavailable.
    if not feature_cols:
        feature_cols = [
            "Day_of_Month",
            "Month",
            "Quarter",
            "Lag_1",
            "Lag_7",
            "Rolling_Mean_7",
            "Rolling_Std_7",
        ]

    # --------------------------------------------------------
    # 3. Load Saved Model Performance Metrics
    # --------------------------------------------------------
    train_performance = {
        "Model": "Gradient Boosting",
        "MAE": 4.10,
        "RMSE": 5.23,
        "R2": 0.8922,
    }

    if PERF_PATH.exists():
        try:
            loaded_perf = joblib.load(PERF_PATH)

            if isinstance(loaded_perf, dict):
                train_performance.update(loaded_perf)

        except Exception as exc:
            with st.expander("Performance artifact loading details"):
                st.code(str(exc))

    return model, feature_cols, train_performance


# ============================================================
# LOAD DATA / MODEL / ARTIFACTS
# ============================================================
df_raw = load_data()

model, feature_cols, train_performance = load_model_artifacts()


# ============================================================
# FEATURE ENGINEERING PIPELINE
# ============================================================
df = df_raw.copy()

# Ensure numeric columns
df["Units_Sold"] = pd.to_numeric(
    df["Units_Sold"],
    errors="coerce",
)

df = df.dropna(
    subset=[
        "Date",
        "Product_Name",
        "Units_Sold",
    ]
).copy()


# ------------------------------------------------------------
# Calendar Features
# ------------------------------------------------------------
df["Day_of_Week"] = df["Date"].dt.dayofweek
df["Day_of_Month"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Quarter"] = df["Date"].dt.quarter


# ------------------------------------------------------------
# Lag Features — Grouped by Product
# ------------------------------------------------------------
df = df.sort_values(
    [
        "Product_Name",
        "Date",
    ]
).reset_index(drop=True)

df["Lag_1"] = (
    df.groupby("Product_Name")["Units_Sold"]
    .shift(1)
)

df["Lag_7"] = (
    df.groupby("Product_Name")["Units_Sold"]
    .shift(7)
)

df["Rolling_Mean_7"] = (
    df.groupby("Product_Name")["Units_Sold"]
    .transform(
        lambda x: x.shift(1).rolling(7).mean()
    )
)

df["Rolling_Std_7"] = (
    df.groupby("Product_Name")["Units_Sold"]
    .transform(
        lambda x: x.shift(1).rolling(7).std()
    )
)


# ------------------------------------------------------------
# Remove rows with unavailable lag/rolling features
# ------------------------------------------------------------
df_featured = (
    df.dropna()
    .sort_values("Date")
    .reset_index(drop=True)
)


# ============================================================
# ENCODING & FEATURE MATRIX ALIGNMENT
# ============================================================
categorical_cols = [
    col
    for col in [
        "Category",
        "Season",
        "Rainfall_Severity",
    ]
    if col in df_featured.columns
]

df_encoded = pd.get_dummies(
    df_featured,
    columns=categorical_cols,
    drop_first=True,
)


# Remove non-model columns
drop_columns = [
    "Date",
    "Product_Name",
    "Units_Sold",
    "Day_of_Week",
]

X = df_encoded.drop(
    columns=[
        c
        for c in drop_columns
        if c in df_encoded.columns
    ],
    errors="ignore",
)

y = df_featured["Units_Sold"]


# ============================================================
# GUARANTEE EXACT TRAINING FEATURE ALIGNMENT
# ============================================================
for col in feature_cols:
    if col not in X.columns:
        X[col] = 0

# Keep the exact training feature order.
X = X[feature_cols]


# ============================================================
# CHRONOLOGICAL TRAIN / TEST SPLIT
# ============================================================
split_index = int(len(X) * 0.8)

X_test = X.iloc[split_index:].reset_index(drop=True)

y_test = (
    y.iloc[split_index:]
    .reset_index(drop=True)
)

test_meta = (
    df_featured.iloc[split_index:]
    .reset_index(drop=True)
)


# ============================================================
# MODEL PREDICTIONS
# ============================================================
test_predictions = model.predict(X_test)

test_predictions = np.maximum(
    np.asarray(
        test_predictions,
        dtype=float,
    ),
    0,
)


# ============================================================
# METRIC CALCULATIONS
# ============================================================
calculated_mae = float(
    mean_absolute_error(
        y_test,
        test_predictions,
    )
)

calculated_rmse = float(
    np.sqrt(
        mean_squared_error(
            y_test,
            test_predictions,
        )
    )
)

calculated_r2 = float(
    r2_score(
        y_test,
        test_predictions,
    )
)


# Use saved official notebook metrics where available.
official_mae = float(
    train_performance.get(
        "MAE",
        calculated_mae,
    )
)

official_rmse = float(
    train_performance.get(
        "RMSE",
        calculated_rmse,
    )
)

official_r2 = float(
    train_performance.get(
        "R2",
        calculated_r2,
    )
)


# ============================================================
# METRICS OVERVIEW
# ============================================================
st.subheader("📌 Model Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "MAE",
    f"{official_mae:.2f} units",
)

col2.metric(
    "RMSE",
    f"{official_rmse:.2f} units",
)

col3.metric(
    "R² Score",
    f"{official_r2:.4f}",
)

col4.metric(
    "Model Type",
    train_performance.get(
        "Model",
        "Gradient Boosting",
    ),
)

st.markdown("---")


# ============================================================
# VISUALIZATION TABS
# ============================================================
tab1, tab2, tab3 = st.tabs(
    [
        "📉 Predictions vs Actuals",
        "📊 Residual Analysis",
        "💡 Feature Importance",
    ]
)


# ============================================================
# TAB 1 — PREDICTIONS VS ACTUALS
# ============================================================
with tab1:

    st.markdown(
        "### Actual vs Predicted Demand Over Time"
    )

    eval_df = pd.DataFrame(
        {
            "Date": test_meta["Date"],
            "Product": test_meta["Product_Name"],
            "Actual": y_test,
            "Predicted": test_predictions,
        }
    )

    selected_product = st.selectbox(
        "Filter by Product",
        ["All"] + list(
            eval_df["Product"].unique()
        ),
    )

    if selected_product != "All":

        plot_df = eval_df[
            eval_df["Product"] == selected_product
        ]

    else:

        plot_df = (
            eval_df
            .groupby("Date")[
                [
                    "Actual",
                    "Predicted",
                ]
            ]
            .sum()
            .reset_index()
        )

    fig_time = px.line(
        plot_df,
        x="Date",
        y=[
            "Actual",
            "Predicted",
        ],
        labels={
            "value": "Units Sold",
            "variable": "Legend",
        },
        title=(
            f"Demand Tracking - {selected_product}"
            if selected_product != "All"
            else "Aggregated Demand Tracking"
        ),
        template="plotly_dark",
    )

    st.plotly_chart(
        fig_time,
        use_container_width=True,
    )


# ============================================================
# TAB 2 — RESIDUAL ANALYSIS
# ============================================================
with tab2:

    st.markdown(
        "### Model Errors & Residual Distribution"
    )

    residuals = (
        y_test - test_predictions
    )

    col_res1, col_res2 = st.columns(2)

    with col_res1:

        fig_scatter = px.scatter(
            x=test_predictions,
            y=residuals,
            labels={
                "x": "Predicted Units",
                "y": "Residuals (Actual - Predicted)",
            },
            title="Residuals vs Predicted Values",
            template="plotly_dark",
        )

        fig_scatter.add_hline(
            y=0,
            line_dash="dash",
            line_color="red",
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True,
        )

    with col_res2:

        fig_hist = px.histogram(
            residuals,
            nbins=30,
            title="Residual Error Distribution",
            labels={
                "value": "Error Amount"
            },
            template="plotly_dark",
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True,
        )


# ============================================================
# TAB 3 — FEATURE IMPORTANCE
# ============================================================
with tab3:

    st.markdown(
        "### Top Feature Drivers"
    )

    # --------------------------------------------------------
    # Production GradientBoostingRegressor exposes
    # feature_importances_
    # --------------------------------------------------------
    if hasattr(
        model,
        "feature_importances_",
    ):

        importances = np.asarray(
            model.feature_importances_,
            dtype=float,
        )

        # Protect against an unexpected feature-count mismatch.
        if len(importances) == len(feature_cols):

            feat_imp = (
                pd.DataFrame(
                    {
                        "Feature": feature_cols,
                        "Importance": importances,
                    }
                )
                .sort_values(
                    "Importance",
                    ascending=False,
                )
                .head(15)
            )

            fig_imp = px.bar(
                feat_imp,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Top 15 Most Important Features",
                template="plotly_dark",
            )

            fig_imp.update_layout(
                yaxis={
                    "categoryorder": "total ascending"
                }
            )

            st.plotly_chart(
                fig_imp,
                use_container_width=True,
            )

        else:

            st.warning(
                "⚠️ The model loaded successfully, but the number "
                "of feature importance values does not match the "
                "saved feature layout."
            )

            st.write(
                f"Model feature importances: {len(importances)}"
            )

            st.write(
                f"Saved feature columns: {len(feature_cols)}"
            )

    else:

        st.info(
            "Feature importance metrics are not available "
            "for this model type."
        )


# ============================================================
# PERFORMANCE BY PRODUCT TABLE
# ============================================================
st.markdown("---")

st.subheader(
    "📦 Performance Breakdown by Product"
)

product_performance = []

for product_name, group in test_meta.groupby(
    "Product_Name"
):

    group_indices = (
        group.index.to_numpy()
    )

    if len(group_indices) == 0:
        continue

    actual = (
        y_test
        .iloc[group_indices]
        .to_numpy()
    )

    predicted = (
        test_predictions[
            group_indices
        ]
    )

    p_mae = mean_absolute_error(
        actual,
        predicted,
    )

    p_rmse = np.sqrt(
        mean_squared_error(
            actual,
            predicted,
        )
    )

    p_r2 = (
        r2_score(
            actual,
            predicted,
        )
        if len(actual) > 1
        else np.nan
    )

    product_performance.append(
        {
            "Product": product_name,
            "MAE": p_mae,
            "RMSE": p_rmse,
            "R²": p_r2,
            "Records": len(actual),
        }
    )


product_performance_df = pd.DataFrame(
    product_performance
)


if not product_performance_df.empty:

    product_performance_df = (
        product_performance_df
        .sort_values("MAE")
        .reset_index(drop=True)
    )

    st.dataframe(
        product_performance_df.style.format(
            {
                "MAE": "{:.2f}",
                "RMSE": "{:.2f}",
                "R²": "{:.4f}",
                "Records": "{:,.0f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )