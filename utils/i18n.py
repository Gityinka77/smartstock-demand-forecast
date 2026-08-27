import streamlit as st


# ============================================================
# SMARTSTOCK MULTILINGUAL TRANSLATIONS
# ============================================================

LANGUAGES = {
    "English": "en",
    "Pidgin": "pidgin",
    "Yorùbá": "yo",
    "Igbo": "ig",
    "Hausa": "ha",
}


# ============================================================
# TRANSLATION DICTIONARY
# ============================================================

TRANSLATIONS = {

    # ========================================================
    # ENGLISH
    # ========================================================

    "en": {

        # ----------------------------------------------------
        # GLOBAL / NAVIGATION
        # ----------------------------------------------------

        "language": "Language",
        "home": "Home",
        "dashboard": "Sales Dashboard",
        "forecast": "Demand Forecast",
        "stock": "Stock & Reorder",
        "model": "Model Performance",
        "about": "About SmartStock",

        "app_tagline":
            "SME Demand Forecasting",

        "sign_in": "Sign In",
        "sign_out": "Sign Out",
        "username": "Username",
        "password": "Password",
        "enter_username": "Enter your username",
        "enter_password": "Enter your password",

        "login": "Login",
        "logout": "Logout",
        "authentication": "Authentication",
        "welcome_back": "Welcome Back",
        "access_application":
            "Sign in to access the SmartStock decision-support application.",
        "invalid_credentials":
            "Invalid username or password.",
        "login_success":
            "Login successful.",
        "protected_application":
            "Protected SmartStock application",

        # ----------------------------------------------------
        # HUMAN VERIFICATION
        # ----------------------------------------------------

        "human_verification":
            "Human Verification",

        "confirm_human":
            "I confirm that I am a human user.",

        "verification_instruction":
            "Please confirm that you are human and complete the verification question below.",

        "verification_question":
            "What is",

        "verification_failed":
            "Please complete the human verification correctly.",

        "verification_required":
            "Human verification is required.",

        # ----------------------------------------------------
        # HOME / HERO
        # ----------------------------------------------------

        "hero_title":
            "SmartStock Demand Forecasting",

        "hero_description": (
            "A machine-learning powered decision-support system designed "
            "to help Nigerian SMEs understand sales demand, forecast future "
            "needs and make smarter stock decisions."
        ),

        "application_navigation":
            "SmartStock Application Navigation",

        "application_navigation_description":
            "Overview of pages and what you can accomplish in each section of the app.",

        "getting_started":
            "Getting Started Workflow",

        "choose_language":
            "Choose your preferred language.",

        # ----------------------------------------------------
        # HOME FUNCTIONAL AREAS
        # ----------------------------------------------------

        "sales_dashboard_title":
            "Sales Dashboard & EDA",

        "sales_dashboard_description":
            "Explore historical sales data across FMCG product categories. View demand trends, seasonality, weekend patterns and exploratory analysis.",

        "demand_forecast_title":
            "Demand Forecast",

        "demand_forecast_description":
            "Generate forward-looking demand predictions using the production machine-learning model.",

        "inventory_advisory_title":
            "Inventory Advisory & Restock",

        "inventory_advisory_description":
            "Translate predicted demand into inventory actions, reorder recommendations and stock-planning decisions.",

        "model_metrics_title":
            "Model Metrics & Pipeline",

        "model_metrics_description":
            "Inspect the machine-learning architecture, evaluation metrics, feature performance and production model results.",

        # ----------------------------------------------------
        # MACHINE LEARNING PIPELINE
        # ----------------------------------------------------

        "ml_pipeline":
            "Machine Learning Pipeline Architecture",

        "ml_pipeline_description":
            "How data moves from raw FMCG sales records to production model inference.",

        "data_ingestion":
            "Data Ingestion",

        "feature_engineering":
            "Feature Engineering",

        "model_training":
            "Model Training",

        "artifact_export":
            "Artifact Export",

        "calendar_lag_features":
            "Calendar & Lag Features",

        "gradient_boosting":
            "Gradient Boosting Regressor",

        "model_artifacts":
            "Model Artifacts",

        "data_ingestion_description":
            "Cleans sales records, standardizes dates and prepares the dataset for analysis.",

        "feature_engineering_description":
            "Creates historical, calendar, promotional, seasonal and environmental features used by the forecasting model.",

        "model_training_description":
            "Trains and evaluates regression models using historical demand data.",

        "artifact_export_description":
            "Stores the trained production model and supporting artifacts for application inference.",

        # ----------------------------------------------------
        # DATASET / KPIs
        # ----------------------------------------------------

        "dataset_summary":
            "Dataset Summary Highlights",

        "total_units":
            "Total Units Sold",

        "average_daily":
            "Average Daily Demand",

        "products":
            "Products",

        "categories":
            "Categories",

        "historical_sales":
            "Historical Sales",

        "records":
            "records",

        "sales_records":
            "Sales Records",

        "total_records":
            "Total Records",

        "date_range":
            "Date Range",

        "first_date":
            "First Date",

        "last_date":
            "Last Date",

        # ----------------------------------------------------
        # DASHBOARD / EDA
        # ----------------------------------------------------

        "dashboard_title":
            "Sales Dashboard",

        "dashboard_description":
            "Explore historical FMCG sales and demand patterns.",

        "filters":
            "Filters",

        "product":
            "Product",

        "category":
            "Category",

        "all_products":
            "All Products",

        "all_categories":
            "All Categories",

        "start_date":
            "Start Date",

        "end_date":
            "End Date",

        "apply_filters":
            "Apply Filters",

        "reset_filters":
            "Reset Filters",

        "sales_over_time":
            "Sales Over Time",

        "demand_trend":
            "Demand Trend",

        "monthly_demand":
            "Monthly Demand",

        "daily_demand":
            "Daily Demand",

        "weekly_demand":
            "Weekly Demand",

        "top_products":
            "Top Products by Demand",

        "demand_category":
            "Demand by Category",

        "category_demand":
            "Category Demand",

        "sales_distribution":
            "Sales Distribution",

        "correlation_matrix":
            "Correlation Matrix",

        "exploratory_analysis":
            "Exploratory Data Analysis",

        "business_insights":
            "Business Insights",

        "highest_product":
            "Highest-Demand Product",

        "leading_category":
            "Leading Category",

        "weekend_effect":
            "Weekend Demand Effect",

        "average_demand":
            "Average Demand",

        "total_demand":
            "Total Demand",

        "maximum_demand":
            "Maximum Demand",

        "minimum_demand":
            "Minimum Demand",

        # ----------------------------------------------------
        # FORECAST
        # ----------------------------------------------------

        "forecast_title":
            "Demand Forecast",

        "forecast_description":
            "Use the production machine-learning model to estimate future product demand.",

        "forecast_settings":
            "Forecast Settings",

        "forecast_horizon":
            "Forecast Horizon",

        "forecast_days":
            "Forecast Days",

        "forecast_period":
            "Forecast Period",

        "generate_forecast":
            "Generate Forecast",

        "forecast_results":
            "Forecast Results",

        "forecast_demand":
            "Forecast Demand",

        "forecast_total":
            "Total Forecast Demand",

        "average_forecast":
            "Average Forecast Demand",

        "forecast_chart":
            "Historical vs Forecast Demand",

        "historical_demand":
            "Historical Demand Trend",

        "future_demand":
            "Future Demand",

        "predicted_demand":
            "Predicted Demand",

        "promotion":
            "Promotion",

        "discount":
            "Discount",

        "discount_percentage":
            "Discount Percentage",

        "rainfall":
            "Rainfall and Weather",

        "rainfall_severity":
            "Rainfall Severity",

        "normal_rainfall":
            "Normal",

        "light_rainfall":
            "Light",

        "moderate_rainfall":
            "Moderate",

        "heavy_rainfall":
            "Heavy",

        "forecast_ready":
            "Forecast ready.",

        "forecast_error":
            "Unable to generate the forecast.",

        # ----------------------------------------------------
        # INVENTORY / STOCK
        # ----------------------------------------------------

        "stock_title":
            "Stock & Reorder",

        "stock_description":
            "Convert demand forecasts into practical inventory and replenishment decisions.",

        "inventory_advisory":
            "Inventory Advisory",

        "current_stock":
            "Current Stock",

        "supplier_lead_time":
            "Supplier Lead Time",

        "lead_time_days":
            "Lead Time (Days)",

        "safety_stock":
            "Safety Stock",

        "safety_stock_days":
            "Safety Stock Coverage",

        "required_stock":
            "Required Stock",

        "lead_time_demand":
            "Lead-Time Demand",

        "reorder_quantity":
            "Recommended Reorder Quantity",

        "reorder_level":
            "Reorder Level",

        "stock_status":
            "Stock Status",

        "stock_sufficient":
            "Stock Sufficient",

        "stock_low":
            "Low Stock",

        "stock_critical":
            "Critical Stock",

        "reorder_recommended":
            "Reorder Recommended",

        "no_reorder_required":
            "No Reorder Required",

        "inventory_summary":
            "Inventory Summary",

        "stock_decision":
            "Stock Decision",

        "recommended_action":
            "Recommended Action",

        "purchase_quantity":
            "Purchase Quantity",

        # ----------------------------------------------------
        # MODEL PERFORMANCE
        # ----------------------------------------------------

        "model_status":
            "Forecasting Model Status",

        "model_performance":
            "Production Model Performance",

        "production_model":
            "Production Model",

        "production_online":
            "Production Model Online",

        "production_unavailable":
            "Production Model Unavailable",

        "official_r2":
            "Official R²",

        "mae":
            "Mean Absolute Error (MAE)",

        "rmse":
            "Root Mean Squared Error (RMSE)",

        "r_squared":
            "Coefficient of Determination (R²)",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Feature Count",

        "feature_importance":
            "Feature Importance",

        "model_evaluation":
            "Model Evaluation",

        "validation_results":
            "Validation Results",

        "residual_analysis":
            "Residual Analysis",

        "model_algorithm":
            "Model Algorithm",

        "gradient_boosting_regressor":
            "Gradient Boosting Regressor",

        # ----------------------------------------------------
        # ABOUT
        # ----------------------------------------------------

        "about_project":
            "Learn More About the Project",

        "read_about":
            "Read More About SmartStock",

        "project_overview":
            "Project Overview",

        "why_smartstock":
            "Why SmartStock?",

        "understand":
            "Understand",

        "decide":
            "Decide",

        "what_smartstock_does":
            "What SmartStock Does",

        "understand_demand":
            "Understand Demand",

        "understand_demand_text": (
            "Analyse past sales to understand what products customers buy "
            "and how demand changes over time."
        ),

        "forecast_future":
            "Forecast Future Sales",

        "forecast_future_text": (
            "Use machine learning to estimate future product demand using "
            "historical, calendar, promotional and seasonal information."
        ),

        "stock_decisions":
            "Make Stock Decisions",

        "stock_decisions_text": (
            "Turn demand forecasts into practical replenishment and "
            "purchasing decisions."
        ),

        "notebook_methodology":
            "Notebook Development Lifecycle & Methodology",

        "data_acquisition_eda":
            "Data Acquisition & Exploratory Analysis",

        "feature_engineering_pipeline":
            "Feature Engineering Pipeline",

        "model_selection_training":
            "Model Selection & Training",

        "evaluation_validation":
            "Evaluation & Validation",

        "deployment_architecture":
            "Serialization & Dashboard Deployment",

        "model_features":
            "Model Features",

        "project_folder_structure":
            "Project Folder Structure",

        "application_pages":
            "Application Pages",

        "nigerian_context":
            "Built for Nigerian SME Inventory Planning",

        "built_for_nigeria":
            "🇳🇬 Built for Nigerian SMEs",

        "payday":
            "Payday periods",

        "promotions":
            "Promotions",

        "discounts":
            "Discounts",

        "weekends":
            "Weekends",

        "festivals":
            "Festive periods",

        "seasonality":
            "Seasonality",

        "about_workflow":
            "From Forecast to Inventory Decision",

        "project_objective":
            "Project Objective",

        # ----------------------------------------------------
        # SYSTEM STATUS
        # ----------------------------------------------------

        "online":
            "Online",

        "not_loaded":
            "Not Loaded",

        "loaded":
            "Loaded",

        "available":
            "Available",

        "unavailable":
            "Unavailable",

        "system_status":
            "System Status",

        "pipeline_status":
            "Pipeline Artifacts Status",

        "data_ready":
            "Data Ready",

        "model_ready":
            "Model Ready",

        # ----------------------------------------------------
        # GENERAL UI
        # ----------------------------------------------------

        "read_more":
            "Read More",

        "show_less":
            "Show Less",

        "next":
            "Next",

        "back":
            "Back",

        "close":
            "Close",

        "save":
            "Save",

        "cancel":
            "Cancel",

        "refresh":
            "Refresh",

        "loading":
            "Loading...",

        "no_data":
            "No data available.",

        "no_results":
            "No results found.",

        "error":
            "Error",

        "warning":
            "Warning",

        "success":
            "Success",

        "information":
            "Information",

        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        "footer":
            "SmartStock SME Demand Forecasting System • "
            "Machine Learning + Inventory Decision Support",
    },


    # ========================================================
    # NIGERIAN PIDGIN
    # ========================================================

    "pidgin": {

        "language": "Language",
        "home": "Home",
        "dashboard": "Sales Dashboard",
        "forecast": "Future Sales",
        "stock": "Stock & Restock",
        "model": "Model Performance",
        "about": "About SmartStock",

        "app_tagline":
            "SME Demand Forecasting",

        "sign_in": "Sign In",
        "sign_out": "Sign Out",
        "username": "Username",
        "password": "Password",
        "enter_username": "Enter your username",
        "enter_password": "Enter your password",
        "login": "Login",
        "logout": "Logout",
        "authentication": "Authentication",
        "welcome_back": "Welcome Back",
        "access_application":
            "Sign in make you fit enter SmartStock decision-support application.",
        "invalid_credentials":
            "Username or password no correct.",
        "login_success":
            "Login don work.",
        "protected_application":
            "SmartStock application wey dey protected",

        "human_verification":
            "Human Verification",
        "confirm_human":
            "I confirm say I be human user.",
        "verification_instruction":
            "Confirm say you be human and answer the question below.",
        "verification_question":
            "Wetin be",
        "verification_failed":
            "Abeg complete the human verification correctly.",
        "verification_required":
            "Human verification dey required.",

        "hero_title":
            "SmartStock Demand Forecasting",

        "hero_description": (
            "SmartStock na machine-learning system wey dey help Nigerian "
            "businesses understand wetin customers dey buy, predict future "
            "sales and make better stock decisions."
        ),

        "application_navigation":
            "SmartStock Application Navigation",

        "application_navigation_description":
            "See wetin you fit do for each part of the app.",

        "getting_started":
            "How to Start",

        "choose_language":
            "Choose the language wey you prefer.",

        "sales_dashboard_title":
            "Sales Dashboard & EDA",

        "sales_dashboard_description":
            "Check past sales across FMCG products and see how demand dey change.",

        "demand_forecast_title":
            "Demand Forecast",

        "demand_forecast_description":
            "Predict future demand using the production machine-learning model.",

        "inventory_advisory_title":
            "Inventory Advisory & Restock",

        "inventory_advisory_description":
            "Use forecast to know when stock low and how much to restock.",

        "model_metrics_title":
            "Model Metrics & Pipeline",

        "model_metrics_description":
            "Check how the machine-learning model perform and the results wey e get.",

        "ml_pipeline":
            "Machine Learning Pipeline",

        "ml_pipeline_description":
            "How sales data dey move from raw data reach the production model.",

        "data_ingestion":
            "Data Collection",

        "feature_engineering":
            "Feature Engineering",

        "model_training":
            "Model Training",

        "artifact_export":
            "Model Export",

        "calendar_lag_features":
            "Calendar & Lag Features",

        "gradient_boosting":
            "Gradient Boosting Regressor",

        "model_artifacts":
            "Model Files",

        "data_ingestion_description":
            "Clean sales data and prepare am for analysis.",

        "feature_engineering_description":
            "Create historical, calendar, promotion, seasonal and weather features.",

        "model_training_description":
            "Train and test regression models using past demand.",

        "artifact_export_description":
            "Save the trained model and supporting files for the app.",

        "dataset_summary":
            "Sales Data Summary",

        "total_units":
            "Total Things We Sell",

        "average_daily":
            "Average Sales Per Day",

        "products":
            "Products",

        "categories":
            "Product Categories",

        "historical_sales":
            "Past Sales",

        "records":
            "records",

        "sales_records":
            "Sales Records",

        "total_records":
            "Total Records",

        "date_range":
            "Date Range",

        "first_date":
            "First Date",

        "last_date":
            "Last Date",

        "dashboard_title":
            "Sales Dashboard",

        "dashboard_description":
            "Check past FMCG sales and demand patterns.",

        "filters":
            "Filters",

        "product":
            "Product",

        "category":
            "Category",

        "all_products":
            "All Products",

        "all_categories":
            "All Categories",

        "start_date":
            "Start Date",

        "end_date":
            "End Date",

        "apply_filters":
            "Apply Filters",

        "reset_filters":
            "Reset Filters",

        "sales_over_time":
            "Sales Over Time",

        "demand_trend":
            "Demand Trend",

        "monthly_demand":
            "Monthly Demand",

        "daily_demand":
            "Daily Demand",

        "weekly_demand":
            "Weekly Demand",

        "top_products":
            "Products We Sell Pass",

        "demand_category":
            "Sales by Product Category",

        "category_demand":
            "Category Sales",

        "sales_distribution":
            "Sales Distribution",

        "correlation_matrix":
            "Correlation Matrix",

        "exploratory_analysis":
            "Exploratory Data Analysis",

        "business_insights":
            "Business Information",

        "highest_product":
            "Product Customers Buy Pass",

        "leading_category":
            "Category We Sell Pass",

        "weekend_effect":
            "Weekend Sales Effect",

        "average_demand":
            "Average Demand",

        "total_demand":
            "Total Demand",

        "maximum_demand":
            "Highest Demand",

        "minimum_demand":
            "Lowest Demand",

        "forecast_title":
            "Demand Forecast",

        "forecast_description":
            "Use the production model to estimate future product demand.",

        "forecast_settings":
            "Forecast Settings",

        "forecast_horizon":
            "Forecast Horizon",

        "forecast_days":
            "Forecast Days",

        "forecast_period":
            "Forecast Period",

        "generate_forecast":
            "Generate Forecast",

        "forecast_results":
            "Forecast Results",

        "forecast_demand":
            "Forecast Demand",

        "forecast_total":
            "Total Forecast Demand",

        "average_forecast":
            "Average Forecast Demand",

        "forecast_chart":
            "Past vs Future Demand",

        "historical_demand":
            "Past Sales Trend",

        "future_demand":
            "Future Demand",

        "predicted_demand":
            "Predicted Demand",

        "promotion":
            "Promo",

        "discount":
            "Discount",

        "discount_percentage":
            "Discount Percentage",

        "rainfall":
            "Rain / Weather",

        "rainfall_severity":
            "Rainfall Level",

        "normal_rainfall":
            "Normal",

        "light_rainfall":
            "Light",

        "moderate_rainfall":
            "Moderate",

        "heavy_rainfall":
            "Heavy",

        "forecast_ready":
            "Forecast don ready.",

        "forecast_error":
            "Forecast no fit run.",

        "stock_title":
            "Stock & Restock",

        "stock_description":
            "Use demand forecast to make better stock and restock decisions.",

        "inventory_advisory":
            "Stock Advice",

        "current_stock":
            "Current Stock",

        "supplier_lead_time":
            "Supplier Lead Time",

        "lead_time_days":
            "Lead Time (Days)",

        "safety_stock":
            "Safety Stock",

        "safety_stock_days":
            "Safety Stock Coverage",

        "required_stock":
            "Stock Required",

        "lead_time_demand":
            "Lead-Time Demand",

        "reorder_quantity":
            "Recommended Restock Quantity",

        "reorder_level":
            "Restock Level",

        "stock_status":
            "Stock Status",

        "stock_sufficient":
            "Stock Enough",

        "stock_low":
            "Stock Low",

        "stock_critical":
            "Stock Critical",

        "reorder_recommended":
            "Restock Recommended",

        "no_reorder_required":
            "No Restock Needed",

        "inventory_summary":
            "Stock Summary",

        "stock_decision":
            "Stock Decision",

        "recommended_action":
            "Recommended Action",

        "purchase_quantity":
            "Quantity to Buy",

        "model_status":
            "Forecasting Model Status",

        "model_performance":
            "How Well the Model Dey Perform",

        "production_model":
            "Forecasting Model",

        "production_online":
            "Forecasting Model Dey Online",

        "production_unavailable":
            "Forecasting Model No Dey Available",

        "official_r2":
            "Model R²",

        "mae":
            "Mean Absolute Error (MAE)",

        "rmse":
            "Root Mean Squared Error (RMSE)",

        "r_squared":
            "Coefficient of Determination (R²)",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Features Used",

        "feature_importance":
            "Feature Importance",

        "model_evaluation":
            "Model Evaluation",

        "validation_results":
            "Validation Results",

        "residual_analysis":
            "Residual Analysis",

        "model_algorithm":
            "Model Algorithm",

        "gradient_boosting_regressor":
            "Gradient Boosting Regressor",

        "about_project":
            "Learn More About SmartStock",

        "read_about":
            "Read About SmartStock",

        "project_overview":
            "Project Overview",

        "why_smartstock":
            "Why SmartStock?",

        "understand":
            "Understand",

        "decide":
            "Decide",

        "what_smartstock_does":
            "Wetin SmartStock Dey Do",

        "understand_demand":
            "Know Wetin Customers Dey Buy",

        "understand_demand_text": (
            "Check past sales to understand which products customers dey "
            "buy and how demand dey change."
        ),

        "forecast_future":
            "Check Wetin Fit Sell",

        "forecast_future_text": (
            "Use machine learning to estimate how much product customers "
            "fit buy for coming days."
        ),

        "stock_decisions":
            "Know When to Restock",

        "stock_decisions_text": (
            "Use the forecast to know when your stock dey low and how much "
            "you fit buy again."
        ),

        "notebook_methodology":
            "Notebook Development Methodology",

        "data_acquisition_eda":
            "Data Acquisition & EDA",

        "feature_engineering_pipeline":
            "Feature Engineering",

        "model_selection_training":
            "Model Selection & Training",

        "evaluation_validation":
            "Evaluation & Validation",

        "deployment_architecture":
            "Deployment Architecture",

        "model_features":
            "Model Features",

        "project_folder_structure":
            "Project Folder Structure",

        "application_pages":
            "Application Pages",

        "nigerian_context":
            "Made for Nigerian SME Stock Planning",

        "built_for_nigeria":
            "🇳🇬 Made for Nigerian Businesses",

        "payday":
            "Salary / Payday",

        "promotions":
            "Promo",

        "discounts":
            "Discount",

        "weekends":
            "Weekend",

        "festivals":
            "Festive Period",

        "seasonality":
            "Season",

        "about_workflow":
            "From Forecast to Stock Decision",

        "project_objective":
            "Project Objective",

        "online":
            "Dey Online",

        "not_loaded":
            "No Load",

        "loaded":
            "Load",

        "available":
            "Available",

        "unavailable":
            "No Dey Available",

        "system_status":
            "System Status",

        "pipeline_status":
            "Pipeline Status",

        "data_ready":
            "Data Ready",

        "model_ready":
            "Model Ready",

        "read_more":
            "Read More",

        "show_less":
            "Show Less",

        "next":
            "Next",

        "back":
            "Back",

        "close":
            "Close",

        "save":
            "Save",

        "cancel":
            "Cancel",

        "refresh":
            "Refresh",

        "loading":
            "Loading...",

        "no_data":
            "No data available.",

        "no_results":
            "No results found.",

        "error":
            "Error",

        "warning":
            "Warning",

        "success":
            "Success",

        "information":
            "Information",

        "footer":
            "SmartStock SME Demand Forecasting • "
            "Machine Learning + Stock Decision Support",
    },


    # ========================================================
    # YORÙBÁ
    # ========================================================

    "yo": {

        "language": "Èdè",
        "home": "Ilé",
        "dashboard": "Àtúpalẹ̀ Títà",
        "forecast": "Àsọtẹ́lẹ̀ Ìbéèrè Ọjà",
        "stock": "Ọjà àti Àtúnra",
        "model": "Ìṣe Àpẹẹrẹ",
        "about": "Nípa SmartStock",

        "app_tagline":
            "Àsọtẹ́lẹ̀ Ìbéèrè fún SME",

        "sign_in": "Wọlé",
        "sign_out": "Jáde",
        "username": "Orúkọ Olùlò",
        "password": "Ọ̀rọ̀ aṣínà",
        "enter_username": "Tẹ orúkọ olùlò rẹ",
        "enter_password": "Tẹ ọ̀rọ̀ aṣínà rẹ",
        "login": "Wọlé",
        "logout": "Jáde",
        "authentication": "Ìdánimọ̀",
        "welcome_back": "Káàbọ̀ Padà",
        "access_application":
            "Wọlé láti lo SmartStock.",
        "invalid_credentials":
            "Orúkọ olùlò tàbí ọ̀rọ̀ aṣínà kò tọ́.",
        "login_success":
            "O ti wọlé dáadáa.",
        "protected_application":
            "Ohun èlò SmartStock tí a dáàbò bò",

        "human_verification":
            "Ìmúdájú Ènìyàn",
        "confirm_human":
            "Mo jẹ́rìí pé ènìyàn ni mí.",
        "verification_instruction":
            "Jọ̀wọ́ jẹ́rìí pé ènìyàn ni ọ́ kí o sì dáhùn ìbéèrè tó wà ní isalẹ.",
        "verification_question":
            "Kí ni",
        "verification_failed":
            "Jọ̀wọ́ parí ìmúdájú ènìyàn dáadáa.",
        "verification_required":
            "A nílò ìmúdájú ènìyàn.",

        "hero_title":
            "SmartStock – Àsọtẹ́lẹ̀ Ìbéèrè Ọjà",

        "hero_description": (
            "SmartStock jẹ́ ètò tí ń lo machine learning láti ran àwọn "
            "ilé-iṣẹ́ kéékèèké àti alábọ̀ọ́de ní Nàìjíríà lọ́wọ́ láti lóye "
            "títà, ṣe àsọtẹ́lẹ̀ ohun tí àwọn oníbàárà lè nílò àti ṣe ìpinnu "
            "tó dára nípa ọjà."
        ),

        "application_navigation":
            "Ìrìnàjò Nínú SmartStock",

        "application_navigation_description":
            "Wo ohun tí o lè ṣe ní apá kọ̀ọ̀kan nínú ohun èlò náà.",

        "getting_started":
            "Bí a Ṣe Lè Bẹ̀rẹ̀",

        "choose_language":
            "Yan èdè tí o fẹ́ràn.",

        "sales_dashboard_title":
            "Àtúpalẹ̀ Títà àti EDA",

        "sales_dashboard_description":
            "Ṣàyẹ̀wò títà FMCG tó ti ṣẹlẹ̀ àti bí ìbéèrè ṣe ń yí padà.",

        "demand_forecast_title":
            "Àsọtẹ́lẹ̀ Ìbéèrè Ọjà",

        "demand_forecast_description":
            "Ṣe àsọtẹ́lẹ̀ ìbéèrè ọjọ́ iwájú pẹ̀lú àpẹẹrẹ machine learning.",

        "inventory_advisory_title":
            "Ìmọ̀ràn Ọjà àti Àtúnra",

        "inventory_advisory_description":
            "Yí àsọtẹ́lẹ̀ padà sí ìpinnu nípa ọjà àti àtúnra.",

        "model_metrics_title":
            "Ìwọn Àpẹẹrẹ àti Pipeline",

        "model_metrics_description":
            "Ṣàyẹ̀wò bí àpẹẹrẹ machine learning ṣe ṣiṣẹ́ àti àwọn àbájáde rẹ̀.",

        "ml_pipeline":
            "Ìlànà Machine Learning",

        "ml_pipeline_description":
            "Bí data títà ṣe ń lọ láti data àkọ́kọ́ sí àpẹẹrẹ ìṣelọpọ.",

        "data_ingestion":
            "Gbigba Data",

        "feature_engineering":
            "Ṣíṣe Àwọn Ẹ̀yà",

        "model_training":
            "Ikẹ́kọ̀ Àpẹẹrẹ",

        "artifact_export":
            "Fífipamọ́ Àpẹẹrẹ",

        "calendar_lag_features":
            "Àwọn Ẹ̀yà Kalẹ́ńdà àti Lag",

        "gradient_boosting":
            "Gradient Boosting Regressor",

        "model_artifacts":
            "Àwọn Fáìlì Àpẹẹrẹ",

        "data_ingestion_description":
            "Mọ́ data títà kí o sì mú un sílẹ̀ fún àtúpalẹ̀.",

        "feature_engineering_description":
            "Ṣẹ̀dá àwọn ẹ̀yà itan, kalẹ́ńdà, ìpolówó, àkókò àti ojú-ọjọ́.",

        "model_training_description":
            "Kọ́ àti dán àwọn àpẹẹrẹ regression wò pẹ̀lú data ìbéèrè.",

        "artifact_export_description":
            "Fipamọ́ àpẹẹrẹ àti àwọn fáìlì tó nílò fún ohun èlò náà.",

        "dataset_summary":
            "Àkótán Data Títà",

        "total_units":
            "Àpapọ̀ Ọjà Tí A Tà",

        "average_daily":
            "Ìwọ̀n Títà Ojoojúmọ́",

        "products":
            "Àwọn Ọjà",

        "categories":
            "Àwọn Ẹ̀ka Ọjà",

        "historical_sales":
            "Títà Tó Ti Ṣẹlẹ̀",

        "records":
            "àkọsílẹ̀",

        "sales_records":
            "Àwọn Àkọsílẹ̀ Títà",

        "total_records":
            "Àpapọ̀ Àkọsílẹ̀",

        "date_range":
            "Àkókò Ọjọ́",

        "first_date":
            "Ọjọ́ Àkọ́kọ́",

        "last_date":
            "Ọjọ́ Ìkẹyìn",

        "dashboard_title":
            "Àtúpalẹ̀ Títà",

        "dashboard_description":
            "Ṣàyẹ̀wò títà FMCG àti àwọn ìyípadà ìbéèrè.",

        "filters":
            "Àwọn Àlẹ̀mọ́",

        "product":
            "Ọjà",

        "category":
            "Ẹ̀ka Ọjà",

        "all_products":
            "Gbogbo Ọjà",

        "all_categories":
            "Gbogbo Ẹ̀ka",

        "start_date":
            "Ọjọ́ Ìbẹ̀rẹ̀",

        "end_date":
            "Ọjọ́ Ìkẹyìn",

        "apply_filters":
            "Lo Àlẹ̀mọ́",

        "reset_filters":
            "Pa Àlẹ̀mọ́ Rẹ̀",

        "sales_over_time":
            "Títà Ní Àkókò",

        "demand_trend":
            "Àṣà Ìbéèrè",

        "monthly_demand":
            "Ìbéèrè Oṣù",

        "daily_demand":
            "Ìbéèrè Ojoojúmọ́",

        "weekly_demand":
            "Ìbéèrè Ọ̀sẹ̀",

        "top_products":
            "Àwọn Ọjà Tí A Tà Jù",

        "demand_category":
            "Ìbéèrè Nípa Ẹ̀ka Ọjà",

        "category_demand":
            "Ìbéèrè Ẹ̀ka Ọjà",

        "sales_distribution":
            "Pínpín Títà",

        "correlation_matrix":
            "Correlation Matrix",

        "exploratory_analysis":
            "Àtúpalẹ̀ Ìwádìí",

        "business_insights":
            "Àlàyé Iṣòwò",

        "highest_product":
            "Ọjà Tí A Tà Jù",

        "leading_category":
            "Ẹ̀ka Ọjà Tó Ga Jù",

        "weekend_effect":
            "Ìyípadà Ìbéèrè Ní Ọ̀sẹ̀ Ìparí",

        "average_demand":
            "Ìwọ̀n Ìbéèrè",

        "total_demand":
            "Àpapọ̀ Ìbéèrè",

        "maximum_demand":
            "Ìbéèrè Tó Ga Jù",

        "minimum_demand":
            "Ìbéèrè Tó Kéré Jù",

        "forecast_title":
            "Àsọtẹ́lẹ̀ Ìbéèrè Ọjà",

        "forecast_description":
            "Lo àpẹẹrẹ ìṣelọpọ láti ṣe àsọtẹ́lẹ̀ ìbéèrè ọjọ́ iwájú.",

        "forecast_settings":
            "Àwọn Eto Àsọtẹ́lẹ̀",

        "forecast_horizon":
            "Àkókò Àsọtẹ́lẹ̀",

        "forecast_days":
            "Ọjọ́ Àsọtẹ́lẹ̀",

        "forecast_period":
            "Àkókò Àsọtẹ́lẹ̀",

        "generate_forecast":
            "Ṣẹ̀dá Àsọtẹ́lẹ̀",

        "forecast_results":
            "Àbájáde Àsọtẹ́lẹ̀",

        "forecast_demand":
            "Ìbéèrè Tí A Ṣe Àsọtẹ́lẹ̀",

        "forecast_total":
            "Àpapọ̀ Ìbéèrè Àsọtẹ́lẹ̀",

        "average_forecast":
            "Ìwọ̀n Ìbéèrè Àsọtẹ́lẹ̀",

        "forecast_chart":
            "Ìbéèrè Tó Ti Ṣẹlẹ̀ àti Tí Ń Bọ̀",

        "historical_demand":
            "Àṣà Ìbéèrè Tó Ti Ṣẹlẹ̀",

        "future_demand":
            "Ìbéèrè Ọjọ́ Iwaju",

        "predicted_demand":
            "Ìbéèrè Tí A Ṣe Àsọtẹ́lẹ̀",

        "promotion":
            "Ìpolówó",

        "discount":
            "Ẹ̀dinwó",

        "discount_percentage":
            "Ìdínkù Nínú Ọgọ́rùn-ún",

        "rainfall":
            "Òjò àti Ojú-ọjọ́",

        "rainfall_severity":
            "Iwọn Òjò",

        "normal_rainfall":
            "Déédé",

        "light_rainfall":
            "Kéré",

        "moderate_rainfall":
            "Àárín",

        "heavy_rainfall":
            "Púpọ̀",

        "forecast_ready":
            "Àsọtẹ́lẹ̀ ti ṣetán.",

        "forecast_error":
            "A kò lè ṣe àsọtẹ́lẹ̀ náà.",

        "stock_title":
            "Ọjà àti Àtúnra",

        "stock_description":
            "Yí àsọtẹ́lẹ̀ ìbéèrè padà sí ìpinnu nípa ọjà àti àtúnra.",

        "inventory_advisory":
            "Ìmọ̀ràn Ọjà",

        "current_stock":
            "Ọjà Tó Wà",

        "supplier_lead_time":
            "Àkókò Olùpèsè",

        "lead_time_days":
            "Ọjọ́ Àkókò Olùpèsè",

        "safety_stock":
            "Ọjà Ààbò",

        "safety_stock_days":
            "Ìbojú Tó Wà Fún Ọjà Ààbò",

        "required_stock":
            "Ọjà Tí A Nílò",

        "lead_time_demand":
            "Ìbéèrè Ní Àkókò Olùpèsè",

        "reorder_quantity":
            "Iye Ọjà Tí A Ṣeduro Kí A Rà",

        "reorder_level":
            "Ipele Àtúnra",

        "stock_status":
            "Ipò Ọjà",

        "stock_sufficient":
            "Ọjà Tó",

        "stock_low":
            "Ọjà Kéré",

        "stock_critical":
            "Ọjà Kéré Gan-an",

        "reorder_recommended":
            "A Ṣeduro Àtúnra",

        "no_reorder_required":
            "A Kò Nílò Àtúnra",

        "inventory_summary":
            "Àkótán Ọjà",

        "stock_decision":
            "Ìpinnu Ọjà",

        "recommended_action":
            "Ìgbésẹ̀ Tí A Ṣeduro",

        "purchase_quantity":
            "Iye Tí A Yẹ Kí A Rà",

        "model_status":
            "Ipò Àpẹẹrẹ Àsọtẹ́lẹ̀",

        "model_performance":
            "Ìṣe Àpẹẹrẹ Ìṣelọpọ",

        "production_model":
            "Àpẹẹrẹ Ìṣelọpọ",

        "production_online":
            "Àpẹẹrẹ Ìṣelọpọ Wà Lórí Ayelujara",

        "production_unavailable":
            "Àpẹẹrẹ Ìṣelọpọ Kò Ṣetán",

        "official_r2":
            "R² Àpẹẹrẹ",

        "mae":
            "Mean Absolute Error (MAE)",

        "rmse":
            "Root Mean Squared Error (RMSE)",

        "r_squared":
            "Coefficient of Determination (R²)",

        "training_records":
            "Àwọn Àkọsílẹ̀ Ikẹ́kọ̀",

        "test_records":
            "Àwọn Àkọsílẹ̀ Ìdánwò",

        "feature_count":
            "Iye Àwọn Ẹ̀yà",

        "feature_importance":
            "Ìjẹ́pàtàkì Ẹ̀yà",

        "model_evaluation":
            "Àyẹ̀wò Àpẹẹrẹ",

        "validation_results":
            "Àbájáde Ìmúdájú",

        "residual_analysis":
            "Àtúpalẹ̀ Àṣìṣe",

        "model_algorithm":
            "Ọ̀nà Àpẹẹrẹ",

        "gradient_boosting_regressor":
            "Gradient Boosting Regressor",

        "about_project":
            "Kọ́ Ẹ̀kọ́ Síi Nípa SmartStock",

        "read_about":
            "Ka Síi Nípa SmartStock",

        "project_overview":
            "Àkótán Iṣẹ́ Yìí",

        "why_smartstock":
            "Kí Ló Dé Tí SmartStock Fi Wúlò?",

        "understand":
            "Lóye",

        "decide":
            "Pinnu",

        "what_smartstock_does":
            "Ohun tí SmartStock Ń Ṣe",

        "understand_demand":
            "Mọ Ìbéèrè Ọjà",

        "understand_demand_text": (
            "Ṣàyẹ̀wò títà tó ti ṣẹlẹ̀ láti mọ àwọn ọjà tí àwọn oníbàárà "
            "ń rà àti bí ìbéèrè ṣe ń yí padà."
        ),

        "forecast_future":
            "Ṣe Àsọtẹ́lẹ̀ Títà Ọjọ́ Iwaju",

        "forecast_future_text": (
            "Lo machine learning láti ṣe àsọtẹ́lẹ̀ iye ọjà tí àwọn "
            "oníbàárà lè nílò ní ọjọ́ iwájú."
        ),

        "stock_decisions":
            "Ṣe Ìpinnu Nípa Ọjà",

        "stock_decisions_text": (
            "Yí àsọtẹ́lẹ̀ ìbéèrè padà sí ìpinnu nípa ìgbà tí ó yẹ kí a "
            "tún ra ọjà àti iye tí a yẹ kí a rà."
        ),

        "notebook_methodology":
            "Ọ̀nà Ìdàgbàsókè Notebook",

        "data_acquisition_eda":
            "Gbigba Data àti Àtúpalẹ̀",

        "feature_engineering_pipeline":
            "Ìlànà Ṣíṣe Àwọn Ẹ̀yà",

        "model_selection_training":
            "Yíyan àti Ikẹ́kọ̀ Àpẹẹrẹ",

        "evaluation_validation":
            "Àyẹ̀wò àti Ìmúdájú",

        "deployment_architecture":
            "Ìṣètò Ìṣàfilọ́lẹ̀",

        "model_features":
            "Àwọn Ẹ̀yà Àpẹẹrẹ",

        "project_folder_structure":
            "Ìṣètò Fọ́dà Iṣẹ́",

        "application_pages":
            "Àwọn Ojú-ìwé Ohun Èlò",

        "nigerian_context":
            "A Ṣe Fún Ìṣètò Ọjà Àwọn SME Nàìjíríà",

        "built_for_nigeria":
            "🇳🇬 A Ṣe Fún Àwọn Iṣòwò Nàìjíríà",

        "payday":
            "Àkókò Ọjọ́ Owo-oṣù",

        "promotions":
            "Ìpolówó",

        "discounts":
            "Ẹ̀dinwó",

        "weekends":
            "Ọ̀sẹ̀ Ìparí",

        "festivals":
            "Àkókò Àjọyọ̀",

        "seasonality":
            "Àkókò Ọdún",

        "about_workflow":
            "Láti Àsọtẹ́lẹ̀ Sí Ìpinnu Ọjà",

        "project_objective":
            "Ète Iṣẹ́ Yìí",

        "online":
            "Ó Wà Lórí Ayelujara",

        "not_loaded":
            "Kò Ṣeé Fífún",

        "loaded":
            "Ti Fífún",

        "available":
            "Ó Wà",

        "unavailable":
            "Kò Wà",

        "system_status":
            "Ipò Ètò",

        "pipeline_status":
            "Ipò Pipeline",

        "data_ready":
            "Data Ti Ṣetán",

        "model_ready":
            "Àpẹẹrẹ Ti Ṣetán",

        "read_more":
            "Ka Síi",

        "show_less":
            "Fi Kéré Hàn",

        "next":
            "Tẹ̀síwájú",

        "back":
            "Padà",

        "close":
            "Pàdé",

        "save":
            "Fipamọ́",

        "cancel":
            "Fagilé",

        "refresh":
            "Tún Ṣe Àtúnṣe",

        "loading":
            "Ń Fífún...",

        "no_data":
            "Kò sí data tó wà.",

        "no_results":
            "Kò sí àbájáde.",

        "error":
            "Àṣìṣe",

        "warning":
            "Ìkìlọ̀",

        "success":
            "Àṣeyọrí",

        "information":
            "Alàyé",

        "footer":
            "SmartStock SME Demand Forecasting • "
            "Machine Learning àti Ìrànlọ́wọ́ Ìpinnu Ọjà",
    },


    # ========================================================
    # IGBO
    # ========================================================

    "ig": {

        "language": "Asụsụ",
        "home": "Ụlọ",
        "dashboard": "Nyocha Ahịa",
        "forecast": "Amụma Ọchịchọ Ngwaahịa",
        "stock": "Ngwaahịa na Ịtụ Ọzọ",
        "model": "Ọrụ Model",
        "about": "Banyere SmartStock",

        "app_tagline":
            "Amụma Ọchịchọ Maka SME",

        "sign_in": "Banye",
        "sign_out": "Pụọ",
        "username": "Aha Onye Ọrụ",
        "password": "Okwuntughe",
        "enter_username": "Tinye aha onye ọrụ gị",
        "enter_password": "Tinye okwuntughe gị",
        "login": "Banye",
        "logout": "Pụọ",
        "authentication": "Nyocha Onye Ọrụ",
        "welcome_back": "Nnọọ Ọzọ",
        "access_application":
            "Banye iji nweta SmartStock.",
        "invalid_credentials":
            "Aha onye ọrụ ma ọ bụ okwuntughe ezighi ezi.",
        "login_success":
            "Ịbanye nke ọma.",
        "protected_application":
            "Ngwa SmartStock echedoro",

        "human_verification":
            "Nyocha Mmadu",
        "confirm_human":
            "A na m akwado na abụ m onye mmadụ.",
        "verification_instruction":
            "Kwenye na ị bụ mmadụ ma zaa ajụjụ dị n'okpuru.",
        "verification_question":
            "Gịnị bụ",
        "verification_failed":
            "Biko mezue nyocha mmadụ nke ọma.",
        "verification_required":
            "A chọrọ nyocha mmadụ.",

        "hero_title":
            "SmartStock – Amụma Ọchịchọ Ngwaahịa",

        "hero_description": (
            "SmartStock bụ usoro na-eji machine learning nyere obere na "
            "etiti azụmahịa na Naịjirịa aka ịghọta ahịa, ịkọ ihe ndị ahịa "
            "ga-achọ n'ọdịnihu na ime mkpebi dị mma banyere ngwaahịa."
        ),

        "application_navigation":
            "Ịgagharị na SmartStock",

        "application_navigation_description":
            "Hụ ihe ị nwere ike ime na ngalaba ọ bụla nke ngwa ahụ.",

        "getting_started":
            "Otu E Si Amal ite",

        "choose_language":
            "Họrọ asụsụ ị chọrọ.",

        "sales_dashboard_title":
            "Nyocha Ahịa & EDA",

        "sales_dashboard_description":
            "Nyochaa ahịa FMCG gara aga na mgbanwe ọchịchọ.",

        "demand_forecast_title":
            "Amụma Ọchịchọ",

        "demand_forecast_description":
            "Mee amụma banyere ọchịchọ ngwaahịa n'ọdịnihu site na machine learning.",

        "inventory_advisory_title":
            "Ndụmọdụ Ngwaahịa na Ịtụ Ọzọ",

        "inventory_advisory_description":
            "Gbanwee amụma ọchịchọ ka ọ bụrụ mkpebi gbasara ngwaahịa na ịtụ ọzọ.",

        "model_metrics_title":
            "Model Metrics & Pipeline",

        "model_metrics_description":
            "Nyochaa otú model machine learning si arụ ọrụ na nsonaazụ ya.",

        "ml_pipeline":
            "Machine Learning Pipeline",

        "ml_pipeline_description":
            "Otu data ahịa si aga site na raw data ruo production model.",

        "data_ingestion":
            "Nchịkọta Data",

        "feature_engineering":
            "Ịrụ Features",

        "model_training":
            "Ịkụzi Model",

        "artifact_export":
            "Mbupụ Model",

        "calendar_lag_features":
            "Calendar & Lag Features",

        "gradient_boosting":
            "Gradient Boosting Regressor",

        "model_artifacts":
            "Faịlụ Model",

        "data_ingestion_description":
            "Hichaa data ahịa ma kwadebe ya maka nyocha.",

        "feature_engineering_description":
            "Mepụta features sitere na akụkọ, kalenda, promotion, oge na ihu igwe.",

        "model_training_description":
            "Kụzie ma nwalee regression models site na demand gara aga.",

        "artifact_export_description":
            "Chekwa model a kụziri na faịlụ ndị ọzọ maka ngwa ahụ.",

        "dataset_summary":
            "Nchịkọta Data Ahịa",

        "total_units":
            "Ngwaahịa A Rere",

        "average_daily":
            "Ọnụ Ahịa Kwa Ụbọchị",

        "products":
            "Ngwaahịa",

        "categories":
            "Ụdị Ngwaahịa",

        "historical_sales":
            "Ahịa Gara Aga",

        "records":
            "records",

        "sales_records":
            "Records Ahịa",

        "total_records":
            "Ngụkọta Records",

        "date_range":
            "Oge Data",

        "first_date":
            "Ụbọchị Mbụ",

        "last_date":
            "Ụbọchị Ikpeazụ",

        "dashboard_title":
            "Nyocha Ahịa",

        "dashboard_description":
            "Nyochaa ahịa FMCG na mgbanwe ọchịchọ.",

        "filters":
            "Filters",

        "product":
            "Ngwaahịa",

        "category":
            "Ụdị Ngwaahịa",

        "all_products":
            "Ngwaahịa Niile",

        "all_categories":
            "Ụdị Niile",

        "start_date":
            "Ụbọchị Mbido",

        "end_date":
            "Ụbọchị Ọgwụgwụ",

        "apply_filters":
            "Tinye Filters",

        "reset_filters":
            "Hichapụ Filters",

        "sales_over_time":
            "Ahịa Ka Oge Na-aga",

        "demand_trend":
            "Ọchịchọ Ka Oge Na-aga",

        "monthly_demand":
            "Ọchịchọ Kwa Ọnwa",

        "daily_demand":
            "Ọchịchọ Kwa Ụbọchị",

        "weekly_demand":
            "Ọchịchọ Kwa Izu",

        "top_products":
            "Ngwaahịa A Na-ere Karịsịa",

        "demand_category":
            "Ọchịchọ Site n'ụdị Ngwaahịa",

        "category_demand":
            "Ọchịchọ Site n'Ụdị",

        "sales_distribution":
            "Nkesa Ahịa",

        "correlation_matrix":
            "Correlation Matrix",

        "exploratory_analysis":
            "Exploratory Data Analysis",

        "business_insights":
            "Ozi Maka Mkpebi Azụmahịa",

        "highest_product":
            "Ngwaahịa A Na-ere Karịsịa",

        "leading_category":
            "Ụdị Ngwaahịa Kasị Elu",

        "weekend_effect":
            "Mmetụta Ahịa N'izu Ọgwụgwụ",

        "average_demand":
            "Ọnụ Ọchịchọ",

        "total_demand":
            "Ngụkọta Ọchịchọ",

        "maximum_demand":
            "Ọchịchọ Kasị Elu",

        "minimum_demand":
            "Ọchịchọ Kasị Ala",

        "forecast_title":
            "Amụma Ọchịchọ",

        "forecast_description":
            "Jiri production model mee amụma banyere ọchịchọ ngwaahịa n'ọdịnihu.",

        "forecast_settings":
            "Ntọala Amụma",

        "forecast_horizon":
            "Oge Amụma",

        "forecast_days":
            "Ụbọchị Amụma",

        "forecast_period":
            "Oge Amụma",

        "generate_forecast":
            "Mepụta Amụma",

        "forecast_results":
            "Nsonaazụ Amụma",

        "forecast_demand":
            "Ọchịchọ A Tụrụ Amụma",

        "forecast_total":
            "Ngụkọta Ọchịchọ A Tụrụ Amụma",

        "average_forecast":
            "Ọnụ Ọchịchọ A Tụrụ Amụma",

        "forecast_chart":
            "Ọchịchọ Gara Aga na Ọdịnihu",

        "historical_demand":
            "Ọchịchọ Gara Aga",

        "future_demand":
            "Ọchịchọ Ọdịnihu",

        "predicted_demand":
            "Ọchịchọ A Tụrụ Amụma",

        "promotion":
            "Promotion",

        "discount":
            "Mbelata Ọnụahịa",

        "discount_percentage":
            "Pasent Mbelata",

        "rainfall":
            "Mmiri Ozuzo na Weather",

        "rainfall_severity":
            "Ọkwa Mmiri Ozuzo",

        "normal_rainfall":
            "Nkịtị",

        "light_rainfall":
            "Obere",

        "moderate_rainfall":
            "Ọkara",

        "heavy_rainfall":
            "Ọtụtụ",

        "forecast_ready":
            "Amụma adịla njikere.",

        "forecast_error":
            "Enweghị ike ime amụma.",

        "stock_title":
            "Ngwaahịa na Ịtụ Ọzọ",

        "stock_description":
            "Jiri amụma ọchịchọ mee mkpebi dị mma banyere ngwaahịa na ịtụ ọzọ.",

        "inventory_advisory":
            "Ndụmọdụ Ngwaahịa",

        "current_stock":
            "Ngwaahịa Dị Ugbu a",

        "supplier_lead_time":
            "Oge Onye Na-ebubata Ngwaahịa",

        "lead_time_days":
            "Ụbọchị Lead Time",

        "safety_stock":
            "Safety Stock",

        "safety_stock_days":
            "Safety Stock Coverage",

        "required_stock":
            "Ngwaahịa Achọrọ",

        "lead_time_demand":
            "Ọchịchọ N'oge Lead Time",

        "reorder_quantity":
            "Ọnụọgụ Ịtụ Ọzọ A Tụrụ Aro",

        "reorder_level":
            "Ọkwa Ịtụ Ọzọ",

        "stock_status":
            "Ọnọdụ Ngwaahịa",

        "stock_sufficient":
            "Ngwaahịa Zuru Oke",

        "stock_low":
            "Ngwaahịa Dị Ala",

        "stock_critical":
            "Ngwaahịa Dị Mkpa",

        "reorder_recommended":
            "A Na-atụ Aro Ịtụ Ọzọ",

        "no_reorder_required":
            "Ịtụ Ọzọ Adịghị Mkpa",

        "inventory_summary":
            "Nchịkọta Ngwaahịa",

        "stock_decision":
            "Mkpebi Ngwaahịa",

        "recommended_action":
            "Omume A Tụrụ Aro",

        "purchase_quantity":
            "Ọnụọgụ A Ga-azụ",

        "model_status":
            "Ọnọdụ Forecasting Model",

        "model_performance":
            "Ọrụ Production Model",

        "production_model":
            "Production Model",

        "production_online":
            "Production Model Dị Online",

        "production_unavailable":
            "Production Model Adịghị",

        "official_r2":
            "R² Model",

        "mae":
            "Mean Absolute Error (MAE)",

        "rmse":
            "Root Mean Squared Error (RMSE)",

        "r_squared":
            "Coefficient of Determination (R²)",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Ọnụọgụ Features",

        "feature_importance":
            "Mkpa Feature",

        "model_evaluation":
            "Nyocha Model",

        "validation_results":
            "Nsonaazụ Validation",

        "residual_analysis":
            "Nyocha Residual",

        "model_algorithm":
            "Algorithm Model",

        "gradient_boosting_regressor":
            "Gradient Boosting Regressor",

        "about_project":
            "Mụtakwuo Banyere SmartStock",

        "read_about":
            "Gụọ Banyere SmartStock",

        "project_overview":
            "Nchịkọta Project",

        "why_smartstock":
            "Gịnị Mere SmartStock Ji Dị Mkpa?",

        "understand":
            "Ghọta",

        "decide":
            "Kpebie",

        "what_smartstock_does":
            "Ihe SmartStock Na-eme",

        "understand_demand":
            "Ghọta Ọchịchọ Ndị Ahịa",

        "understand_demand_text": (
            "Nyochaa ahịa gara aga iji ghọta ngwaahịa ndị ahịa na-azụ "
            "na otu ọchịchọ si agbanwe."
        ),

        "forecast_future":
            "Kwuo Ihe Ndị Ahịa Ga-achọ",

        "forecast_future_text": (
            "Jiri machine learning mee amụma banyere ọnụọgụ ngwaahịa "
            "ndị ahịa nwere ike ịchọ n'ọdịnihu."
        ),

        "stock_decisions":
            "Mee Mkpebi Banyere Ngwaahịa",

        "stock_decisions_text": (
            "Jiri amụma ọchịchọ mara mgbe a ga-atụ ngwaahịa ọzọ na ego "
            "ole kwesịrị ịzụta."
        ),

        "notebook_methodology":
            "Usoro Mmepe Notebook",

        "data_acquisition_eda":
            "Nchịkọta Data na EDA",

        "feature_engineering_pipeline":
            "Feature Engineering Pipeline",

        "model_selection_training":
            "Nhọrọ na Ọzụzụ Model",

        "evaluation_validation":
            "Nyocha na Validation",

        "deployment_architecture":
            "Deployment Architecture",

        "model_features":
            "Features Model",

        "project_folder_structure":
            "Nhazi Fọldà Project",

        "application_pages":
            "Peeji Ngwa",

        "nigerian_context":
            "Emere Maka Atụmatụ Ngwaahịa SME Naịjirịa",

        "built_for_nigeria":
            "🇳🇬 Emere Maka Azụmahịa Naịjirịa",

        "payday":
            "Oge Ụgwọ Ọrụ",

        "promotions":
            "Mgbasa Ozi Ahịa",

        "discounts":
            "Mbelata Ọnụahịa",

        "weekends":
            "Ụbọchị Izu Ọgwụgwụ",

        "festivals":
            "Oge Emume",

        "seasonality":
            "Oge Afọ",

        "about_workflow":
            "Site na Amụma ruo Mkpebi Ngwaahịa",

        "project_objective":
            "Ebumnuche Project",

        "online":
            "Ọ Dị Online",

        "not_loaded":
            "Ọ Dịghị",

        "loaded":
            "Ebuola",

        "available":
            "Ọ Dị",

        "unavailable":
            "Ọ Dịghị",

        "system_status":
            "Ọnọdụ System",

        "pipeline_status":
            "Ọnọdụ Pipeline",

        "data_ready":
            "Data Adịla Njikere",

        "model_ready":
            "Model Adịla Njikere",

        "read_more":
            "Gụọ Ọzọ",

        "show_less":
            "Gosi Obere",

        "next":
            "Gaa n'ihu",

        "back":
            "Laghachi",

        "close":
            "Mechie",

        "save":
            "Chekwaa",

        "cancel":
            "Kagbuo",

        "refresh":
            "Mee Refresh",

        "loading":
            "Na-ebunye...",

        "no_data":
            "Enweghị data dị.",

        "no_results":
            "Enweghị nsonaazụ.",

        "error":
            "Njehie",

        "warning":
            "Ịdọ aka ná ntị",

        "success":
            "Ihe ịga nke ọma",

        "information":
            "Ozi",

        "footer":
            "SmartStock SME Demand Forecasting • "
            "Machine Learning na Mkpebi Banyere Ngwaahịa",
    },


    # ========================================================
    # HAUSA
    # ========================================================

    "ha": {

        "language": "Harshe",
        "home": "Gida",
        "dashboard": "Binciken Tallace-tallace",
        "forecast": "Hasashen Buƙatar Kaya",
        "stock": "Kaya da Sake Cike Kaya",
        "model": "Ayyukan Model",
        "about": "Game da SmartStock",

        "app_tagline":
            "Hasashen Buƙatar Kaya ga SME",

        "sign_in": "Shiga",
        "sign_out": "Fita",
        "username": "Sunan Mai Amfani",
        "password": "Kalmar Sirri",
        "enter_username": "Shigar da sunan mai amfani",
        "enter_password": "Shigar da kalmar sirri",
        "login": "Shiga",
        "logout": "Fita",
        "authentication": "Tabbatar da Mai Amfani",
        "welcome_back": "Barka da Dawowa",
        "access_application":
            "Shiga domin samun damar SmartStock.",
        "invalid_credentials":
            "Sunan mai amfani ko kalmar sirri ba daidai ba ne.",
        "login_success":
            "An shiga cikin nasara.",
        "protected_application":
            "Manhajar SmartStock mai kariya",

        "human_verification":
            "Tabbatar da Mutum",
        "confirm_human":
            "Na tabbatar cewa ni mutum ne.",
        "verification_instruction":
            "Da fatan tabbatar cewa kai mutum ne sannan ka amsa tambayar da ke ƙasa.",
        "verification_question":
            "Nawa ne",
        "verification_failed":
            "Da fatan kammala tabbacin mutum daidai.",
        "verification_required":
            "Ana buƙatar tabbacin mutum.",

        "hero_title":
            "SmartStock – Hasashen Buƙatar Kaya",

        "hero_description": (
            "SmartStock tsarin machine learning ne da aka tsara don "
            "taimaka wa ƙananan da matsakaitan kasuwanci a Najeriya su "
            "fahimci tallace-tallace, su yi hasashen buƙatar gaba kuma "
            "su yanke shawarar kaya mafi kyau."
        ),

        "application_navigation":
            "Kewaya SmartStock",

        "application_navigation_description":
            "Duba abin da za ka iya yi a kowane sashe na manhajar.",

        "getting_started":
            "Yadda Ake Farawa",

        "choose_language":
            "Zaɓi harshen da ka fi so.",

        "sales_dashboard_title":
            "Binciken Tallace-tallace da EDA",

        "sales_dashboard_description":
            "Bincika tallace-tallacen FMCG da suka gabata da canjin buƙata.",

        "demand_forecast_title":
            "Hasashen Buƙatar Kaya",

        "demand_forecast_description":
            "Yi hasashen buƙatar kaya ta gaba ta amfani da production model.",

        "inventory_advisory_title":
            "Shawarar Kaya da Sake Cike Kaya",

        "inventory_advisory_description":
            "Mayar da hasashen buƙata zuwa shawarar kaya da sake cike kaya.",

        "model_metrics_title":
            "Ma'aunin Model da Pipeline",

        "model_metrics_description":
            "Bincika yadda machine-learning model ke aiki da sakamakonsa.",

        "ml_pipeline":
            "Tsarin Machine Learning",

        "ml_pipeline_description":
            "Yadda bayanan tallace-tallace ke tafiya daga raw data zuwa production model.",

        "data_ingestion":
            "Shigar da Bayanai",

        "feature_engineering":
            "Gina Features",

        "model_training":
            "Horar da Model",

        "artifact_export":
            "Fitar da Model",

        "calendar_lag_features":
            "Calendar da Lag Features",

        "gradient_boosting":
            "Gradient Boosting Regressor",

        "model_artifacts":
            "Fayilolin Model",

        "data_ingestion_description":
            "Tsaftace bayanan tallace-tallace kuma shirya su domin bincike.",

        "feature_engineering_description":
            "Ƙirƙiri features na tarihi, kalanda, talla, yanayi da ruwan sama.",

        "model_training_description":
            "Horar da gwada regression models ta amfani da buƙatar da ta gabata.",

        "artifact_export_description":
            "Ajiye trained model da sauran fayilolin da manhajar ke buƙata.",

        "dataset_summary":
            "Taƙaitaccen Bayanai na Tallace-tallace",

        "total_units":
            "Jimillar Kayayyakin da Aka Sayar",

        "average_daily":
            "Matsakaicin Tallace-tallace a Rana",

        "products":
            "Kayayyaki",

        "categories":
            "Rukunin Kayayyaki",

        "historical_sales":
            "Tallace-tallacen Da Suka Gabata",

        "records":
            "records",

        "sales_records":
            "Bayanan Tallace-tallace",

        "total_records":
            "Jimillar Bayanai",

        "date_range":
            "Lokacin Bayanai",

        "first_date":
            "Ranar Farko",

        "last_date":
            "Ranar Ƙarshe",

        "dashboard_title":
            "Binciken Tallace-tallace",

        "dashboard_description":
            "Bincika tallace-tallacen FMCG da canjin buƙata.",

        "filters":
            "Matattara",

        "product":
            "Kaya",

        "category":
            "Rukunin Kaya",

        "all_products":
            "Duk Kayayyaki",

        "all_categories":
            "Duk Rukunai",

        "start_date":
            "Ranar Farawa",

        "end_date":
            "Ranar Ƙarshe",

        "apply_filters":
            "Aiwatar da Matattara",

        "reset_filters":
            "Sake Saita Matattara",

        "sales_over_time":
            "Tallace-tallace a Kan Lokaci",

        "demand_trend":
            "Yanayin Buƙata",

        "monthly_demand":
            "Buƙatar Kowane Wata",

        "daily_demand":
            "Buƙatar Kullum",

        "weekly_demand":
            "Buƙatar Kowane Mako",

        "top_products":
            "Kayayyakin da Aka Fi Sayarwa",

        "demand_category":
            "Buƙata Bisa Rukunin Kaya",

        "category_demand":
            "Buƙatar Rukuni",

        "sales_distribution":
            "Rarraba Tallace-tallace",

        "correlation_matrix":
            "Correlation Matrix",

        "exploratory_analysis":
            "Binciken Bayanai",

        "business_insights":
            "Bayanan Taimakon Yanke Shawarar Kasuwanci",

        "highest_product":
            "Kayan da Aka Fi Sayarwa",

        "leading_category":
            "Rukunin Kaya Mafi Girma",

        "weekend_effect":
            "Tasirin Buƙata a Ƙarshen Mako",

        "average_demand":
            "Matsakaicin Buƙata",

        "total_demand":
            "Jimillar Buƙata",

        "maximum_demand":
            "Mafi Girman Buƙata",

        "minimum_demand":
            "Mafi Ƙarancin Buƙata",

        "forecast_title":
            "Hasashen Buƙatar Kaya",

        "forecast_description":
            "Yi amfani da production model domin hasashen buƙatar kaya ta gaba.",

        "forecast_settings":
            "Saitunan Hasashe",

        "forecast_horizon":
            "Lokacin Hasashe",

        "forecast_days":
            "Kwanakin Hasashe",

        "forecast_period":
            "Lokacin Hasashe",

        "generate_forecast":
            "Ƙirƙiri Hasashe",

        "forecast_results":
            "Sakamakon Hasashe",

        "forecast_demand":
            "Buƙatar da Aka Yi Hasashe",

        "forecast_total":
            "Jimillar Buƙatar Hasashe",

        "average_forecast":
            "Matsakaicin Buƙatar Hasashe",

        "forecast_chart":
            "Buƙatar Da Ta Gabata da Ta Gaba",

        "historical_demand":
            "Yanayin Buƙatar Kaya da Ta Gabata",

        "future_demand":
            "Buƙatar Gaba",

        "predicted_demand":
            "Buƙatar da Aka Yi Hasashe",

        "promotion":
            "Tallan Kasuwanci",

        "discount":
            "Rangwame",

        "discount_percentage":
            "Kashi na Rangwame",

        "rainfall":
            "Ruwan Sama da Yanayi",

        "rainfall_severity":
            "Matsayin Ruwan Sama",

        "normal_rainfall":
            "Al'ada",

        "light_rainfall":
            "Ƙalilan",

        "moderate_rainfall":
            "Matsakaici",

        "heavy_rainfall":
            "Mai Yawa",

        "forecast_ready":
            "Hasashe ya shirya.",

        "forecast_error":
            "Ba a iya yin hasashen ba.",

        "stock_title":
            "Kaya da Sake Cike Kaya",

        "stock_description":
            "Mayar da hasashen buƙata zuwa shawarar kaya da sake cike kaya.",

        "inventory_advisory":
            "Shawarar Kaya",

        "current_stock":
            "Kayan da Ake da Su Yanzu",

        "supplier_lead_time":
            "Lokacin Mai Kaya",

        "lead_time_days":
            "Kwanakin Lokacin Mai Kaya",

        "safety_stock":
            "Kayan Tsaro",

        "safety_stock_days":
            "Ranar Rufe Kayan Tsaro",

        "required_stock":
            "Kayan da Ake Buƙata",

        "lead_time_demand":
            "Buƙata a Lokacin Mai Kaya",

        "reorder_quantity":
            "Adadin Sake Cike Kaya da Aka Shawarta",

        "reorder_level":
            "Matsayin Sake Cike Kaya",

        "stock_status":
            "Matsayin Kaya",

        "stock_sufficient":
            "Kaya Sun Isa",

        "stock_low":
            "Kaya Sun Yi Ƙasa",

        "stock_critical":
            "Kaya Suna Cikin Haɗari",

        "reorder_recommended":
            "Ana Shawartar Sake Cike Kaya",

        "no_reorder_required":
            "Ba a Buƙatar Sake Cike Kaya",

        "inventory_summary":
            "Taƙaitaccen Kaya",

        "stock_decision":
            "Shawarar Kaya",

        "recommended_action":
            "Matakin da Aka Shawarta",

        "purchase_quantity":
            "Adadin da Za a Saya",

        "model_status":
            "Matsayin Forecasting Model",

        "model_performance":
            "Ayyukan Production Model",

        "production_model":
            "Production Model",

        "production_online":
            "Production Model Yana Aiki",

        "production_unavailable":
            "Production Model Baya Samuwa",

        "official_r2":
            "R² na Model",

        "mae":
            "Mean Absolute Error (MAE)",

        "rmse":
            "Root Mean Squared Error (RMSE)",

        "r_squared":
            "Coefficient of Determination (R²)",

        "training_records":
            "Bayanan Horarwa",

        "test_records":
            "Bayanan Gwaji",

        "feature_count":
            "Adadin Features",

        "feature_importance":
            "Muhimmancin Feature",

        "model_evaluation":
            "Binciken Model",

        "validation_results":
            "Sakamakon Validation",

        "residual_analysis":
            "Binciken Residual",

        "model_algorithm":
            "Algorithm na Model",

        "gradient_boosting_regressor":
            "Gradient Boosting Regressor",

        "about_project":
            "Koyi Ƙari Game da SmartStock",

        "read_about":
            "Karanta Game da SmartStock",

        "project_overview":
            "Taƙaitaccen Project",

        "why_smartstock":
            "Me Ya Sa SmartStock?",

        "understand":
            "Fahimta",

        "decide":
            "Yanke Shawara",

        "what_smartstock_does":
            "Abin da SmartStock Ke Yi",

        "understand_demand":
            "Fahimci Buƙatar Kaya",

        "understand_demand_text": (
            "Bincika tallace-tallacen da suka gabata domin fahimtar "
            "kayayyakin da abokan ciniki ke saya da yadda buƙata ke canzawa."
        ),

        "forecast_future":
            "Yi Hasashen Tallace-tallace na Gaba",

        "forecast_future_text": (
            "Yi amfani da machine learning domin hasashen yawan "
            "kayayyakin da abokan ciniki za su iya buƙata."
        ),

        "stock_decisions":
            "Yanke Shawarar Kaya",

        "stock_decisions_text": (
            "Mayar da hasashen buƙata zuwa shawarar lokacin sake cike "
            "kaya da adadin kayan da ya kamata a saya."
        ),

        "notebook_methodology":
            "Tsarin Ci gaban Notebook",

        "data_acquisition_eda":
            "Samun Bayanai da Binciken EDA",

        "feature_engineering_pipeline":
            "Feature Engineering Pipeline",

        "model_selection_training":
            "Zaɓi da Horar da Model",

        "evaluation_validation":
            "Bincike da Tabbatarwa",

        "deployment_architecture":
            "Tsarin Deployment",

        "model_features":
            "Features na Model",

        "project_folder_structure":
            "Tsarin Folders na Project",

        "application_pages":
            "Shafukan Manhaja",

        "nigerian_context":
            "An Gina Shi Don Tsarin Kaya na SME a Najeriya",

        "built_for_nigeria":
            "🇳🇬 An Gina Shi Don Kasuwancin Najeriya",

        "payday":
            "Lokacin Albashi",

        "promotions":
            "Tallan Kasuwanci",

        "discounts":
            "Rangwame",

        "weekends":
            "Ƙarshen Mako",

        "festivals":
            "Lokutan Bukukuwa",

        "seasonality":
            "Yanayin Lokutan Shekara",

        "about_workflow":
            "Daga Hasashe zuwa Shawarar Kaya",

        "project_objective":
            "Manufar Project",

        "online":
            "Yana Aiki",

        "not_loaded":
            "Ba a Loda ba",

        "loaded":
            "An Loda",

        "available":
            "Akwai",

        "unavailable":
            "Babu",

        "system_status":
            "Matsayin System",

        "pipeline_status":
            "Matsayin Pipeline",

        "data_ready":
            "Data Ya Shirya",

        "model_ready":
            "Model Ya Shirya",

        "read_more":
            "Karanta Ƙari",

        "show_less":
            "Nuna Ƙasa",

        "next":
            "Na Gaba",

        "back":
            "Koma Baya",

        "close":
            "Rufe",

        "save":
            "Ajiye",

        "cancel":
            "Soke",

        "refresh":
            "Sabunta",

        "loading":
            "Ana Lodawa...",

        "no_data":
            "Babu bayanan da ake da su.",

        "no_results":
            "Ba a sami sakamako ba.",

        "error":
            "Kuskure",

        "warning":
            "Gargaɗi",

        "success":
            "Nasara",

        "information":
            "Bayani",

        "footer":
            "SmartStock SME Demand Forecasting • "
            "Machine Learning da Taimakon Yanke Shawarar Kaya",
    },
}


# ============================================================
# LANGUAGE STATE
# ============================================================

def get_language():
    """
    Return the currently selected language code.

    English is the default language.
    """

    if "language" not in st.session_state:
        st.session_state["language"] = "en"

    language = st.session_state["language"]

    if language not in TRANSLATIONS:
        st.session_state["language"] = "en"
        language = "en"

    return language


def set_language(language_code):
    """
    Store the selected language code in Streamlit session state.
    """

    if language_code not in TRANSLATIONS:
        language_code = "en"

    st.session_state["language"] = language_code


# ============================================================
# TRANSLATION FUNCTION
# ============================================================

def t(key):
    """
    Translate a key using the active application language.

    Fallback order:

        1. Selected language
        2. English
        3. Raw key
    """

    language = get_language()

    selected_translation = TRANSLATIONS.get(
        language,
        TRANSLATIONS["en"],
    )

    if key in selected_translation:
        return selected_translation[key]

    if key in TRANSLATIONS["en"]:
        return TRANSLATIONS["en"][key]

    return key


# ============================================================
# LANGUAGE DISPLAY HELPERS
# ============================================================

def get_language_name(language_code=None):
    """
    Convert a language code to its display name.
    """

    if language_code is None:
        language_code = get_language()

    for name, code in LANGUAGES.items():

        if code == language_code:
            return name

    return "English"


def get_language_code(language_name):
    """
    Convert a language display name to its language code.
    """

    return LANGUAGES.get(
        language_name,
        "en",
    )


# ============================================================
# GLOBAL SIDEBAR LANGUAGE SELECTOR
# ============================================================

def render_language_selector():
    """
    Render the global language selector.

    app.py should call this before rendering the application
    navigation so that language selection appears above the
    navigation links.
    """

    current_code = get_language()

    current_name = get_language_name(
        current_code
    )

    language_names = list(
        LANGUAGES.keys()
    )

    current_index = (
        language_names.index(current_name)
        if current_name in language_names
        else 0
    )

    selected_name = st.sidebar.selectbox(
        f"🌐 {t('language')}",
        options=language_names,
        index=current_index,
        key="global_language_selector",
    )

    selected_code = get_language_code(
        selected_name
    )

    if selected_code != current_code:

        set_language(
            selected_code
        )

        st.rerun()

    return selected_code