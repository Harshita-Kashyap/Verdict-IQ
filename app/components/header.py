import streamlit as st

from config import APP_SUBTITLE


def render_header():
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-mark">Fake Review Detector</div>
            <div class="hero-title">Verdict <em>IQ</em></div>
            <div class="hero-subtitle">{APP_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
