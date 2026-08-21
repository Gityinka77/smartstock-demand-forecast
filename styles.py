import base64
import html
import os

import streamlit as st


# ============================================================
# SMARTSTOCK ASSET PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ASSETS_DIR = os.path.join(
    BASE_DIR,
    "assets"
)

LOGO_PATH = os.path.join(
    ASSETS_DIR,
    "smartstock_logo.png"
)

BANNER_PATH = os.path.join(
    ASSETS_DIR,
    "smartstock_banner.png"
)


# ============================================================
# IMAGE TO BASE64
# ============================================================

def _image_to_base64(image_path):

    if not os.path.exists(image_path):
        return None

    try:

        with open(
            image_path,
            "rb"
        ) as image_file:

            encoded = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        extension = (
            os.path.splitext(
                image_path
            )[1]
            .lower()
        )

        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".gif": "image/gif",
        }

        mime_type = mime_types.get(
            extension,
            "image/png"
        )

        return (
            f"data:{mime_type};base64,{encoded}"
        )

    except Exception:

        return None


# ============================================================
# GLOBAL SMARTSTOCK STYLES
# ============================================================

def apply_global_styles():

    st.markdown(
        """
        <style>

        /* =====================================================
           APPLICATION BACKGROUND
           ===================================================== */

        .stApp {

            background:
                linear-gradient(
                    135deg,
                    #F8FBF9 0%,
                    #F3F8F5 50%,
                    #EEF5F1 100%
                ) !important;

            color:
                #173B2D !important;

            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif !important;
        }


        /* =====================================================
           MAIN CONTENT
           ===================================================== */

        section[data-testid="stMain"] {

            background:
                transparent !important;
        }


        .main {

            background:
                transparent !important;
        }


        .block-container {

            max-width:
                1450px !important;

            padding-top:
                2rem !important;

            padding-bottom:
                3rem !important;

            padding-left:
                2rem !important;

            padding-right:
                2rem !important;
        }


        /* =====================================================
           STREAMLIT HEADER
           ===================================================== */

        header[data-testid="stHeader"] {

            background:
                #F8FBF9 !important;

            background-color:
                #F8FBF9 !important;

            border-bottom:
                1px solid #DCE8E2 !important;

            box-shadow:
                none !important;
        }


        .stAppHeader {

            background:
                #F8FBF9 !important;

            background-color:
                #F8FBF9 !important;
        }


        [data-testid="stToolbar"] {

            background:
                transparent !important;
        }


        [data-testid="stDecoration"] {

            display:
                none !important;
        }


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #EAF4EF 0%,
                    #E4F1EB 55%,
                    #DDEDE5 100%
                ) !important;

            border-right:
                1px solid #C9DED4 !important;

            box-shadow:
                3px 0 18px
                rgba(23, 59, 45, 0.06) !important;
        }


        section[data-testid="stSidebar"] > div {

            background:
                transparent !important;
        }


        section[data-testid="stSidebar"] * {

            color:
                #173B2D;
        }


        /* =====================================================
           SIDEBAR NAVIGATION
           ===================================================== */

        section[data-testid="stSidebar"]
        [data-testid="stPageLink-NavLink"] {

            border-radius:
                10px !important;

            margin-bottom:
                4px !important;

            color:
                #244D3C !important;
        }


        section[data-testid="stSidebar"]
        [data-testid="stPageLink-NavLink"]:hover {

            background:
                rgba(15, 118, 110, 0.10) !important;

            color:
                #075333 !important;
        }


        section[data-testid="stSidebar"]
        [data-testid="stPageLink-NavLink"][aria-current="page"] {

            background:
                linear-gradient(
                    90deg,
                    #D4E8DF,
                    #C9E2D7
                ) !important;

            color:
                #075333 !important;

            font-weight:
                700 !important;

            box-shadow:
                inset 3px 0 0 #0F766E !important;
        }


        /* =====================================================
           SIDEBAR LANGUAGE SELECTOR
           ===================================================== */

        section[data-testid="stSidebar"]
        div[data-baseweb="select"] > div {

            background:
                #FFFFFF !important;

            border:
                1px solid #BFD7CC !important;

            border-radius:
                10px !important;
        }


        section[data-testid="stSidebar"]
        div[data-baseweb="select"] span {

            color:
                #173B2D !important;
        }


        /* =====================================================
           HEADINGS
           ===================================================== */

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {

            color:
                #073B2A !important;
        }


        h1 {

            font-weight:
                800 !important;

            letter-spacing:
                -0.03em !important;
        }


        h2 {

            font-weight:
                750 !important;

            letter-spacing:
                -0.025em !important;
        }


        h3 {

            font-weight:
                700 !important;
        }


        p {

            color:
                #365B4B;
        }


        /* =====================================================
           LINKS
           ===================================================== */

        a {

            color:
                #087F5B !important;
        }


        /* =====================================================
           SECTION TITLES
           ===================================================== */

        .section-title {

            color:
                #073B2A !important;

            font-size:
                27px;

            font-weight:
                750;

            margin-top:
                10px;

            margin-bottom:
                8px;

            letter-spacing:
                -0.02em;
        }


        .section-description {

            color:
                #527366 !important;

            font-size:
                14px;

            line-height:
                1.65;

            margin-bottom:
                18px;
        }


        /* =====================================================
           HOME HERO
           ===================================================== */

        .smartstock-hero {

            position:
                relative;

            overflow:
                hidden;

            min-height:
                300px;

            display:
                flex;

            align-items:
                center;

            border-radius:
                22px;

            margin-bottom:
                28px;

            border:
                1px solid
                rgba(10, 83, 51, 0.22);

            box-shadow:
                0 16px 38px
                rgba(23, 59, 45, 0.16);

            background:
                linear-gradient(
                    135deg,
                    #075333,
                    #0B7653,
                    #149A73
                );

            background-size:
                cover;

            background-position:
                center;

            background-repeat:
                no-repeat;
        }


        .smartstock-hero-overlay {

            position:
                absolute;

            inset:
                0;

            background:
                linear-gradient(
                    90deg,
                    rgba(4, 54, 34, 0.90) 0%,
                    rgba(4, 54, 34, 0.70) 48%,
                    rgba(4, 54, 34, 0.15) 100%
                );

            pointer-events:
                none;
        }


        .smartstock-hero-content {

            position:
                relative;

            z-index:
                2;

            padding:
                38px 42px;

            max-width:
                900px;
        }


        .smartstock-hero-badge {

            display:
                inline-block;

            padding:
                5px 13px;

            margin-bottom:
                12px;

            border-radius:
                999px;

            background:
                rgba(255,255,255,0.14);

            border:
                1px solid
                rgba(255,255,255,0.32);

            color:
                #FFFFFF !important;

            font-size:
                11px;

            font-weight:
                800;

            text-transform:
                uppercase;

            letter-spacing:
                0.08em;
        }


        .smartstock-hero-title {

            color:
                #FFFFFF !important;

            font-size:
                38px;

            line-height:
                1.12;

            font-weight:
                850;

            margin:
                0 0 12px 0;

            letter-spacing:
                -0.035em;
        }


        .smartstock-hero-description {

            color:
                rgba(255,255,255,0.92) !important;

            font-size:
                16px;

            line-height:
                1.7;

            max-width:
                850px;

            margin:
                0;
        }


        /* =====================================================
           WHITE CARDS
           ===================================================== */

        [data-testid="stVerticalBlockBorderWrapper"] {

            background:
                rgba(255,255,255,0.95) !important;

            border:
                1px solid #D6E5DE !important;

            border-radius:
                16px !important;

            box-shadow:
                0 6px 20px
                rgba(23,59,45,0.05) !important;
        }


        /* =====================================================
           METRICS
           ===================================================== */

        [data-testid="stMetric"] {

            background:
                #FFFFFF !important;

            border:
                1px solid #D5E5DE !important;

            border-radius:
                16px !important;

            padding:
                18px !important;

            min-height:
                105px;

            box-shadow:
                0 7px 22px
                rgba(23,59,45,0.06) !important;
        }


        [data-testid="stMetricLabel"] {

            color:
                #527366 !important;
        }


        [data-testid="stMetricLabel"] p {

            color:
                #527366 !important;

            font-weight:
                600 !important;
        }


        [data-testid="stMetricValue"] {

            color:
                #075333 !important;

            font-weight:
                800 !important;
        }


        [data-testid="stMetricValue"] div {

            color:
                #075333 !important;

            font-weight:
                800 !important;
        }


        /* =====================================================
           BUTTONS
           ===================================================== */

        .stButton > button,
        .stDownloadButton > button {

            min-height:
                44px !important;

            border-radius:
                11px !important;

            border:
                1px solid #087F5B !important;

            background:
                linear-gradient(
                    135deg,
                    #087F5B,
                    #0F9F72
                ) !important;

            color:
                #FFFFFF !important;

            font-weight:
                700 !important;

            box-shadow:
                0 6px 18px
                rgba(8,127,91,0.16) !important;
        }


        .stButton > button *,
        .stDownloadButton > button * {

            color:
                #FFFFFF !important;
        }


        .stButton > button:hover,
        .stDownloadButton > button:hover {

            background:
                linear-gradient(
                    135deg,
                    #066B4B,
                    #0B8B63
                ) !important;

            border-color:
                #075333 !important;

            transform:
                translateY(-1px);
        }


        /* =====================================================
           INPUTS
           ===================================================== */

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {

            background:
                #FFFFFF !important;

            border:
                1px solid #BFD7CC !important;

            border-radius:
                10px !important;
        }


        div[data-baseweb="select"] *,
        div[data-baseweb="input"] * {

            color:
                #173B2D !important;
        }


        input,
        textarea {

            color:
                #173B2D !important;

            background:
                #FFFFFF !important;
        }


        /* =====================================================
           DATAFRAME
           ===================================================== */

        [data-testid="stDataFrame"] {

            border:
                1px solid #D0E0D8 !important;

            border-radius:
                14px !important;

            overflow:
                hidden !important;

            box-shadow:
                0 5px 18px
                rgba(23,59,45,0.05);
        }


        /* =====================================================
           ALERTS
           ===================================================== */

        [data-testid="stAlert"] {

            border-radius:
                13px !important;
        }


        /* =====================================================
           DIVIDERS
           ===================================================== */

        hr {

            border-color:
                #D7E5DE !important;
        }


        /* =====================================================
           PLOTLY CHART AREA
           ===================================================== */

        .js-plotly-plot {

            background:
                #E8EEEB !important;

            border:
                1px solid #CDDCD5 !important;

            border-radius:
                14px !important;

            padding:
                8px !important;

            box-shadow:
                0 6px 20px
                rgba(23,59,45,0.06);
        }


        .js-plotly-plot .plot-container {

            background:
                #E8EEEB !important;

            border-radius:
                10px !important;
        }


        .js-plotly-plot .svg-container {

            background:
                #E8EEEB !important;

            border-radius:
                10px !important;
        }


        .js-plotly-plot .gtitle {

            fill:
                #073B2A !important;

            font-weight:
                750 !important;
        }


        .js-plotly-plot .xtitle,
        .js-plotly-plot .ytitle {

            fill:
                #365B4B !important;

            font-weight:
                650 !important;
        }


        .js-plotly-plot .xtick text,
        .js-plotly-plot .ytick text {

            fill:
                #527366 !important;
        }


        .js-plotly-plot .legendtext {

            fill:
                #173B2D !important;
        }


        /* =====================================================
           FOOTER
           ===================================================== */

        .footer,
        .smartstock-footer {

            text-align:
                center;

            color:
                #6B8277;

            font-size:
                13px;

            padding:
                25px 0 10px 0;
        }


        /* =====================================================
           STREAMLIT BRANDING
           ===================================================== */

        #MainMenu {

            visibility:
                hidden;
        }


        footer {

            visibility:
                hidden;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SIDEBAR LOGO
# ============================================================

def render_sidebar_logo():

    logo_data = _image_to_base64(
        LOGO_PATH
    )

    if logo_data:

        # IMPORTANT:
        # Use st.sidebar.html(), NOT st.sidebar.markdown().
        # This prevents the HTML from appearing as code.

        st.sidebar.html(
            f"""
            <div style="
                width: 100%;
                text-align: center;
                padding: 8px 0 20px 0;
            ">

                <img
                    src="{logo_data}"
                    alt="SmartStock Logo"
                    style="
                        width: 92px;
                        height: 92px;
                        object-fit: contain;
                        display: block;
                        margin: 0 auto 10px auto;
                    "
                >

                <div style="
                    color: #075333;
                    font-size: 21px;
                    font-weight: 800;
                    line-height: 1.2;
                ">
                    SmartStock
                </div>

                <div style="
                    color: #527366;
                    font-size: 11px;
                    font-weight: 600;
                    margin-top: 5px;
                ">
                    SME Demand Forecasting
                </div>

            </div>
            """
        )

    else:

        st.sidebar.html(
            """
            <div style="
                width: 100%;
                text-align: center;
                padding: 12px 0 20px 0;
            ">

                <div style="
                    width: 72px;
                    height: 72px;
                    margin: 0 auto 10px auto;
                    border-radius: 16px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background:
                        linear-gradient(
                            135deg,
                            #075333,
                            #0F9F72
                        );
                    color: #FFFFFF;
                    font-size: 34px;
                ">
                    📈
                </div>

                <div style="
                    color: #075333;
                    font-size: 21px;
                    font-weight: 800;
                ">
                    SmartStock
                </div>

                <div style="
                    color: #527366;
                    font-size: 11px;
                    margin-top: 5px;
                ">
                    SME Demand Forecasting
                </div>

            </div>
            """
        )


# ============================================================
# HOME HEADER BANNER
# ============================================================

def render_header_banner(title, subtitle):

    banner_data = _image_to_base64(
        BANNER_PATH
    )

    safe_title = html.escape(
        str(title)
    )

    safe_subtitle = html.escape(
        str(subtitle)
    )

    if banner_data:

        background_style = (
            f"background-image:url('{banner_data}');"
        )

    else:

        background_style = """
            background:
                linear-gradient(
                    135deg,
                    #075333 0%,
                    #0B7653 50%,
                    #149A73 100%
                );
        """

    st.html(
        f"""
        <div
            class="smartstock-hero"
            style="{background_style}"
        >

            <div class="smartstock-hero-overlay"></div>

            <div class="smartstock-hero-content">

                <div class="smartstock-hero-badge">
                    SmartStock Decision Engine
                </div>

                <div class="smartstock-hero-title">
                    {safe_title}
                </div>

                <div class="smartstock-hero-description">
                    {safe_subtitle}
                </div>

            </div>

        </div>
        """
    )