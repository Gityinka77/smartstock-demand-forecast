import streamlit as st

from styles import (
    apply_global_styles,
    render_header_banner,
)

from utils.i18n import t


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About SmartStock",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# GLOBAL STYLES
# ============================================================

apply_global_styles()


# ============================================================
# ABOUT PAGE STYLES
# ============================================================

st.markdown(
    """
    <style>

    .about-detail-card {
        background:
            linear-gradient(
                145deg,
                #111827,
                #0F172A
            );

        border:
            1px solid
            rgba(99, 102, 241, 0.20);

        border-radius: 18px;

        padding: 25px;

        margin-bottom: 20px;
    }

    .about-detail-card h3 {
        color: #FFFFFF !important;
        margin-top: 0;
    }

    .about-detail-card p {
        color: #CBD5E1;
        line-height: 1.75;
    }

    .folder-card {
        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.95),
                rgba(15, 23, 42, 0.98)
            );

        border:
            1px solid
            rgba(34, 211, 238, 0.18);

        border-radius: 16px;

        padding: 20px;

        height: 100%;
    }

    .folder-name {
        color: #67E8F9;
        font-size: 18px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .folder-description {
        color: #CBD5E1;
        line-height: 1.65;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
#
# IMPORTANT:
# app.py owns the SmartStock logo and language selector.
# Do not create another sidebar selector on this page.
# ============================================================

render_header_banner(
    title=f"ℹ️ {t('about')}",
    subtitle=(
        "SmartStock is a machine-learning powered demand "
        "forecasting and inventory decision-support system "
        "designed to help Nigerian SMEs make better purchasing, "
        "replenishment, and stock-planning decisions."
    ),
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.divider()

st.subheader("🎯 Project Overview")

with st.container(border=True):

    st.markdown(
        """
        ### What is SmartStock?

        SmartStock is an SME-focused demand forecasting and
        inventory decision-support application.

        The system analyses historical FMCG sales data,
        identifies demand patterns and uses a trained
        Gradient Boosting machine-learning model to estimate
        future product demand.

        The important distinction is that SmartStock is not
        designed to stop at prediction.

        The forecast is connected to inventory planning so
        that a business can consider current stock, supplier
        lead time and safety-stock requirements before making
        a replenishment decision.

        The application therefore follows a practical
        business chain:

        **Historical Sales → Demand Forecast → Stock Planning
        → Replenishment Decision**
        """
    )


# ============================================================
# WHY SMARTSTOCK
# ============================================================

st.divider()

st.subheader("💡 Why SmartStock?")

purpose1, purpose2, purpose3 = st.columns(3)


with purpose1:

    with st.container(border=True):

        st.subheader("📊 Understand")

        st.write(
            """
            Analyse historical demand across products,
            categories and time periods to understand
            sales behaviour.
            """
        )


with purpose2:

    with st.container(border=True):

        st.subheader("📈 Forecast")

        st.write(
            """
            Estimate future product demand using the
            trained Gradient Boosting machine-learning
            model.
            """
        )


with purpose3:

    with st.container(border=True):

        st.subheader("📦 Decide")

        st.write(
            """
            Convert forecast demand into practical
            inventory and replenishment decisions.
            """
        )


# ============================================================
# READ MORE / SHOW LESS
# ============================================================

st.divider()

st.subheader("📖 Project Information")

st.write(
    """
    SmartStock combines historical FMCG sales, machine
    learning and inventory planning into one decision-
    support application.

    Use **Read More** below to explore the complete project
    explanation, including notebook methodology, folder structure,
    individual application pages, data, model features, model
    performance and business workflow.
    """
)


if "about_read_more" not in st.session_state:

    st.session_state.about_read_more = False


if not st.session_state.about_read_more:

    if st.button(
        "📖 Read More",
        type="primary",
        use_container_width=False,
    ):

        st.session_state.about_read_more = True

        st.rerun()


else:

    # ========================================================
    # TOP COLLAPSE BUTTON
    # ========================================================

    if st.button(
        "⬆️ Show Less",
        type="secondary",
        key="top_show_less",
    ):

        st.session_state.about_read_more = False

        st.rerun()


    # ========================================================
    # NOTEBOOK METHODOLOGY
    # ========================================================

    with st.container(border=True):

        st.subheader(
            "🔬 Notebook Development Lifecycle & Methodology"
        )

        st.write(
            """
            The predictive engine behind SmartStock was developed
            systematically inside `smartstock_ML_Pipeline.ipynb`.
            Below is the complete step-by-step breakdown from raw
            data processing to deployment artifact generation.
            """
        )


        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "1️⃣ Data Acquisition & EDA",
                "2️⃣ Feature Engineering",
                "3️⃣ Model Selection & Training",
                "4️⃣ Evaluation & Validation",
                "5️⃣ Deployment Architecture",
            ]
        )


        # ----------------------------------------------------
        # TAB 1
        # ----------------------------------------------------

        with tab1:

            st.markdown(
                "#### 📊 Step 1: Data Acquisition & Exploratory Analysis"
            )

            st.markdown(
                """
                - **Dataset Ingestion:** Ingested multi-category FMCG transactional logs containing dates, product identifiers, sales quantities, unit prices, category groupings, seasonal tags, and environmental indicators such as rainfall severity.

                - **Data Cleaning & Sanitization:** Handled missing values, stripped string formatting issues, validated date types, and corrected negative or anomalous record entries.

                - **Exploratory Data Analysis (EDA):** Analysed time-series distributions, seasonality spikes, price elasticity trends, and variance across top-performing stock keeping units (SKUs).
                """
            )


        # ----------------------------------------------------
        # TAB 2
        # ----------------------------------------------------

        with tab2:

            st.markdown(
                "#### ⚙️ Step 2: Feature Engineering Pipeline"
            )

            st.markdown(
                """
                To empower supervised regression algorithms to learn temporal patterns, extensive feature transformation was applied:

                - **Calendar Features:** Extracted `Day_of_Week`, `Day_of_Month`, `Month`, and `Quarter` from the date component to capture purchasing behaviour.

                - **Lag Variables:** Generated `Lag_1` and `Lag_7` per product to inform the model of immediate historical demand momentum.

                - **Rolling Window Statistics:** Calculated 7-day moving averages (`Rolling_Mean_7`) and standard deviations (`Rolling_Std_7`) to capture smoothed demand trends and local volatility.

                - **Categorical Encoding:** Converted categorical variables such as `Category`, `Season`, and `Rainfall_Severity` into numerical representations using One-Hot Encoding.
                """
            )


        # ----------------------------------------------------
        # TAB 3
        # ----------------------------------------------------

        with tab3:

            st.markdown(
                "#### 🏋️ Step 3: Model Architecture & Training"
            )

            st.markdown(
                """
                - **Data Splitting Strategy:** Applied a chronological 80/20 train-test split rather than random sampling to prevent temporal data leakage and respect time-series ordering.

                - **Algorithm Selection:** Evaluated standard regression approaches including baseline linear models, decision trees and Gradient Boosting regressors.

                - **Model Optimization:** Selected **Gradient Boosting Regressor (`best_gbr`)** for its ability to capture complex non-linear feature interactions and sequential residual errors.
                """
            )


        # ----------------------------------------------------
        # TAB 4
        # ----------------------------------------------------

        with tab4:

            st.markdown(
                "#### 📈 Step 4: Model Evaluation & Validation"
            )

            st.markdown(
                """
                The finalized model was benchmarked on the unseen test dataset using standard regression metrics:

                - **Mean Absolute Error (MAE - 4.10 units):** Measures the average magnitude of absolute forecasting error in physical inventory units.

                - **Root Mean Squared Error (RMSE - 5.23 units):** Penalizes larger deviations and helps assess forecasting stability during demand spikes.

                - **Coefficient of Determination (R² - 0.8922):** Indicates that approximately 89% of the observed demand variance is explained by the engineered feature set.
                """
            )


        # ----------------------------------------------------
        # TAB 5
        # ----------------------------------------------------

        with tab5:

            st.markdown(
                "#### 🚀 Step 5: Serialization & Dashboard Deployment"
            )

            st.markdown(
                """
                - **Artifact Serialization:** Serialized the optimized model binary (`best_gradient_boosting_model.pkl`), feature layout (`model_features.pkl`) and benchmark metrics (`model_performance.pkl`) for application use.

                - **Streamlit Integration:** Integrated the model artifacts into a modular multi-page Streamlit application supporting feature alignment, real-time inference, scenario planning and interactive Plotly visualizations.
                """
            )


    # ========================================================
    # MACHINE LEARNING APPROACH
    # ========================================================

    with st.container(border=True):

        st.subheader("🧠 Machine Learning Approach")

        st.write(
            """
            SmartStock uses a tuned Gradient Boosting regression
            model for demand forecasting.

            Gradient Boosting is suitable for this type of problem
            because demand can be influenced by multiple interacting
            variables rather than one simple linear relationship.

            The production model learns relationships between
            historical demand and variables representing calendar
            effects, business conditions, seasonality, promotions
            and other demand drivers.

            The application uses the saved production model rather
            than retraining the model every time the Streamlit
            application starts.
            """
        )


    # ========================================================
    # MODEL PERFORMANCE
    # ========================================================

    with st.container(border=True):

        st.subheader("📊 Model Performance")

        metric1, metric2, metric3 = st.columns(3)


        with metric1:

            st.metric(
                "MAE",
                "4.077347",
            )


        with metric2:

            st.metric(
                "RMSE",
                "5.218218",
            )


        with metric3:

            st.metric(
                "R²",
                "0.892632",
            )


        st.caption(
            "Official production metrics recorded during "
            "the notebook model evaluation."
        )


    # ========================================================
    # MODEL FEATURES
    # ========================================================

    with st.container(border=True):

        st.subheader("🧩 Model Features")

        st.write(
            """
            The production forecasting model uses 22 features.
            These features represent historical demand, business
            conditions and calendar or environmental demand drivers.
            """
        )


        feature_col1, feature_col2 = st.columns(2)


        with feature_col1:

            st.markdown(
                """
                **Historical and demand features**

                - Lag 1 demand
                - Lag 7 demand
                - 7-day rolling mean
                - 7-day rolling standard deviation
                - Unit price
                """
            )


        with feature_col2:

            st.markdown(
                """
                **Business and calendar features**

                - Payday period
                - Promotion
                - Discount percentage
                - Weekend
                - Holiday
                - Month
                - Day of month
                - Quarter
                - Season
                - Rainfall severity
                - Product category
                """
            )


    # ========================================================
    # PROJECT FOLDER STRUCTURE
    # ========================================================

    with st.container(border=True):

        st.subheader("📁 Project Folder Structure")

        st.write(
            """
            The SmartStock project is organised into separate
            folders so that data, trained models, utility functions
            and Streamlit pages are kept distinct.
            """
        )


        folder1, folder2 = st.columns(2)


        with folder1:

            st.markdown(
                """
                **`data/`**

                Contains the historical FMCG sales dataset used
                by the application.

                **`smartstock_fmcg_sales.csv`** is the main
                application data source.

                **`model/`**

                Contains the production machine-learning artifacts.

                - `best_gradient_boosting_model.pkl`
                - `model_features.pkl`
                - `model_performance.pkl`
                """
            )


        with folder2:

            st.markdown(
                """
                **`utils/`**

                Contains reusable application functions, including
                data loading, column detection and model artifact loading.

                **`pages/`**

                Contains the individual Streamlit pages that make
                up the application.

                **`styles.py`**

                Contains the shared CSS design system used across
                the application.
                """
            )


    # ========================================================
    # APPLICATION PAGES
    # ========================================================

    with st.container(border=True):

        st.subheader("🧭 Application Pages")

        st.write(
            """
            Each Streamlit page has a specific role in the overall
            decision-support workflow.
            """
        )


        st.markdown(
            """
            ### 🏠 Home

            The Home page introduces SmartStock, shows the overall
            system status and provides a high-level overview of the
            application.

            It is the starting point for the user.

            ---

            ### 📊 Dashboard

            The Dashboard focuses on historical sales analysis.

            Users can filter products, categories and dates and
            examine demand trends, sales distributions and
            relationships between demand drivers.

            The Dashboard answers:

            **"What has happened in the business?"**

            ---

            ### 📈 Demand Forecast

            The Demand Forecast page uses the production Gradient
            Boosting model to estimate future demand for a selected
            product.

            Users can define:

            - Product
            - Forecast horizon
            - Promotion assumption
            - Discount percentage
            - Rainfall assumption

            The page produces daily forecast values and compares
            historical demand with expected future demand.

            This page answers:

            **"What might happen next?"**

            ---

            ### 📦 Stock Recommendation

            The Stock Recommendation page converts forecast demand
            into inventory planning information.

            Users provide:

            - Current stock
            - Forecast horizon
            - Supplier lead time
            - Safety-stock coverage
            - Promotion assumptions
            - Discount assumptions
            - Rainfall assumptions

            The system calculates:

            - Lead-time demand
            - Safety stock
            - Required stock
            - Recommended reorder quantity
            - Stock status

            This page answers:

            **"What should the business do about its stock?"**

            ---

            ### 🧠 Model Performance

            The Model Performance page presents the evaluation
            results of the production model.

            It provides transparency around:

            - MAE
            - RMSE
            - R²
            - Prediction accuracy
            - Residual behaviour
            - Feature importance
            - Product-level performance

            ---

            ### ℹ️ About

            The About page explains the SmartStock project,
            methodology, architecture and Nigerian SME context.
            """
        )


    # ========================================================
    # NIGERIAN SME CONTEXT
    # ========================================================

    with st.container(border=True):

        st.subheader("🇳🇬 Nigerian SME Context")

        st.write(
            """
            SmartStock is designed around the practical challenges
            faced by Nigerian FMCG businesses.

            SMEs often need to balance limited working capital
            against the risk of stockouts and excess inventory.

            Demand can change because of:

            - Payday periods
            - Weekends
            - Promotions
            - Discounts
            - Holidays
            - Seasonal patterns
            - Rainfall conditions

            These factors can affect purchasing and replenishment
            decisions.

            SmartStock therefore provides a structured approach in
            which historical evidence and machine-learning forecasts
            support inventory decisions.
            """
        )


    # ========================================================
    # FORECAST TO INVENTORY
    # ========================================================

    with st.container(border=True):

        st.subheader("📦 From Forecast to Inventory Decision")

        st.write(
            """
            The SmartStock decision-support workflow consists of
            four major stages.
            """
        )


        st.markdown(
            """
            **1. Understand Historical Demand**

            Analyse previous sales to understand what the
            business has experienced.

            **2. Forecast Future Demand**

            Use the trained machine-learning model to estimate
            expected future product demand.

            **3. Plan Inventory**

            Combine expected demand with current stock,
            supplier lead time and safety-stock requirements.

            **4. Take Business Action**

            Use the resulting recommendation to support
            purchasing, replenishment and inventory-management
            decisions.
            """
        )


    # ========================================================
    # PROJECT OBJECTIVE
    # ========================================================

    with st.container(border=True):

        st.subheader("🎯 Project Objective")

        st.write(
            """
            The primary objective of SmartStock is not simply
            to produce an accurate prediction.

            The broader objective is to transform demand information
            into practical business intelligence that can support
            better inventory decisions.

            This makes SmartStock a decision-support system rather
            than simply a machine-learning model.
            """
        )


    # ========================================================
    # BOTTOM COLLAPSE BUTTON
    # ========================================================

    if st.button(
        "⬆️ Show Less",
        type="secondary",
        key="bottom_show_less",
    ):

        st.session_state.about_read_more = False

        st.rerun()


# ============================================================
# PAGE FOOTER
# ============================================================

st.divider()

footer_col1, footer_col2 = st.columns(
    [1, 1]
)


with footer_col1:

    st.markdown(
        "**👨‍💻 Developed by:** "
        "**Adekunle Olayinka Grace**"
    )

    st.markdown(
        "SmartStock AI © 2026 | All Rights Reserved"
    )


with footer_col2:

    st.markdown(
        "**⚙️ Tech Stack & Libraries:**"
    )

    st.markdown(
        "`Jupyter Notebook` | "
        "`Pandas` | "
        "`NumPy` | "
        "`Scikit-Learn` | "
        "`Machine Learning` | "
        "`Streamlit`"
    )