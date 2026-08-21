import os
import joblib
import pandas as pd
import streamlit as st


def resolve_path(relative_path):
    """
    Dynamic Path Resolution Fallback:
    Checks the primary path relative to root, parent directories, 
    and checks both 'model/' and 'models/' directories to prevent FileNotFoundError.
    """
    path_variations = [
        relative_path,
        os.path.join("..", relative_path),
        relative_path.replace("model/", "models/") if "model/" in relative_path else relative_path.replace("models/", "model/")
    ]
    
    # Absolute path check relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_variations.append(os.path.join(base_dir, relative_path))

    for path in path_variations:
        if os.path.exists(path):
            return path
            
    raise FileNotFoundError(f"❌ File not found. Tried paths: {path_variations}")


@st.cache_resource
def load_model_artifacts():
    """
    Standardized loader for trained models, feature lists, and performance metrics.
    """
    try:
        model_path = resolve_path("model/best_gradient_boosting_model.pkl")
        features_path = resolve_path("model/model_features.pkl")
        metrics_path = resolve_path("model/model_performance.pkl")
        
        model = joblib.load(model_path)
        features = joblib.load(features_path)
        metrics = joblib.load(metrics_path) if os.path.exists(metrics_path) else None
        
        return model, features, metrics
    except Exception as e:
        return None, None, str(e)


@st.cache_data
def load_fmcg_data():
    """
    Standardized loader for raw FMCG transaction dataset.
    """
    try:
        csv_path = resolve_path("data/smartstock_fmcg_sales.csv")
        return pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error loading sales data: {e}")
        return None


# Alias for backward compatibility across pages
load_sales_data = load_fmcg_data


def detect_columns(df):
    """
    Maps dataset column names dynamically to expected key names.
    """
    if df is None:
        return {}
    
    cols = {col.lower().strip(): col for col in df.columns}
    
    mapping = {
        "date": None,
        "product": None,
        "category": None,
        "demand": None,
        "price": None
    }
    
    for key in mapping.keys():
        for col_lower, col_original in cols.items():
            if key in col_lower or (key == "demand" and ("quantity" in col_lower or "sales" in col_lower or "units" in col_lower)):
                mapping[key] = col_original
                break
                
    return mapping