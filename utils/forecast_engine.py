"""Shared forecasting utilities for SmartStock AI.

Keeps future-feature construction identical across the Demand Forecast and
Inventory Advisory pages. The saved model feature list is always treated as
the source of truth for column order and one-hot feature availability.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd


def is_payday_period(date: pd.Timestamp) -> int:
    """Return 1 for the Nigerian SME payday window (25th through 2nd)."""
    return int(date.day >= 25 or date.day <= 2)


def is_fixed_holiday(date: pd.Timestamp) -> int:
    """Return 1 for the fixed-date holidays represented by the app.

    Movable religious holidays should come from a maintained holiday calendar
    rather than being guessed from month/day rules. The model can therefore be
    supplemented with a future holiday calendar later without changing this
    engine.
    """
    fixed_dates = {
        (1, 1),    # New Year's Day
        (5, 1),    # Workers' Day
        (10, 1),   # Independence Day
        (12, 25),  # Christmas Day
        (12, 26),  # Boxing Day
        (12, 31),  # Year-end demand effect used by the dataset
    }
    return int((date.month, date.day) in fixed_dates)


def season_for_date(date: pd.Timestamp) -> str:
    """Return the dataset's Rainy/Dry seasonal label."""
    return "Rainy" if 4 <= date.month <= 10 else "Dry"


def _safe_float(value: float | int | None, default: float = 0.0) -> float:
    try:
        result = float(value)
        return result if np.isfinite(result) else default
    except (TypeError, ValueError):
        return default


def build_feature_row(
    *,
    model_features: Iterable[str],
    product_category: str,
    date: pd.Timestamp,
    unit_price: float,
    lag_1: float,
    lag_7: float,
    rolling_mean_7: float,
    rolling_std_7: float,
    promotion: bool,
    discount_percent: float,
    rainfall: str,
    holiday: int | None = None,
) -> pd.DataFrame:
    """Build exactly the feature matrix expected by the saved model."""
    features = list(model_features)
    row = pd.DataFrame(0.0, index=[0], columns=features)

    is_weekend = int(date.weekday() >= 5)
    is_holiday = (
        is_fixed_holiday(date) if holiday is None else int(bool(holiday))
    )

    direct = {
        "Unit_Price_NGN": _safe_float(unit_price),
        "Is_Payday_Period": is_payday_period(date),
        "Is_Promotion": int(bool(promotion)),
        "Discount_Percent": _safe_float(discount_percent),
        "Is_Weekend": is_weekend,
        "Is_Holiday": is_holiday,
        "Day_of_Week": date.weekday(),
        "Day_of_Month": date.day,
        "Month": date.month,
        "Quarter": date.quarter,
        "Lag_1": _safe_float(lag_1),
        "Lag_7": _safe_float(lag_7),
        "Rolling_Mean_7": _safe_float(rolling_mean_7),
        "Rolling_Std_7": _safe_float(rolling_std_7),
    }

    for name, value in direct.items():
        if name in row.columns:
            row.at[0, name] = value

    # The training pipeline uses one-hot encoding for these categorical fields.
    one_hot_values = {
        f"Category_{product_category}": 1.0,
        f"Season_{season_for_date(date)}": 1.0,
        f"Rainfall_Severity_{rainfall}": 1.0,
    }

    for name, value in one_hot_values.items():
        if name in row.columns:
            row.at[0, name] = value

    return row.astype(float)


def recursive_forecast(
    *,
    model,
    model_features: Iterable[str],
    product_category: str,
    start_date: pd.Timestamp,
    demand_history: Iterable[float],
    unit_price: float,
    forecast_days: int,
    promotion: bool,
    discount_percent: float,
    rainfall: str,
    holiday_dates: set | None = None,
) -> pd.DataFrame:
    """Generate a recursive multi-day demand forecast."""
    history = [
        _safe_float(value)
        for value in demand_history
    ]
    fallback = float(np.mean(history)) if history else 0.0
    future_dates = pd.date_range(
        start=start_date + pd.Timedelta(days=1),
        periods=forecast_days,
        freq="D",
    )

    records = []

    for date in future_dates:
        recent_7 = history[-7:]
        lag_1 = history[-1] if history else fallback
        lag_7 = history[-7] if len(history) >= 7 else fallback
        rolling_mean_7 = float(np.mean(recent_7)) if recent_7 else fallback
        rolling_std_7 = (
            float(np.std(recent_7, ddof=1))
            if len(recent_7) >= 2
            else 0.0
        )

        holiday = None
        if holiday_dates is not None:
            holiday = date.date() in holiday_dates

        row = build_feature_row(
            model_features=model_features,
            product_category=product_category,
            date=date,
            unit_price=unit_price,
            lag_1=lag_1,
            lag_7=lag_7,
            rolling_mean_7=rolling_mean_7,
            rolling_std_7=rolling_std_7,
            promotion=promotion,
            discount_percent=discount_percent if promotion else 0,
            rainfall=rainfall,
            holiday=holiday,
        )

        prediction = float(model.predict(row)[0])
        prediction = max(0.0, prediction)
        history.append(prediction)

        records.append(
            {
                "Date": date,
                "Forecast Demand": prediction,
                "Category": product_category,
                "Promotion": "Yes" if promotion else "No",
                "Discount (%)": discount_percent if promotion else 0,
                "Rainfall": rainfall,
                "Is_Payday_Period": is_payday_period(date),
                "Is_Weekend": int(date.weekday() >= 5),
                "Is_Holiday": int(
                    is_fixed_holiday(date)
                    if holiday is None
                    else bool(holiday)
                ),
            }
        )

    result = pd.DataFrame(records)
    if not result.empty:
        result["Forecast Demand"] = (
            result["Forecast Demand"].round(0).astype(int)
        )
    return result
