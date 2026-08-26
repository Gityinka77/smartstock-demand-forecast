# 🇳🇬 SmartStock.AI — SME Demand Forecasting Decision Engine

SmartStock.AI is a Streamlit machine-learning decision-support application designed for Nigerian SMEs. It connects historical FMCG sales analysis, demand forecasting and inventory replenishment planning in one workflow.

## 🌐 Live Application

**SmartStock.AI:**

https://smartstock-demand-forecast-bwrvkcagt6ebum6bkbt4jg.streamlit.app/

> The live deployment reads the same application code and model artifacts maintained in this repository. Authentication credentials are supplied through Streamlit Secrets and are never stored in GitHub.

## 🚀 Enhanced Application Workflow

```text
🔐 Secure Login
      ↓
🏠 Home / Executive Overview
      ↓
📊 Sales Dashboard & EDA
      ↓
🔮 Demand Forecast
      ↓
📦 Stock & Reorder Advisory
      ↓
🤖 Model Performance
      ↓
ℹ️ About SmartStock
```

## ✨ Key Features

- **Secure application gate:** Username/password authentication with a lightweight human-verification challenge.
- **Multilingual navigation:** English, Nigerian Pidgin, Yoruba, Igbo and Hausa are available from the application language selector.
- **Executive dashboard:** Historical demand KPIs, top products, business insights and Nigerian SME context.
- **Demand EDA:** Trends, moving averages, demand distribution, price/volume relationships, promotions, payday effects, weekends, seasonality, holidays, rainfall and correlations.
- **Machine-learning demand forecast:** Production Gradient Boosting model with recursive multi-day forecasting.
- **Nigerian payday logic:** The forecast engine treats the 25th through the 2nd as the payday period.
- **Scenario planning:** Promotion, discount and rainfall assumptions can be changed before generating a forecast.
- **Inventory advisory:** Lead-time demand, safety stock, required stock, reorder quantity and stock-status recommendations.
- **Model transparency:** MAE, RMSE, R², prediction-vs-actual analysis, residual analysis and feature importance.
- **Exports:** Forecast and reorder reports can be downloaded as CSV files.

## 🧠 Machine-Learning Pipeline

The production model is a saved Gradient Boosting regression model. The application does **not** retrain the model when a user opens the dashboard.

The saved artifacts are:

```text
model/
├── best_gradient_boosting_model.pkl
├── model_features.pkl
└── model_performance.pkl
```

The saved feature list is treated as the source of truth for prediction-column order. The shared forecasting engine in `utils/forecast_engine.py` is used by the forecast and inventory pages so that future-feature construction remains consistent.

### Core demand features

- Unit price
- Payday period
- Promotion flag
- Discount percentage
- Weekend flag
- Holiday flag
- Month
- Day of month
- Quarter
- Lag 1 demand
- Lag 7 demand
- 7-day rolling mean
- 7-day rolling standard deviation
- Product category one-hot features
- Season
- Rainfall severity

## 📦 Inventory Decision Logic

The inventory advisory translates forecast demand into operational quantities.

```text
Average Forecast Demand × Supplier Lead Time
                    ↓
             Lead-Time Demand
                    ↓
       + Safety Stock Coverage
                    ↓
             Required Stock
                    ↓
       Required Stock − Current Stock
                    ↓
       Recommended Reorder Quantity
```

Stock status is classified as:

- 🔴 **REORDER NOW** — current stock is below estimated lead-time demand.
- 🟡 **MONITOR STOCK** — current stock covers lead-time demand but does not provide the selected safety-stock buffer.
- 🟢 **HEALTHY STOCK** — current stock covers both lead-time demand and the safety-stock requirement.

## 🇳🇬 Nigerian SME Context

SmartStock explicitly models or analyses factors relevant to Nigerian retail demand, including:

- Payday periods
- Promotions and discounts
- Weekends
- Festive/holiday periods
- Rainy and dry seasons
- Rainfall severity
- Product/category behaviour

The current forecasting engine contains a fixed-date holiday layer. Movable religious holidays should be maintained through a dedicated holiday calendar rather than guessed from month/day rules.

## 🔐 Deployment Authentication

The login system intentionally does **not** hard-code a username or password into the repository.

Configure the following in Streamlit Cloud **App Settings → Secrets**:

```toml
SMARTSTOCK_USERNAME = "your_username"
SMARTSTOCK_PASSWORD = "your_strong_password"
```

For local development, create:

```text
.streamlit/secrets.toml
```

with the same values. Do not commit that file to GitHub.

If the credentials are missing, the application will display a configuration message instead of allowing an unauthenticated session.

## 🧪 Validation

The repository includes GitHub Actions validation for pushes and pull requests to `main`.

The CI pipeline:

1. Installs the pinned project dependencies.
2. Compiles `app.py`, `styles.py`, `pages/` and `utils/` to catch Python syntax errors.
3. Runs a smoke test against the shared forecasting engine.
4. Verifies the Nigerian payday rule and model-feature alignment behaviour.

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Plotly
- Streamlit
- Matplotlib
- Seaborn
- Statsmodels
- GitHub
- GitHub Actions

## 📁 Project Structure

```text
smartstock-demand-forecast/
│
├── assets/                       # SmartStock branding assets
├── data/                         # FMCG sales dataset
├── model/                        # Production model artifacts
├── notebook/                     # ML development notebook
├── pages/                        # Streamlit application pages
│   ├── 1_home_page.py
│   ├── 2_📊_Dashboard_EDA.py
│   ├── 3_🔮_Demand_Forecast.py
│   ├── 4_📦_Inventory_Advisory.py
│   ├── 5_📈_Model_Metrics.py
│   └── 6_ℹ️_About.py
├── utils/
│   ├── data_loader.py
│   ├── forecast_engine.py
│   └── i18n.py
├── app.py                        # Authentication and navigation router
├── styles.py                     # Shared visual design system
├── requirements.txt
├── .github/workflows/            # Automated validation
└── README.md
```

## ▶️ Run Locally

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` with your credentials, then run:

```bash
streamlit run app.py
```

## 📓 Model Development

The machine-learning development notebook is:

```text
notebook/SmartStock_ML_Pipeline.ipynb
```

The notebook contains data preparation, exploratory analysis, feature engineering, model comparison/training, evaluation and serialization of the production artifacts.

## 🎯 Business Objective

SmartStock is designed around a simple SME problem:

> **How much stock should I expect to sell, and when should I reorder?**

The application therefore goes beyond displaying a machine-learning prediction. It connects the prediction to a practical stock-planning decision.

## 📌 Important Production Note

The model artifact itself is not retrained by the Streamlit application. Any change to the trained model or its feature engineering pipeline should be made in the notebook, evaluated on a chronological holdout, serialized to the `model/` directory, and then validated through the application before deployment.

---

**SmartStock.AI — SME Demand Forecasting + Inventory Decision Support** 🇳🇬