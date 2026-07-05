import streamlit as st
import streamlit.components.v1 as components

from utils.risk_policy import (
    get_confidence_note,
    get_recommended_action,
)

_STAMP_COLORS = {
    "Low Risk": "#2F6B4F",
    "Medium Risk": "#A6790A",
    "High Risk": "#C1531B",
    "Critical Risk": "#A32424",
}

_STAMP_TEXT = {
    "Low Risk": "GENUINE",
    "Medium Risk": "CHECK",
    "High Risk": "FAKE",
    "Critical Risk": "FAKE",
}


def _prediction_label(prediction):
    return "Likely a Fake Review" if prediction == 1 else "Looks Like a Genuine Review"


def _render_stamp(risk_level, fraud_probability):
    color = _STAMP_COLORS.get(risk_level, "#A6790A")
    word = _STAMP_TEXT.get(risk_level, "CHECK")
    pct = f"{fraud_probability * 100:.0f}%"

    return f"""
    <div class="stamp-wrap">
        <svg width="150" height="150" viewBox="0 0 150 150" xmlns="http://www.w3.org/2000/svg" style="transform: rotate(-7deg);">
            <circle cx="75" cy="75" r="68" fill="none" stroke="{color}" stroke-width="3.5" />
            <circle cx="75" cy="75" r="58" fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="2,4" />
            <text x="75" y="68" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="800" fill="{color}">{word}</text>
            <text x="75" y="95" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="{color}">{pct} risk</text>
        </svg>
    </div>
    """


def render_verdict(fraud_probability, prediction, risk_level, top_reasons, threshold):
    prediction_label = _prediction_label(prediction)
    top_features = top_reasons["Display Feature"].head(2).tolist()

    if len(top_features) >= 2:
        reason_text = f"{top_features[0]} and {top_features[1]}"
    elif len(top_features) == 1:
        reason_text = top_features[0]
    else:
        reason_text = "behavioral reputation patterns"

    action = get_recommended_action(risk_level)
    confidence_note = get_confidence_note(fraud_probability, threshold)
    color = _STAMP_COLORS.get(risk_level, "#A6790A")
    marker_position = max(0, min(100, fraud_probability * 100))
    stamp_svg = _render_stamp(risk_level, fraud_probability)

    html = f"""
    <style>
        body {{
            margin: 0;
            font-family: Inter, Arial, sans-serif;
            background: transparent;
        }}

        .verdict-card {{
            display: grid;
            grid-template-columns: 170px 1fr;
            gap: 1.4rem;
            align-items: center;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-left: 7px solid {color};
            border-radius: 22px;
            padding: 1.45rem 1.55rem;
            box-shadow: 0 18px 42px rgba(15, 23, 42, 0.10);
        }}

        .stamp-wrap {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .verdict-eyebrow {{
            font-size: 0.82rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 0.35rem;
        }}

        .verdict-headline {{
            color: #0f172a;
            font-size: 2.15rem;
            line-height: 1.08;
            font-weight: 950;
            letter-spacing: -0.04em;
            margin-bottom: 0.65rem;
        }}

        .verdict-summary {{
            color: #475569;
            font-size: 0.98rem;
            line-height: 1.65;
        }}

        .verdict-meta {{
            display: flex;
            gap: 0.6rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }}

        .verdict-meta-item {{
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 999px;
            padding: 0.45rem 0.7rem;
            color: #475569;
            font-size: 0.86rem;
            font-weight: 700;
        }}

        .meter-shell {{
            margin-top: 0.9rem;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 1rem;
        }}

        .meter-track {{
            height: 12px;
            width: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #16a34a 0%, #16a34a 30%, #d97706 30%, #d97706 60%, #ea580c 60%, #ea580c 80%, #dc2626 80%, #dc2626 100%);
            position: relative;
        }}

        .meter-marker {{
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: #111827;
            border: 3px solid #ffffff;
            position: absolute;
            top: -3px;
            transform: translateX(-50%);
            box-shadow: 0 4px 10px rgba(15, 23, 42, 0.25);
        }}

        .meter-labels {{
            display: flex;
            justify-content: space-between;
            margin-top: 0.45rem;
            color: #64748b;
            font-size: 0.78rem;
            font-weight: 750;
        }}

        @media (max-width: 800px) {{
            .verdict-card {{
                grid-template-columns: 1fr;
                text-align: center;
            }}

            .verdict-headline {{
                font-size: 1.75rem;
            }}
        }}
    </style>

    <div class="verdict-card">
        {stamp_svg}
        <div class="verdict-content">
            <div class="verdict-eyebrow" style="color:{color};">{risk_level}</div>
            <div class="verdict-headline">{prediction_label}</div>
            <div class="verdict-summary">
                The strongest signals behind this verdict: <b>{reason_text}</b>.
                {confidence_note}
            </div>
            <div class="verdict-meta">
                <div class="verdict-meta-item">Fake-likelihood score &nbsp;<b>{fraud_probability * 100:.1f}%</b></div>
                <div class="verdict-meta-item">Flag cutoff &nbsp;<b>{float(threshold) * 100:.0f}%</b></div>
                <div class="verdict-meta-item">Suggested action &nbsp;<b>{action['title']}</b></div>
            </div>
        </div>
    </div>

    <div class="meter-shell">
        <div class="meter-track">
            <div class="meter-marker" style="left: {marker_position:.2f}%"></div>
        </div>
        <div class="meter-labels">
            <span>Genuine</span>
            <span>Worth checking</span>
            <span>Likely fake</span>
            <span>Very likely fake</span>
        </div>
    </div>
    """

    components.html(html, height=360, scrolling=False)


def render_recommended_action(risk_level):
    action = get_recommended_action(risk_level)
    steps_html = "".join(f"<li>{step}</li>" for step in action["next_steps"])

    st.markdown(
        f"""
        <div class="action-card">
            <div class="action-kicker">What to do next</div>
            <div class="action-title">{action['title']}</div>
            <div class="action-copy">{action['description']}</div>
            <ul class="action-steps">{steps_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_model_governance(threshold):
    with st.expander("About this verdict — how it works and its limits"):
        st.markdown(
            f"""
            <div class="about-copy">
                VerityIQ compares the fake-likelihood score against a cutoff of <b>{float(threshold):.2f}</b>
                that was tuned on labeled review data to balance catching suspicious reviews against wrongly flagging genuine reviewers.
                <br><br>
                The evidence below comes from <b>SHAP</b>, a method that shows which inputs pushed the score up or down
                for this specific case. It explains the model's reasoning — it does not prove intent. Some signals are
                related to each other, so always weigh the verdict alongside platform policy, reviewer history, and context
                the model cannot see.
            </div>
            """,
            unsafe_allow_html=True,
        )