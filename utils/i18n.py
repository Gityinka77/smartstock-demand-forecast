import streamlit as st


# ============================================================
# SMARTSTOCK MULTILINGUAL TRANSLATIONS
# ============================================================

LANGUAGES = {
    "English": "en",
    "Nigerian Pidgin": "pidgin",
    "Yorùbá": "yo",
    "Igbo": "ig",
    "Hausa": "ha",
}


TRANSLATIONS = {

    # ========================================================
    # ENGLISH
    # ========================================================

    "en": {

        "language": "Language",
        "home": "Home",
        "dashboard": "Sales Dashboard",
        "forecast": "Demand Forecast",
        "stock": "Stock & Reorder",
        "model": "Model Performance",
        "about": "About SmartStock",

        "app_tagline": "SME Demand Forecasting",

        "hero_title":
            "SmartStock Demand Forecasting",

        "hero_description": (
            "A machine-learning powered decision-support system designed "
            "to help Nigerian SMEs understand sales demand, forecast future "
            "needs and make smarter stock decisions."
        ),

        "total_units": "Total Units Sold",
        "average_daily": "Average Daily Demand",
        "products": "Products",
        "categories": "Categories",

        "historical_sales": "Historical Sales",

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

        "historical_demand":
            "Historical Demand Trend",

        "top_products":
            "Top Products by Demand",

        "demand_category":
            "Demand by Category",

        "business_insights":
            "Business Insights",

        "highest_product":
            "Highest-Demand Product",

        "leading_category":
            "Leading Category",

        "weekend_effect":
            "Weekend Demand Effect",

        "model_status":
            "Forecasting Model Status",

        "production_online":
            "Production Model Online",

        "production_unavailable":
            "Production Model Unavailable",

        "production_model":
            "Production Model",

        "official_r2":
            "Official R²",

        "model_performance":
            "Production Model Performance",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Feature Count",

        "nigerian_context":
            "Built for Nigerian SME Inventory Planning",

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

        "rainfall":
            "Rainfall and weather",

        "about_project":
            "Learn More About the Project",

        "read_about":
            "Read More About SmartStock",

        "online":
            "Online",

        "not_loaded":
            "Not Loaded",

        "dataset":
            "Dataset",

        "records":
            "records",

        "built_for_nigeria":
            "🇳🇬 Built for Nigerian SMEs",

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

        "hero_title":
            "SmartStock Demand Forecasting",

        "hero_description": (
            "SmartStock na machine-learning system wey dey help Nigerian "
            "businesses understand wetin customers dey buy, predict future "
            "sales and make better stock decisions."
        ),

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

        "historical_demand":
            "Past Sales Trend",

        "top_products":
            "Products We Sell Pass",

        "demand_category":
            "Sales by Product Category",

        "business_insights":
            "Business Information",

        "highest_product":
            "Product Customers Buy Pass",

        "leading_category":
            "Category We Sell Pass",

        "weekend_effect":
            "Weekend Sales Effect",

        "model_status":
            "Forecasting Model Status",

        "production_online":
            "Forecasting Model Dey Online",

        "production_unavailable":
            "Forecasting Model No Dey Available",

        "production_model":
            "Forecasting Model",

        "official_r2":
            "Model R²",

        "model_performance":
            "How Well the Model Dey Perform",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Features Used",

        "nigerian_context":
            "Made for Nigerian SME Stock Planning",

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

        "rainfall":
            "Rain / Weather",

        "about_project":
            "Learn More About SmartStock",

        "read_about":
            "Read About SmartStock",

        "online":
            "Dey Online",

        "not_loaded":
            "No Load",

        "dataset":
            "Sales Data",

        "records":
            "records",

        "built_for_nigeria":
            "🇳🇬 Made for Nigerian Businesses",

        "footer":
            "SmartStock SME Demand Forecasting • "
            "Machine Learning + Stock Decision Support",
    },


    # ========================================================
    # YORUBA
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

        "hero_title":
            "SmartStock – Àsọtẹ́lẹ̀ Ìbéèrè Ọjà",

        "hero_description": (
            "SmartStock jẹ́ ètò tí ń lo machine learning láti ran àwọn "
            "ilé-iṣẹ́ kéékèèké àti alábọ̀ọ́de ní Nàìjíríà lọ́wọ́ láti lóye "
            "títà, ṣe àsọtẹ́lẹ̀ ohun tí àwọn oníbàárà lè nílò àti ṣe ìpinnu "
            "tó dára nípa ọjà."
        ),

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

        "historical_demand":
            "Àṣà Ìbéèrè Ọjà Tó Ti Ṣẹlẹ̀",

        "top_products":
            "Àwọn Ọjà Tí A Tà Jù",

        "demand_category":
            "Títà Nípa Ẹ̀ka Ọjà",

        "business_insights":
            "Àlàyé fún Ìpinnu Iṣòwò",

        "highest_product":
            "Ọjà Tí A Tà Jù",

        "leading_category":
            "Ẹ̀ka Ọjà Tó Ga Jù",

        "weekend_effect":
            "Ìyípadà Ìbéèrè Ní Ọ̀sẹ̀ Ìparí",

        "model_status":
            "Ipò Àpẹẹrẹ Àsọtẹ́lẹ̀",

        "production_online":
            "Àpẹẹrẹ Ìṣelọpọ Wà Lórí Ayelujara",

        "production_unavailable":
            "Àpẹẹrẹ Ìṣelọpọ Kò Ṣetán",

        "production_model":
            "Àpẹẹrẹ Ìṣelọpọ",

        "official_r2":
            "R² Àpẹẹrẹ",

        "model_performance":
            "Ìṣe Àpẹẹrẹ Ìṣelọpọ",

        "training_records":
            "Àwọn Àkọsílẹ̀ Ikẹ́kọ̀",

        "test_records":
            "Àwọn Àkọsílẹ̀ Ìdánwò",

        "feature_count":
            "Iye Àwọn Ẹ̀yà",

        "nigerian_context":
            "A Ṣe Fún Ìṣètò Ọjà Àwọn SME Nàìjíríà",

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

        "rainfall":
            "Òjò àti Ojú-ọjọ́",

        "about_project":
            "Kọ́ Ẹ̀kọ́ Síi Nípa SmartStock",

        "read_about":
            "Ka Síi Nípa SmartStock",

        "online":
            "Ó Wà Lórí Ayelujara",

        "not_loaded":
            "Kò Ṣeé Fífún",

        "dataset":
            "Àkójọpọ̀ Àwọn Àkọsílẹ̀",

        "records":
            "àkọsílẹ̀",

        "built_for_nigeria":
            "🇳🇬 A Ṣe Fún Àwọn Iṣòwò Nàìjíríà",

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

        "hero_title":
            "SmartStock – Amụma Ọchịchọ Ngwaahịa",

        "hero_description": (
            "SmartStock bụ usoro na-eji machine learning nyere obere na "
            "etiti azụmahịa na Naịjirịa aka ịghọta ahịa, ịkọ ihe ndị ahịa "
            "ga-achọ n'ọdịnihu na ime mkpebi dị mma banyere ngwaahịa."
        ),

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

        "historical_demand":
            "Ọchịchọ Ngwaahịa Gara Aga",

        "top_products":
            "Ngwaahịa A Na-ere Karịsịa",

        "demand_category":
            "Ahịa Site n'ụdị Ngwaahịa",

        "business_insights":
            "Ozi Maka Mkpebi Azụmahịa",

        "highest_product":
            "Ngwaahịa A Na-ere Karịsịa",

        "leading_category":
            "Ụdị Ngwaahịa Kasị Elu",

        "weekend_effect":
            "Mmetụta Ahịa N'izu Ọgwụgwụ",

        "model_status":
            "Ọnọdụ Forecasting Model",

        "production_online":
            "Production Model Dị Online",

        "production_unavailable":
            "Production Model Adịghị",

        "production_model":
            "Production Model",

        "official_r2":
            "R² Model",

        "model_performance":
            "Ọrụ Production Model",

        "training_records":
            "Training Records",

        "test_records":
            "Test Records",

        "feature_count":
            "Ọnụọgụ Features",

        "nigerian_context":
            "Emere Maka Atụmatụ Ngwaahịa SME Naịjirịa",

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

        "rainfall":
            "Mmiri Ozuzo na Weather",

        "about_project":
            "Mụtakwuo Banyere SmartStock",

        "read_about":
            "Gụọ Banyere SmartStock",

        "online":
            "Ọ Dị Online",

        "not_loaded":
            "Ọ Dịghị",

        "dataset":
            "Data Ahịa",

        "records":
            "records",

        "built_for_nigeria":
            "🇳🇬 Emere Maka Azụmahịa Naịjirịa",

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

        "hero_title":
            "SmartStock – Hasashen Buƙatar Kaya",

        "hero_description": (
            "SmartStock tsarin machine learning ne da aka tsara don "
            "taimaka wa ƙananan da matsakaitan kasuwanci a Najeriya su "
            "fahimci tallace-tallace, su yi hasashen buƙatar gaba kuma "
            "su yanke shawarar kaya mafi kyau."
        ),

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

        "historical_demand":
            "Yanayin Buƙatar Kaya da Ta Gabata",

        "top_products":
            "Kayayyakin da Aka Fi Sayarwa",

        "demand_category":
            "Tallace-tallace Bisa Rukunin Kaya",

        "business_insights":
            "Bayanan Taimakon Yanke Shawarar Kasuwanci",

        "highest_product":
            "Kayan da Aka Fi Sayarwa",

        "leading_category":
            "Rukunin Kaya Mafi Girma",

        "weekend_effect":
            "Tasirin Buƙata a Ƙarshen Mako",

        "model_status":
            "Matsayin Forecasting Model",

        "production_online":
            "Production Model Yana Aiki",

        "production_unavailable":
            "Production Model Baya Samuwa",

        "production_model":
            "Production Model",

        "official_r2":
            "R² na Model",

        "model_performance":
            "Ayyukan Production Model",

        "training_records":
            "Bayanan Horarwa",

        "test_records":
            "Bayanan Gwaji",

        "feature_count":
            "Adadin Features",

        "nigerian_context":
            "An Gina Shi Don Tsarin Kaya na SME a Najeriya",

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

        "rainfall":
            "Ruwan Sama da Yanayi",

        "about_project":
            "Koyi Ƙari Game da SmartStock",

        "read_about":
            "Karanta Game da SmartStock",

        "online":
            "Yana Aiki",

        "not_loaded":
            "Ba a Loda ba",

        "dataset":
            "Bayanan Tallace-tallace",

        "records":
            "records",

        "built_for_nigeria":
            "🇳🇬 An Gina Shi Don Kasuwancin Najeriya",

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
        selected language
        English
        raw key
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
    Render the GLOBAL language selector.

    IMPORTANT:
    This function should be called by app.py BEFORE the
    Streamlit page navigation is rendered.

    The selector therefore becomes the first interactive
    application control in the sidebar.
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