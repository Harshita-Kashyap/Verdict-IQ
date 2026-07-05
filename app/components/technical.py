import matplotlib.pyplot as plt
import streamlit as st

from services.explanation_service import (
    create_compact_shap_chart,
    format_input_summary,
    style_summary_table,
)


def render_technical_appendix(shap_values_fake, input_df):
    with st.expander("See the full chart and raw numbers behind this verdict"):
        st.markdown(
            """
            <div class="section-copy" style="margin-bottom: 0.8rem;">
                A chart of every signal's pull on the score, plus the raw values the model actually used.
            </div>
            """,
            unsafe_allow_html=True,
        )

        fig = create_compact_shap_chart(shap_values_fake, input_df)
        st.pyplot(fig, width="stretch")
        plt.close(fig)

        st.markdown("<br>", unsafe_allow_html=True)
        summary_df = format_input_summary(input_df)
        st.dataframe(style_summary_table(summary_df), width="stretch", hide_index=True)
