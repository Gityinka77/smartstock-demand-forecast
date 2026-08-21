import streamlit as st
from styles import apply_global_styles
from utils.i18n import (
    LANGUAGES,
    get_language,
    set_language,
    t,
)

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="SmartStock AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# GLOBAL STYLES & LANGUAGE INITIALIZATION
# ============================================================
apply_global_styles()
current_language = get_language()

# ============================================================
# SIDEBAR BRANDING & LANGUAGE SELECTOR
# ============================================================
with st.sidebar:
    st.markdown(
        """
        <div class="smartstock-brand" style="text-align: center; padding: 10px 0;">
            <div class="smartstock-logo" style="font-size: 2.5rem;">📈</div>
            <div class="smartstock-name" style="font-size: 1.5rem; font-weight: bold; color: #10B981;">SmartStock</div>
            <div class="smartstock-tagline" style="font-size: 0.85rem; color: #94A3B8;">
                SME Demand Forecasting
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(f"**🌍 {t('language')}**")

    language_names = list(LANGUAGES.keys())
    current_language_name = next(
        (name for name, code in LANGUAGES.items() if code == current_language),
        "English",
    )

    selected_language_name = st.selectbox(
        label=t("language"),
        options=language_names,
        index=(
            language_names.index(current_language_name)
            if current_language_name in language_names
            else 0
        ),
        key="app_language_selector",
        label_visibility="collapsed",
    )

    selected_language = LANGUAGES[selected_language_name]

    if selected_language != current_language:
        set_language(selected_language)
        st.rerun()

# ============================================================
# MULTILINGUAL NAVIGATION (MATCHING YOUR EXACT VS CODE FILENAMES)
# ============================================================
pages = {
    "SmartStock AI": [
        st.Page(
            "pages/1_home_page.py",
            title=t("home"),
            icon="🏠",
            default=True,
        ),
        st.Page(
            "pages/2_📊_Dashboard_EDA.py",
            title=t("dashboard"),
            icon="📊",
        ),
        st.Page(
            "pages/3_🔮_Demand_Forecast.py",
            title=t("forecast"),
            icon="🔮",
        ),
        st.Page(
            "pages/4_📦_Inventory_Advisory.py",
            title=t("stock"),
            icon="📦",
        ),
        st.Page(
            "pages/5_📈_Model_Metrics.py",
            title=t("model"),
            icon="🤖",
        ),
        st.Page(
            "pages/6_ℹ️_About.py",
            title=t("about"),
            icon="ℹ️",
        ),
    ]
}

# ============================================================
# RUN APPLICATION
# ============================================================
pg = st.navigation(pages, position="sidebar")
pg.run()