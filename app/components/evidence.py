import streamlit as st

from utils.labels import CATEGORY_DESCRIPTIONS, FEATURE_CATEGORIES, PLAIN_ENGLISH_SIGNALS


def render_evidence(top_reasons):
    st.markdown('<div class="section-title">Why this verdict</div>', unsafe_allow_html=True)

    top_categories = []
    for feature in top_reasons["Feature"].tolist():
        category = FEATURE_CATEGORIES.get(feature, "Behavioral Signal")
        if category not in top_categories:
            top_categories.append(category)
    chips = "".join(f'<span class="topic-chip">{category}</span>' for category in top_categories[:5])

    st.markdown(
        f"""
        <div class="section-copy">
            The model's top {len(top_reasons)} signals for this case, ranked by how much each one moved the score.
            <div class="chip-row">{chips}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = top_reasons.to_dict("records")
    columns = st.columns(3)

    for index, row in enumerate(cards):
        is_risk_increasing = row["Impact"] > 0
        tag_class = "tag-risk" if is_risk_increasing else "tag-safe"
        tag_label = "Raises suspicion" if is_risk_increasing else "Builds trust"
        plain_text = PLAIN_ENGLISH_SIGNALS.get(
            row["Feature"],
            "This behavioral signal affected the verdict.",
        )

        with columns[index % 3]:
            st.markdown(
                f"""
                <div class="evidence-card">
                    <span class="evidence-tag {tag_class}">{tag_label}</span>
                    <div class="evidence-feature">{row['Display Feature']}</div>
                    <div class="evidence-value">Value: {round(row['Value'], 2)}</div>
                    <div class="evidence-text">{plain_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
