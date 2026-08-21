# 🇳🇬 SmartStock.AI: SME Demand Forecasting Decision Engine

## 🌐 Live Web Application

**SmartStock.AI is available online here:**

https://smartstock-demand-forecast-bwrvkcagt6ebum6bkbt4jg.streamlit.app/

SmartStock.AI is an end-to-end machine learning and decision-support web application designed to help Nigerian and African Small and Medium Enterprises (SMEs) predict product demand, optimize inventory levels, and prevent costly stockouts.

---

## 🚀 Features

* **Interactive Sales Dashboard & EDA:** Explore historical Fast-Moving Consumer Goods (FMCG) sales trends, seasonal patterns, weekend spikes, and correlation matrices.

* **Real-Time Demand Forecasting:** Generate daily and weekly unit demand predictions using trained machine learning models, factoring in promotional flags and weather parameters.

* **Inventory Advisory & Restock Alerts:** Automatically translates predicted demand into safety stock levels, optimal reorder thresholds, lead-time requirements, and payday stockout risk warnings.

* **Model Performance Metrics:** Inspect validation metrics (MAE, RMSE, $R^2$), residual plots, and feature importances derived from the ML pipeline.

* **Multilingual Support:** Accessible in multiple languages including English, Nigerian Pidgin, Yoruba, Hausa, and Igbo.

---

## 🛠️ Project Structure

```text
C:\Users\h\OneDrive\Desktop\SME Demand Forecast\
│
├── assets\                 # Branding assets (logo.png, banner.png)
├── data\                   # FMCG sales dataset
├── model\                  # Trained ML model and deployment artifacts
├── notebook\               # Machine learning development notebook
├── pages\                  # Streamlit application pages
├── utils\                  # Helper modules (data_loader.py, i18n.py)
├── app.py                  # Main Streamlit router/entry point
├── home.py                 # Home page view
├── styles.py               # Global CSS styling & rendering functions
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation