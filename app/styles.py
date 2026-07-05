import streamlit as st


def configure_page(title: str):
    st.set_page_config(
        page_title=f"{title} — Review Verdict",
        page_icon="🔎",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def apply_custom_css():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap');

            :root {
                --paper: #FBF8F1;
                --paper-raised: #FFFFFF;
                --ink: #1B1B1F;
                --ink-soft: #5B5A55;
                --line: #E6E0D2;
                --stamp: #B5471B;
                --stamp-soft: #F3E3D8;
                --genuine: #2F6B4F;
                --genuine-soft: #E4EFE8;
                --low: #2F6B4F;
                --medium: #A6790A;
                --high: #C1531B;
                --critical: #A32424;
                --shadow: 0 18px 40px rgba(27, 27, 31, 0.07);
                --shadow-soft: 0 8px 20px rgba(27, 27, 31, 0.05);
            }

            html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

            .stApp { background: var(--paper); }

            [data-testid="stMainBlockContainer"] { max-width: 1180px; }

            .main .block-container,
            [data-testid="stAppViewContainer"] .main .block-container {
                width: 100%;
                max-width: 1180px;
                margin: 0 auto;
                padding-top: 2rem;
                padding-bottom: 3.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            h1, h2, h3 { font-family: 'Inter', sans-serif; color: var(--ink); }

            /* ---------- Sidebar ---------- */
            section[data-testid="stSidebar"] {
                width: 300px;
                background: var(--paper-raised);
                border-right: 1px solid var(--line);
            }

            section[data-testid="stSidebar"] > div { padding: 1.5rem 1.3rem; }

            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2,
            section[data-testid="stSidebar"] h3,
            section[data-testid="stSidebar"] p,
            section[data-testid="stSidebar"] span,
            section[data-testid="stSidebar"] label { color: var(--ink) !important; }

            .side-mark {
                font-family: 'Fraunces', serif;
                font-size: 1.55rem;
                font-weight: 600;
                letter-spacing: -0.01em;
                color: var(--ink);
                margin-bottom: 0.1rem;
            }

            .side-mark span { color: var(--stamp); }

            .side-tagline {
                color: var(--ink-soft);
                font-size: 0.85rem;
                margin-bottom: 1.3rem;
                line-height: 1.5;
            }

            .side-block {
                border-top: 1px solid var(--line);
                padding-top: 1rem;
                margin-top: 1rem;
            }

            .side-label {
                font-size: 0.68rem;
                color: var(--ink-soft);
                text-transform: uppercase;
                letter-spacing: 0.09em;
                font-weight: 700;
                margin-bottom: 0.5rem;
            }

            .side-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 0.6rem;
                padding: 0.4rem 0;
                font-size: 0.86rem;
                color: var(--ink);
            }

            .dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; margin-right: 0.45rem; flex-shrink: 0; }
            .dot-low { background: var(--low); }
            .dot-medium { background: var(--medium); }
            .dot-high { background: var(--high); }
            .dot-critical { background: var(--critical); }

            .side-note {
                color: var(--ink-soft);
                font-size: 0.82rem;
                line-height: 1.55;
            }

            /* ---------- Hero ---------- */
            .hero {
                padding: 0.4rem 0 1.8rem 0;
                margin-bottom: 0.6rem;
            }

            .hero-mark {
                display: inline-flex;
                align-items: center;
                gap: 0.45rem;
                font-size: 0.74rem;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                font-weight: 700;
                color: var(--stamp);
                margin-bottom: 0.9rem;
            }

            .hero-mark::before {
                content: "";
                width: 7px;
                height: 7px;
                border-radius: 50%;
                background: var(--stamp);
                display: inline-block;
            }

            .hero-title {
                font-family: 'Fraunces', serif;
                font-size: 3.1rem;
                line-height: 1.05;
                font-weight: 600;
                color: var(--ink);
                letter-spacing: -0.02em;
                margin-bottom: 0.7rem;
            }

            .hero-title em { color: var(--stamp); font-style: normal; }

            .hero-subtitle {
                max-width: 620px;
                color: var(--ink-soft);
                font-size: 1.08rem;
                line-height: 1.65;
            }

            /* ---------- Section headers ---------- */
            .section-title {
                font-family: 'Fraunces', serif;
                font-size: 1.5rem;
                font-weight: 600;
                color: var(--ink);
                margin-top: 0.5rem;
                margin-bottom: 0.2rem;
                letter-spacing: -0.01em;
            }

            .section-copy {
                color: var(--ink-soft);
                font-size: 0.95rem;
                margin-bottom: 1.1rem;
                line-height: 1.55;
            }

            /* ---------- Form card ---------- */
            .form-card {
                background: var(--paper-raised);
                border: 1px solid var(--line);
                border-radius: 20px;
                padding: 1.6rem 1.8rem 0.6rem 1.8rem;
                margin: 0.8rem 0 1.4rem 0;
                box-shadow: var(--shadow-soft);
            }

            .form-group-label {
                font-size: 0.78rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                font-weight: 750;
                color: var(--stamp);
                margin: 1.1rem 0 0.2rem 0;
            }

            .form-group-label:first-child { margin-top: 0.1rem; }

            .form-group-hint {
                color: var(--ink-soft);
                font-size: 0.85rem;
                margin-bottom: 0.7rem;
                margin-top: -0.1rem;
            }

            div[data-testid="stSlider"] label,
            div[data-testid="stNumberInput"] label {
                font-size: 0.86rem !important;
                font-weight: 600 !important;
                color: var(--ink) !important;
            }

            div[data-testid="stNumberInput"] input {
                border-radius: 10px !important;
            }

            /* ---------- Verdict stamp ---------- */
            .verdict-card {
                background: var(--paper-raised);
                border: 1px solid var(--line);
                border-radius: 24px;
                padding: 2rem 2.2rem;
                margin: 1.2rem 0;
                box-shadow: var(--shadow);
                display: grid;
                grid-template-columns: 168px 1fr;
                gap: 2rem;
                align-items: center;
            }

            .stamp-wrap { display: flex; justify-content: center; }

            .verdict-eyebrow {
                font-size: 0.76rem;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                font-weight: 750;
                margin-bottom: 0.5rem;
            }

            .verdict-headline {
                font-family: 'Fraunces', serif;
                font-size: 2.3rem;
                font-weight: 600;
                color: var(--ink);
                letter-spacing: -0.02em;
                line-height: 1.08;
                margin-bottom: 0.55rem;
            }

            .verdict-summary {
                color: var(--ink-soft);
                font-size: 1.02rem;
                line-height: 1.6;
                max-width: 560px;
            }

            .verdict-meta {
                margin-top: 1.1rem;
                display: flex;
                gap: 1.6rem;
                flex-wrap: wrap;
            }

            .verdict-meta-item { font-size: 0.86rem; color: var(--ink-soft); }
            .verdict-meta-item b { color: var(--ink); font-family: 'IBM Plex Mono', monospace; font-weight: 600; }

            @media (max-width: 900px) {
                .verdict-card { grid-template-columns: 1fr; text-align: center; }
                .verdict-summary { max-width: 100%; }
                .verdict-meta { justify-content: center; }
            }

            /* ---------- Confidence bar ---------- */
            .meter-shell { margin: 1.4rem 0 0.3rem 0; }

            .meter-track {
                height: 10px;
                width: 100%;
                border-radius: 999px;
                background: linear-gradient(90deg, var(--low) 0%, var(--low) 30%, var(--medium) 30%, var(--medium) 60%, var(--high) 60%, var(--high) 80%, var(--critical) 80%, var(--critical) 100%);
                position: relative;
                opacity: 0.85;
            }

            .meter-marker {
                width: 18px;
                height: 18px;
                border-radius: 50%;
                background: var(--ink);
                border: 3px solid var(--paper-raised);
                box-shadow: 0 3px 8px rgba(27,27,31,0.3);
                position: absolute;
                top: -4px;
                transform: translateX(-50%);
            }

            .meter-labels {
                display: flex;
                justify-content: space-between;
                color: var(--ink-soft);
                font-size: 0.74rem;
                font-weight: 700;
                margin-top: 0.5rem;
                text-transform: uppercase;
                letter-spacing: 0.04em;
            }

            /* ---------- Action card ---------- */
            .action-card {
                background: var(--paper-raised);
                border: 1px solid var(--line);
                border-left: 5px solid var(--stamp);
                border-radius: 18px;
                padding: 1.4rem 1.6rem;
                margin: 1.2rem 0;
                box-shadow: var(--shadow-soft);
            }

            .action-kicker {
                font-size: 0.74rem;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                font-weight: 750;
                color: var(--stamp);
                margin-bottom: 0.4rem;
            }

            .action-title {
                font-family: 'Fraunces', serif;
                font-size: 1.4rem;
                font-weight: 600;
                color: var(--ink);
                margin-bottom: 0.5rem;
            }

            .action-copy {
                color: var(--ink-soft);
                font-size: 0.96rem;
                line-height: 1.6;
                margin-bottom: 0.7rem;
            }

            .action-steps { margin: 0; padding-left: 1.2rem; color: var(--ink); }
            .action-steps li { margin-bottom: 0.3rem; font-size: 0.92rem; }

            /* ---------- Evidence ---------- */
            .evidence-card {
                background: var(--paper-raised);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 1.2rem 1.35rem;
                margin: 0.6rem 0;
                box-shadow: var(--shadow-soft);
                height: 100%;
            }

            .evidence-tag {
                display: inline-block;
                font-size: 0.7rem;
                font-weight: 750;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                padding: 0.22rem 0.55rem;
                border-radius: 999px;
                margin-bottom: 0.6rem;
            }

            .tag-risk { background: #FBE7DD; color: var(--high); }
            .tag-safe { background: var(--genuine-soft); color: var(--genuine); }

            .evidence-feature {
                font-weight: 700;
                color: var(--ink);
                font-size: 1rem;
                margin-bottom: 0.3rem;
            }

            .evidence-value {
                font-family: 'IBM Plex Mono', monospace;
                color: var(--ink-soft);
                font-size: 0.82rem;
                margin-bottom: 0.5rem;
            }

            .evidence-text {
                color: var(--ink-soft);
                font-size: 0.9rem;
                line-height: 1.55;
            }

            .chip-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.7rem; }

            .topic-chip {
                border: 1px solid var(--line);
                background: var(--stamp-soft);
                color: var(--stamp);
                border-radius: 999px;
                padding: 0.3rem 0.7rem;
                font-size: 0.8rem;
                font-weight: 700;
            }

            /* ---------- About / governance ---------- */
            .about-card {
                background: var(--paper-raised);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 1.3rem 1.5rem;
                margin: 1rem 0;
                box-shadow: var(--shadow-soft);
            }

            .about-title {
                font-weight: 750;
                color: var(--ink);
                font-size: 1rem;
                margin-bottom: 0.4rem;
            }

            .about-copy { color: var(--ink-soft); font-size: 0.92rem; line-height: 1.6; }

            /* ---------- Buttons ---------- */
            .stButton > button {
                background: var(--ink);
                color: var(--paper);
                border: 0;
                border-radius: 12px;
                font-weight: 700;
                padding: 0.8rem 1.1rem;
                transition: background 0.15s ease;
            }

            .stButton > button:hover { background: var(--stamp); color: white; }

            div[data-testid="stExpander"] {
                border: 1px solid var(--line);
                border-radius: 14px;
                background: var(--paper-raised);
            }

            /* ---------- Footer ---------- */
            .footer-note {
                text-align: center;
                color: var(--ink-soft);
                font-size: 0.8rem;
                margin-top: 2.6rem;
                padding-top: 1.4rem;
                border-top: 1px solid var(--line);
            }

            .empty-state {
                background: var(--paper-raised);
                border: 1px dashed var(--line);
                border-radius: 18px;
                padding: 1.4rem 1.6rem;
                color: var(--ink-soft);
                font-size: 0.95rem;
                margin-top: 1rem;
            }

            @media (max-width: 900px) {
                .hero-title { font-size: 2.2rem; }
                .main .block-container, [data-testid="stMainBlockContainer"] {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
