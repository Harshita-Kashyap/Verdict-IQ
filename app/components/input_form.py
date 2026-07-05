import streamlit as st


def render_input_form():
    st.markdown('<div class="section-title">Check a review</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-copy">
            Fill in what you know about the review and the reviewer. The more accurate the details, the more reliable the verdict.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("review_check_form"):
        st.markdown('<div class="form-group-label">The review itself</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        rating = col1.slider(
            "Star rating given", 1.0, 5.0, 5.0, 0.5,
            help="The star rating the reviewer gave.",
        )
        restaurant_rating = col2.slider(
            "Business's usual rating", 1.0, 5.0, 4.0, 0.1,
            help="The business's average rating from all reviews. A big gap from this review's rating can be a red flag.",
        )
        review_word_count = col3.number_input(
            "Words in the review", min_value=0, value=50,
            help="Very short, generic reviews are more often fake.",
        )
        review_useful_count = col4.number_input(
            "'Useful' votes on this review", min_value=0, value=0,
            help="How many other users marked this specific review as useful.",
        )

        st.markdown('<div class="form-group-label">The reviewer&rsquo;s track record</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="form-group-hint">A brand-new account with one glowing review behaves very differently from a long-time regular reviewer.</div>',
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns(3)
        review_count = col1.number_input(
            "Reviews written in total", min_value=0, value=1,
            help="How many reviews this account has ever posted.",
        )
        reviewer_account_age_days = col2.number_input(
            "Account age (in days)", min_value=0, value=30,
            help="How long ago the account was created.",
        )
        tip_count = col3.number_input(
            "Tips written", min_value=0, value=0,
            help="Short tips are a lighter-weight form of activity than full reviews.",
        )

        st.markdown('<div class="form-group-label">Reputation in the community</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="form-group-hint">Real reviewers usually build up a visible social footprint over time — friends, fans, and votes from other users.</div>',
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns(3)
        friend_count = col1.number_input("Friends on the platform", min_value=0, value=0)
        fan_count = col1.number_input("Fans / followers", min_value=0, value=0)

        useful_count = col2.number_input("Total 'useful' votes received", min_value=0, value=0)
        compliment_count = col2.number_input("Compliments received", min_value=0, value=0)

        cool_count = col3.number_input("Total 'cool' votes received", min_value=0, value=0)
        funny_count = col3.number_input("Total 'funny' votes received", min_value=0, value=0)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Get the verdict", width="stretch")

    raw_inputs = {
        "rating": rating,
        "restaurantRating": restaurant_rating,
        "friendCount": friend_count,
        "reviewCount": review_count,
        "reviewUsefulCount": review_useful_count,
        "usefulCount": useful_count,
        "coolCount": cool_count,
        "funnyCount": funny_count,
        "complimentCount": compliment_count,
        "tipCount": tip_count,
        "fanCount": fan_count,
        "reviewer_account_age_days": reviewer_account_age_days,
        "review_word_count": review_word_count,
    }

    return raw_inputs, submitted
