import streamlit as st


def render_sidebar(threshold):
    st.sidebar.markdown(
        """
        <div class="side-mark">Verdict<span>IQ</span></div>
        <div class="side-tagline">A quick way to check if a review looks genuine or fake, based on the reviewer's behavior — not the words they wrote.</div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="side-block">
            <div class="side-label">How to read the score</div>
            <div class="side-row"><span><span class="dot dot-low"></span>0–29%</span><span>Looks genuine</span></div>
            <div class="side-row"><span><span class="dot dot-medium"></span>30–59%</span><span>Worth a second look</span></div>
            <div class="side-row"><span><span class="dot dot-high"></span>60–79%</span><span>Likely fake</span></div>
            <div class="side-row"><span><span class="dot dot-critical"></span>80–100%</span><span>Very likely fake</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        f"""
        <div class="side-block">
            <div class="side-label">What's under the hood</div>
            <div class="side-note">
                A machine learning model trained on real Yelp reviewer patterns. It flags a review once its fake-likelihood score
                crosses <b>{float(threshold) * 100:.0f}%</b> — a cutoff tuned for the best balance of catching fakes without
                over-flagging genuine reviewers.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="side-block">
            <div class="side-label">Good to know</div>
            <div class="side-note">
                This is a decision-support tool, not a final judgment. It looks at reviewer history and engagement patterns,
                so treat the verdict as a strong hint worth checking — not absolute proof.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
