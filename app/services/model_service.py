import sys
import joblib
import shap
import streamlit as st

from config import BASE_DIR, MODEL_PATH, FEATURE_PATH, THRESHOLD_PATH

sys.path.append(str(BASE_DIR))


@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        features = joblib.load(FEATURE_PATH)
        threshold = joblib.load(THRESHOLD_PATH)
        explainer = shap.TreeExplainer(model)
        return model, features, threshold, explainer
    except FileNotFoundError as error:
        st.error("Model artifact file is missing. Please ensure all model files exist in the models folder.")
        st.exception(error)
        st.stop()
    except Exception as error:
        st.error("Model artifacts could not be loaded.")
        st.exception(error)
        st.stop()
