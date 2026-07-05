import sys
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from config import APP_TITLE
from styles import apply_custom_css, configure_page
from components.header import render_header
from components.sidebar import render_sidebar
from components.input_form import render_input_form
from components.verdict import (
    render_verdict,
    render_model_governance,
    render_recommended_action,
)
from components.evidence import render_evidence
from components.technical import render_technical_appendix
from services.model_service import load_artifacts
from services.prediction_service import build_model_input, make_prediction
from services.explanation_service import get_shap_values_for_fake_class, get_top_explanation_signals


def main():
    configure_page(APP_TITLE)
    apply_custom_css()

    model, features, threshold, explainer = load_artifacts()

    render_header()
    render_sidebar(threshold)

    raw_inputs, submitted = render_input_form()
    input_df = build_model_input(raw_inputs, features)

    if submitted:
        with st.spinner("Reading the evidence..."):
            fraud_probability, prediction, risk_level = make_prediction(
                model=model,
                input_df=input_df,
                threshold=threshold,
            )
            shap_values_fake = get_shap_values_for_fake_class(explainer, input_df)
            top_reasons = get_top_explanation_signals(input_df, shap_values_fake, top_n=6)

        st.divider()
        render_verdict(fraud_probability, prediction, risk_level, top_reasons, threshold)
        render_recommended_action(risk_level)

        st.divider()
        render_evidence(top_reasons)

        st.markdown("<br>", unsafe_allow_html=True)
        render_model_governance(threshold)
        render_technical_appendix(shap_values_fake, input_df)
    else:
        st.markdown(
            """
            <div class="empty-state">
                Fill in the details above and select <b>Get the verdict</b> to see the result.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="footer-note">Verdict IQ — a behavioral, reputation-based fake review detector built with explainable machine learning.</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
