import base64
import hmac
import os
import random

import streamlit as st

from styles import (
    apply_global_styles,
    render_sidebar_logo,
)

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
# GLOBAL STYLES
# ============================================================

apply_global_styles()


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ============================================================
# SMARTSTOCK LOGIN LOGO
# ============================================================

LOGIN_LOGO_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "smartstock_logo.png",
)


def load_login_logo():
    """
    Load the SmartStock logo for the authentication screen.
    """

    if not os.path.exists(
        LOGIN_LOGO_PATH
    ):
        return None

    try:

        with open(
            LOGIN_LOGO_PATH,
            "rb",
        ) as image_file:

            encoded = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        return (
            "data:image/png;base64,"
            + encoded
        )

    except Exception:

        return None


# ============================================================
# AUTHENTICATION CREDENTIALS
# ============================================================

def get_auth_credentials():
    """
    Load SmartStock credentials.

    Priority:
    1. Environment variables
    2. Streamlit secrets
    """

    username = os.getenv(
        "SMARTSTOCK_USERNAME",
        "",
    )

    password = os.getenv(
        "SMARTSTOCK_PASSWORD",
        "",
    )

    try:

        if not username:

            username = st.secrets.get(
                "SMARTSTOCK_USERNAME",
                "",
            )

        if not password:

            password = st.secrets.get(
                "SMARTSTOCK_PASSWORD",
                "",
            )

    except Exception:

        pass

    return (
        str(username).strip(),
        str(password),
    )


AUTH_USERNAME, AUTH_PASSWORD = (
    get_auth_credentials()
)


# ============================================================
# SESSION STATE
# ============================================================

if "authenticated" not in st.session_state:

    st.session_state.authenticated = False


if "human_verified" not in st.session_state:

    st.session_state.human_verified = False


if "captcha_num1" not in st.session_state:

    st.session_state.captcha_num1 = random.randint(
        2,
        9,
    )


if "captcha_num2" not in st.session_state:

    st.session_state.captcha_num2 = random.randint(
        1,
        9,
    )


# ============================================================
# CAPTCHA RESET
# ============================================================

def reset_human_challenge():

    st.session_state.captcha_num1 = random.randint(
        2,
        9,
    )

    st.session_state.captcha_num2 = random.randint(
        1,
        9,
    )

    st.session_state.human_verified = False


# ============================================================
# LOGIN PAGE STYLES
# ============================================================

def render_login_styles():

    st.html(
        """
        <style>

        /* ====================================================
           LOGIN LAYOUT
           ==================================================== */

        .smartstock-login-wrapper {

            max-width: 980px;

            margin: 65px auto 0 auto;

            padding: 0 20px;
        }


        .smartstock-login-brand {

            text-align: center;

            margin-bottom: 34px;
        }


        /* ====================================================
           LOGIN LOGO
           ==================================================== */

        .smartstock-login-logo {

            width: 105px;

            height: 105px;

            margin: 0 auto 18px auto;

            border-radius: 20px;

            display: block;

            object-fit: contain;

            background: #FFFFFF;

            border: 1px solid #D6E5DE;

            box-shadow:
                0 10px 28px
                rgba(23, 59, 45, 0.10);
        }


        .smartstock-login-logo-fallback {

            width: 105px;

            height: 105px;

            margin: 0 auto 18px auto;

            border-radius: 20px;

            display: flex;

            align-items: center;

            justify-content: center;

            background: #FFFFFF;

            border: 1px solid #D6E5DE;

            box-shadow:
                0 10px 28px
                rgba(23, 59, 45, 0.10);

            font-size: 52px;
        }


        /* ====================================================
           LOGIN BRAND TEXT
           ==================================================== */

        .smartstock-login-title {

            color: #075333 !important;

            font-size: 34px;

            font-weight: 850;

            line-height: 1.15;

            margin: 0;
        }


        .smartstock-login-subtitle {

            color: #527366 !important;

            font-size: 15px;

            line-height: 1.65;

            margin-top: 8px;
        }


        .smartstock-login-note {

            color: #527366 !important;

            font-size: 14px;

            margin-top: 5px;
        }


        /* ====================================================
           LOGIN FOOTER
           ==================================================== */

        .smartstock-login-footer {

            text-align: center;

            color: #6B8277;

            font-size: 12px;

            line-height: 1.7;

            margin-top: 28px;
        }


        /* ====================================================
           PRIMARY LOGIN BUTTON
           ==================================================== */

        div.stButton > button[kind="primary"] {

            background:
                linear-gradient(
                    135deg,
                    #DC2626 0%,
                    #B91C1C 100%
                ) !important;

            color: #FFFFFF !important;

            border: 1px solid #991B1B !important;

            border-radius: 12px !important;

            font-weight: 800 !important;

            min-height: 48px !important;

            box-shadow:
                0 6px 16px
                rgba(185, 28, 28, 0.22) !important;
        }


        div.stButton > button[kind="primary"]:hover {

            background:
                linear-gradient(
                    135deg,
                    #B91C1C 0%,
                    #991B1B 100%
                ) !important;

            color: #FFFFFF !important;

            border: 1px solid #7F1D1D !important;
        }


        div.stButton > button[kind="primary"]:focus {

            background: #B91C1C !important;

            color: #FFFFFF !important;

            border: 2px solid #7F1D1D !important;
        }


        </style>
        """
    )


# ============================================================
# LOGIN SCREEN
# ============================================================

def render_login_screen():

    render_login_styles()

    login_logo = load_login_logo()


    # --------------------------------------------------------
    # BRAND
    # --------------------------------------------------------

    if login_logo:

        logo_html = f"""
            <img
                class="smartstock-login-logo"
                src="{login_logo}"
                alt="SmartStock basket logo"
            >
        """

    else:

        logo_html = """
            <div class="smartstock-login-logo-fallback">
                🛒
            </div>
        """


    st.html(
        f"""
        <div class="smartstock-login-wrapper">

            <div class="smartstock-login-brand">

                {logo_html}

                <div class="smartstock-login-title">
                    SmartStock.AI
                </div>

                <div class="smartstock-login-subtitle">
                    SME Demand Forecasting Decision Engine
                </div>

                <div class="smartstock-login-note">
                    Sign in to access the SmartStock
                    decision-support application.
                </div>

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # CREDENTIAL CONFIGURATION CHECK
    # --------------------------------------------------------

    if (
        not AUTH_USERNAME
        or not AUTH_PASSWORD
    ):

        st.error(
            "Authentication credentials have not been configured."
        )

        st.info(
            """
            Configure your local credentials in:

            `.streamlit/secrets.toml`

            Example:

            ```toml
            SMARTSTOCK_USERNAME = "admin"
            SMARTSTOCK_PASSWORD = "your-secure-password"
            ```
            """
        )

        st.html(
            """
            <div class="smartstock-login-footer">

                🔒 Protected SmartStock application
                <br>
                SmartStock AI © 2026

            </div>
            """
        )

        st.stop()


    # --------------------------------------------------------
    # LOGIN FORM
    # --------------------------------------------------------

    with st.container(border=True):

        username = st.text_input(
            "Username",
            placeholder="Enter your username",
            key="login_username",
        )


        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password",
        )


        # ----------------------------------------------------
        # HUMAN VERIFICATION
        # ----------------------------------------------------

        st.subheader(
            "🛡️ Human Verification"
        )

        st.write(
            """
            Please confirm that you are human and complete
            the verification question below.
            """
        )


        human_check = st.checkbox(
            "I confirm that I am a human user.",
            key="human_confirmation",
        )


        captcha_question = (
            f"What is "
            f"{st.session_state.captcha_num1} + "
            f"{st.session_state.captcha_num2}?"
        )


        captcha_answer = st.number_input(
            captcha_question,
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key="captcha_answer",
        )


        submit_login = st.button(
            "🔐 Sign In",
            type="primary",
            use_container_width=True,
            key="sign_in_button",
        )


    # --------------------------------------------------------
    # LOGIN VALIDATION
    # --------------------------------------------------------

    if submit_login:

        expected_answer = (
            st.session_state.captcha_num1
            + st.session_state.captcha_num2
        )


        username_valid = hmac.compare_digest(
            str(username).strip(),
            str(AUTH_USERNAME).strip(),
        )


        password_valid = hmac.compare_digest(
            str(password),
            str(AUTH_PASSWORD),
        )


        human_valid = (
            human_check
            and int(captcha_answer)
            == expected_answer
        )


        if not human_check:

            st.error(
                "Please confirm that you are a human user."
            )


        elif not human_valid:

            st.error(
                "Human verification failed. "
                "Please answer the question correctly."
            )

            reset_human_challenge()


        elif (
            not username_valid
            or not password_valid
        ):

            st.error(
                "Invalid username or password."
            )


        else:

            st.session_state.authenticated = True

            st.session_state.human_verified = True

            st.rerun()


    # --------------------------------------------------------
    # LOGIN FOOTER
    # --------------------------------------------------------

    st.html(
        """
        <div class="smartstock-login-footer">

            🔒 Protected SmartStock application
            <br>

            SmartStock AI © 2026

        </div>
        """
    )


# ============================================================
# AUTHENTICATION GATE
# ============================================================

if not st.session_state.authenticated:

    st.html(
        """
        <style>

        section[data-testid="stSidebar"] {
            display: none !important;
        }

        [data-testid="collapsedControl"] {
            display: none !important;
        }

        </style>
        """
    )

    render_login_screen()

    st.stop()


# ============================================================
# LANGUAGE INITIALIZATION
# ============================================================

current_language = get_language()


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


# ============================================================
# APPLICATION NAVIGATION
# ============================================================

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
# AUTHENTICATED SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # SMARTSTOCK LOGO
    # --------------------------------------------------------

    render_sidebar_logo()


    # --------------------------------------------------------
    # LANGUAGE SELECTOR
    # --------------------------------------------------------

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


    language_names = list(
        LANGUAGES.keys()
    )


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
            language_names.index(
                current_language_name
            )
            if current_language_name
            in language_names
            else 0
        ),
        key="app_language_selector",
        label_visibility="collapsed",
    )


    selected_language = LANGUAGES[
        selected_language_name
    ]


    if (
        selected_language
        != current_language
    ):

        set_language(
            selected_language
        )

        st.rerun()


    # --------------------------------------------------------
    # NAVIGATION DIVIDER
    # --------------------------------------------------------

    st.markdown("---")


    # --------------------------------------------------------
    # NAVIGATION LINKS
    # --------------------------------------------------------

    st.page_link(
        home_page,
        label=t("home"),
        icon="🏠",
    )


    st.page_link(
        dashboard_page,
        label=t("dashboard"),
        icon="📊",
    )


    st.page_link(
        forecast_page,
        label=t("forecast"),
        icon="🔮",
    )


    st.page_link(
        stock_page,
        label=t("stock"),
        icon="📦",
    )


    st.page_link(
        model_page,
        label=t("model"),
        icon="🤖",
    )


    st.page_link(
        about_page,
        label=t("about"),
        icon="ℹ️",
    )


    # --------------------------------------------------------
    # SIGN OUT
    # --------------------------------------------------------

    st.markdown("---")


    if st.button(
        "🚪 Sign Out",
        type="primary",
        use_container_width=True,
        key="sign_out_button",
    ):

        st.session_state.authenticated = False

        st.session_state.human_verified = False

        reset_human_challenge()


        for key in [
            "login_username",
            "login_password",
            "human_confirmation",
            "captcha_answer",
        ]:

            if key in st.session_state:

                del st.session_state[key]


        st.rerun()


# ============================================================
# STREAMLIT NAVIGATION ENGINE
# ============================================================

pg = st.navigation(
    pages,
    position="hidden",
)


# ============================================================
# RUN CURRENT PAGE
# ============================================================

pg.run()