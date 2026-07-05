import pandas as pd
import streamlit as st

from src.feature_engineering import calculate_engineered_features
from utils.risk_policy import get_risk_level


def build_model_input(raw_inputs, features):
    engineered = calculate_engineered_features(raw_inputs)
    input_data = {**raw_inputs, **engineered}
    input_df = pd.DataFrame([input_data])

    missing_features = set(features) - set(input_df.columns)
    if missing_features:
        st.error("Model input validation failed.")
        st.write("Missing required model features:")
        st.write(sorted(missing_features))
        st.stop()

    return input_df[features]


def make_prediction(model, input_df, threshold):
    fraud_probability = model.predict_proba(input_df)[0][1]
    prediction = 1 if fraud_probability >= float(threshold) else 0
    risk_level = get_risk_level(fraud_probability)
    return fraud_probability, prediction, risk_level
