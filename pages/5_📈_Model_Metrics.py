import joblib
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from styles import apply_global_styles
from utils.i18n import t


# ============================================================
# DYNAMIC PATH SETUP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "smartstock_fmcg_sales.csv"
)

MODEL_PATH = (
    BASE_DIR
    / "model"
    / "best_gradient_boosting_model.pkl"
)

FEATURES_PATH = (
    BASE_DIR
    / "model"
    / "model_features.pkl"
)

PERF_PATH = (
    BASE_DIR
    / "model"
    / "model_performance.pkl"
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartStock AI - Model Performance",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
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

    .performance-header {
        background:
            linear-gradient(
                135deg,
                #0F172A 0%,
                #172554 55%,
                #164E63 100%
            );

        padding: 30px 32px;

        border-radius: 20px;

        margin-bottom: 25px;

        border:
            1px solid
            rgba(129, 140, 248, 0.25);

        box-shadow:
            0 15px 40px
            rgba(0, 0, 0, 0.20);
    }


    .performance-header-title {
        color: #FFFFFF !important;

        font-size: 36px !important;

        font-weight: 800 !important;

        margin-bottom: 8px;
    }


    .performance-header-description {
        color: #CBD5E1 !important;

        font-size: 16px;

        line-height: 1.7;

        max-width: 950px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE HEADER
# ============================================================

st.html(
    f"""
    <div class="performance-header">

        <div class="performance-header-title">
            🧠 {t("model_performance")}
        </div>

        <div class="performance-header-description">
            {t("model_performance_description")}
        </div>

    </div>
    """
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    if not DATA_PATH.exists():

        return None

    try:

        data = pd.read_csv(
            DATA_PATH
        )

        data.columns = (
            data.columns
            .str.strip()
        )

        if "Date" in data.columns:

            data["Date"] = pd.to_datetime(
                data["Date"],
                errors="coerce",
            )

        return (
            data
            .sort_values("Date")
            .reset_index(drop=True)
        )

    except Exception:

        return None


# ============================================================
# MODEL ARTIFACT LOADING
# ============================================================

@st.cache_resource
def load_model_artifacts():

    model = None

    feature_cols = []

    performance = {}


    # --------------------------------------------------------
    # MODEL
    # --------------------------------------------------------

    if MODEL_PATH.exists():

        try:

            model = joblib.load(
                MODEL_PATH
            )

            if not hasattr(
                model,
                "predict",
            ):

                raise TypeError(
                    "Loaded model artifact does not "
                    "provide a predict() method."
                )

        except Exception as error:

            return (
                None,
                [],
                {},
                str(error),
            )

    else:

        return (
            None,
            [],
            {},
            "Production model artifact was not found.",
        )


    # --------------------------------------------------------
    # FEATURE LIST
    # --------------------------------------------------------

    if FEATURES_PATH.exists():

        try:

            feature_cols = joblib.load(
                FEATURES_PATH
            )

            feature_cols = list(
                feature_cols
            )

        except Exception as error:

            return (
                model,
                [],
                {},
                f"Feature artifact could not be loaded: {error}",
            )

    if not feature_cols:

        return (
            model,
            [],
            {},
            "The saved model feature list is empty.",
        )


    # --------------------------------------------------------
    # PERFORMANCE ARTIFACT
    # --------------------------------------------------------

    if PERF_PATH.exists():

        try:

            loaded_performance = joblib.load(
                PERF_PATH
            )

            if isinstance(
                loaded_performance,
                dict,
            ):

                performance.update(
                    loaded_performance
                )

        except Exception:

            pass


    return (
        model,
        feature_cols,
        performance,
        None,
    )


# ============================================================
# LOAD APPLICATION ARTIFACTS
# ============================================================

df_raw = load_data()

(
    model,
    feature_cols,
    saved_performance,
    model_error,
) = load_model_artifacts()


# ============================================================
# DATA VALIDATION
# ============================================================

if df_raw is None:

    st.error(
        t("dataset_not_found")
    )

    st.info(
        f"Expected file: {DATA_PATH}"
    )

    st.stop()


# ============================================================
# MODEL VALIDATION
# ============================================================

if model is None:

    st.error(
        t("model_not_loaded")
    )

    if model_error:

        with st.expander(
            "Model loading details"
        ):

            st.code(
                model_error
            )

    st.stop()


# ============================================================
# FEATURE VALIDATION
# ============================================================

if not feature_cols:

    st.error(
        "Saved model feature definitions could not be loaded."
    )

    st.stop()


# ============================================================
# MODEL STATUS
# ============================================================

actual_feature_count = getattr(
    model,
    "n_features_in_",
    None,
)


if (
    actual_feature_count is not None
    and
    actual_feature_count != len(feature_cols)
):

    st.error(
        "The production model feature count does not "
        "match the saved feature definition."
    )

    st.write(
        f"Model expects: {actual_feature_count}"
    )

    st.write(
        f"Saved feature list contains: "
        f"{len(feature_cols)}"
    )

    st.stop()


st.success(
    f"✅ {t('production_model')} "
    f"{t('online')} — "
    f"{len(feature_cols)} features."
)


# ============================================================
# DATA PREPARATION
# ============================================================

df = df_raw.copy()


required_columns = [
    "Date",
    "Product_Name",
    "Units_Sold",
]


missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


if missing_columns:

    st.error(
        t("missing_required_columns")
    )

    st.code(
        "\n".join(
            missing_columns
        )
    )

    st.stop()


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


# ============================================================
# FEATURE ENGINEERING
# ============================================================

df["Day_of_Week"] = (
    df["Date"].dt.dayofweek
)

df["Day_of_Month"] = (
    df["Date"].dt.day
)

df["Month"] = (
    df["Date"].dt.month
)

df["Quarter"] = (
    df["Date"].dt.quarter
)


# ============================================================
# PRODUCT-SPECIFIC LAG FEATURES
# ============================================================

df = df.sort_values(
    [
        "Product_Name",
        "Date",
    ]
).reset_index(
    drop=True
)


df["Lag_1"] = (
    df.groupby(
        "Product_Name"
    )["Units_Sold"]
    .shift(1)
)


df["Lag_7"] = (
    df.groupby(
        "Product_Name"
    )["Units_Sold"]
    .shift(7)
)


df["Rolling_Mean_7"] = (
    df.groupby(
        "Product_Name"
    )["Units_Sold"]
    .transform(
        lambda x:
        x.shift(1)
        .rolling(7)
        .mean()
    )
)


df["Rolling_Std_7"] = (
    df.groupby(
        "Product_Name"
    )["Units_Sold"]
    .transform(
        lambda x:
        x.shift(1)
        .rolling(7)
        .std()
    )
)


# ============================================================
# REMOVE INCOMPLETE FEATURE ROWS
# ============================================================

df_featured = (
    df
    .dropna(
        subset=[
            "Lag_1",
            "Lag_7",
            "Rolling_Mean_7",
            "Rolling_Std_7",
        ]
    )
    .sort_values("Date")
    .reset_index(drop=True)
)


if df_featured.empty:

    st.error(
        "There are not enough historical records "
        "to construct the model evaluation features."
    )

    st.stop()


# ============================================================
# CATEGORICAL ENCODING
# ============================================================

categorical_columns = [
    column
    for column in [
        "Category",
        "Season",
        "Rainfall_Severity",
    ]
    if column in df_featured.columns
]


df_encoded = pd.get_dummies(
    df_featured,
    columns=categorical_columns,
    drop_first=True,
)


# ============================================================
# BUILD MODEL INPUT MATRIX
# ============================================================

drop_columns = [
    "Date",
    "Product_Name",
    "Units_Sold",
    "Day_of_Week",
]


X = df_encoded.drop(
    columns=[
        column
        for column in drop_columns
        if column in df_encoded.columns
    ],
    errors="ignore",
)


y = df_featured[
    "Units_Sold"
]


# ============================================================
# EXACT FEATURE ALIGNMENT
# ============================================================

for feature in feature_cols:

    if feature not in X.columns:

        X[feature] = 0


X = X[
    feature_cols
]


# ============================================================
# CHRONOLOGICAL TRAIN / TEST SPLIT
# ============================================================

split_index = int(
    len(X) * 0.80
)


if split_index <= 0 or split_index >= len(X):

    st.error(
        "The dataset is too small to create a "
        "chronological evaluation split."
    )

    st.stop()


X_test = (
    X
    .iloc[split_index:]
    .reset_index(drop=True)
)


y_test = (
    y
    .iloc[split_index:]
    .reset_index(drop=True)
)


test_meta = (
    df_featured
    .iloc[split_index:]
    .reset_index(drop=True)
)


# ============================================================
# MODEL PREDICTIONS
# ============================================================

try:

    test_predictions = model.predict(
        X_test
    )

except Exception as error:

    st.error(
        "The production model could not generate "
        "evaluation predictions."
    )

    with st.expander(
        "Prediction error details"
    ):

        st.code(
            str(error)
        )

    st.stop()


test_predictions = np.maximum(
    np.asarray(
        test_predictions,
        dtype=float,
    ),
    0,
)


# ============================================================
# CALCULATED PERFORMANCE METRICS
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


# ============================================================
# OFFICIAL SAVED METRICS
# ============================================================

official_mae = float(
    saved_performance.get(
        "MAE",
        calculated_mae,
    )
)


official_rmse = float(
    saved_performance.get(
        "RMSE",
        calculated_rmse,
    )
)


official_r2 = float(
    saved_performance.get(
        "R2",
        calculated_r2,
    )
)


model_name = saved_performance.get(
    "Model",
    "Gradient Boosting",
)


# ============================================================
# PERFORMANCE OVERVIEW
# ============================================================

st.divider()

st.subheader(
    f"📌 {t('model_performance_overview')}"
)


metric1, metric2, metric3, metric4 = (
    st.columns(4)
)


with metric1:

    st.metric(
        "MAE",
        f"{official_mae:.2f} units",
    )


with metric2:

    st.metric(
        "RMSE",
        f"{official_rmse:.2f} units",
    )


with metric3:

    st.metric(
        "R² Score",
        f"{official_r2:.4f}",
    )


with metric4:

    st.metric(
        t("model_type"),
        model_name,
    )


# ============================================================
# CALCULATED VS SAVED METRICS
# ============================================================

with st.expander(
    "🔎 Calculated Evaluation Metrics"
):

    comparison_df = pd.DataFrame(
        {
            "Metric": [
                "MAE",
                "RMSE",
                "R²",
            ],

            "Saved / Official": [
                official_mae,
                official_rmse,
                official_r2,
            ],

            "Calculated on Current Test Split": [
                calculated_mae,
                calculated_rmse,
                calculated_r2,
            ],
        }
    )

    st.dataframe(
        comparison_df.style.format(
            {
                "Saved / Official": "{:.4f}",
                "Calculated on Current Test Split": "{:.4f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# VISUALIZATION TABS
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        f"📉 {t('predictions_vs_actuals')}",
        f"📊 {t('residual_analysis')}",
        f"💡 {t('feature_importance')}",
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
            "Date":
                test_meta["Date"],

            "Product":
                test_meta["Product_Name"],

            "Actual":
                y_test,

            "Predicted":
                test_predictions,
        }
    )


    product_options = (
        ["All"]
        + sorted(
            eval_df[
                "Product"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )


    selected_product = st.selectbox(
        "Filter by Product",
        product_options,
        key="performance_product_filter",
    )


    if selected_product != "All":

        plot_df = (
            eval_df[
                eval_df["Product"].astype(str)
                == selected_product
            ]
            .sort_values("Date")
        )

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
            .sort_values("Date")
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
            f"Demand Tracking — "
            f"{selected_product}"
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
        y_test
        - test_predictions
    )


    col_res1, col_res2 = st.columns(2)


    with col_res1:

        fig_scatter = px.scatter(
            x=test_predictions,
            y=residuals,
            labels={
                "x":
                    "Predicted Units",

                "y":
                    "Residuals "
                    "(Actual - Predicted)",
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
                "value":
                    "Error Amount"
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


    if hasattr(
        model,
        "feature_importances_",
    ):

        importances = np.asarray(
            model.feature_importances_,
            dtype=float,
        )


        if len(importances) == len(feature_cols):

            feat_imp = (
                pd.DataFrame(
                    {
                        "Feature":
                            feature_cols,

                        "Importance":
                            importances,
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
                    "categoryorder":
                        "total ascending"
                }
            )


            st.plotly_chart(
                fig_imp,
                use_container_width=True,
            )


        else:

            st.warning(
                "The model loaded successfully, but "
                "the number of feature importance values "
                "does not match the saved feature layout."
            )


            st.write(
                f"Model feature importances: "
                f"{len(importances)}"
            )


            st.write(
                f"Saved feature columns: "
                f"{len(feature_cols)}"
            )


    else:

        st.info(
            "Feature importance metrics are not available "
            "for this model type."
        )


# ============================================================
# PERFORMANCE BY PRODUCT
# ============================================================

st.divider()

st.subheader(
    "📦 Performance Breakdown by Product"
)


product_performance = []


# Use positional indices rather than the original DataFrame
# index to avoid indexing errors after reset_index().
for product_name, group in (
    test_meta
    .groupby("Product_Name")
):

    group_positions = (
        group.index.to_numpy()
    )


    if len(group_positions) == 0:

        continue


    actual = (
        y_test
        .iloc[group_positions]
        .to_numpy()
    )


    predicted = (
        test_predictions[
            group_positions
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
            "Product":
                product_name,

            "MAE":
                p_mae,

            "RMSE":
                p_rmse,

            "R²":
                p_r2,

            "Records":
                len(actual),
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
                "MAE":
                    "{:.2f}",

                "RMSE":
                    "{:.2f}",

                "R²":
                    "{:.4f}",

                "Records":
                    "{:,.0f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info(
        "Product-level performance could not be calculated."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.html(
    f"""
    <div class="footer">
        {t("footer")}
    </div>
    """
)