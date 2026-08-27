import os

import streamlit as st

from styles import apply_global_styles, render_sidebar_logo
from utils.i18n import LANGUAGES, get_language, set_language, t


# ============================================================
# SMARTSTOCK AI - PRODUCTION ENTRYPOINT
# Authentication removed so the enhanced application opens
# directly without username/password or human verification.
# ============================================================

st.set_page_config(
    page_title="SmartStock AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_global_styles()


# ============================================================
# PAGE DEFINITIONS
# ============================================================

home_page = st.Page(
    "pages/1_home_page.py",
    title=t("home"),
    icon="🏠",
    default=True,
)

dashboard_page = st.Page(
    "pages/2_📊_Dashboard_EDA.py",
    title=t("dashboard"),
    icon="📊",
)

forecast_page = st.Page(
    "pages/3_🔮_Demand_Forecast.py",
    title=t("forecast"),
    icon="🔮",
)

stock_page = st.Page(
    "pages/4_📦_Inventory_Advisory.py",
    title=t("stock"),
    icon="📦",
)

model_page = st.Page(
    "pages/5_📈_Model_Metrics.py",
    title=t("model"),
    icon="🤖",
)

about_page = st.Page(
    "pages/6_ℹ️_About.py",
    title=t("about"),
    icon="ℹ️",
)


pages = {
    "SmartStock AI": [
        home_page,
        dashboard_page,
        forecast_page,
        stock_page,
        model_page,
        about_page,
    ]
}


# ============================================================
# ENHANCED CUSTOM SIDEBAR
# ============================================================

with st.sidebar:

    # SmartStock logo and branding
    render_sidebar_logo()

    # Language selector
    st.markdown(
        """
        <div
            class="smartstock-sidebar-language-label"
            style="
                font-weight: 700;
                margin-top: 2px;
                margin-bottom: 7px;
            "
        >
            🌐 Language
        </div>
        """,
        unsafe_allow_html=True,
    )

    language_names = list(LANGUAGES.keys())
    current_language = get_language()

    current_language_name = next(
        (
            name
            for name, code in LANGUAGES.items()
            if code == current_language
        ),
        "English",
    )

    selected_language_name = st.selectbox(
        "Language",
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

    st.markdown("---")

    # Enhanced navigation links
    st.page_link(home_page, label=t("home"), icon="🏠")
    st.page_link(dashboard_page, label=t("dashboard"), icon="📊")
    st.page_link(forecast_page, label=t("forecast"), icon="🔮")
    st.page_link(stock_page, label=t("stock"), icon="📦")
    st.page_link(model_page, label=t("model"), icon="🤖")
    st.page_link(about_page, label=t("about"), icon="ℹ️")


# ============================================================
# HIDE STREAMLIT'S AUTOMATIC PAGES MENU
# ============================================================

pg = st.navigation(
    pages,
    position="hidden",
)

pg.run()
