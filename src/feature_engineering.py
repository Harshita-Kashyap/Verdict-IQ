import numpy as np


def calculate_engineered_features(raw_inputs):
    """
    Calculate engineered behavioral features used by the fake review detection model.

    Important:
    This function must stay consistent with the feature engineering logic used
    during model training.
    """

    rating_deviation = abs(raw_inputs["rating"] - raw_inputs["restaurantRating"])

    reviewer_engagement_ratio = (
        raw_inputs["usefulCount"]
        + raw_inputs["coolCount"]
        + raw_inputs["funnyCount"]
        + raw_inputs["complimentCount"]
    ) / (raw_inputs["reviewCount"] + 1)

    reviewer_social_reach = raw_inputs["friendCount"] + raw_inputs["fanCount"]

    reviewer_helpfulness_ratio = raw_inputs["usefulCount"] / (
        raw_inputs["reviewCount"] + 1
    )

    reviewer_activity_level = np.log1p(raw_inputs["reviewCount"])

    return {
        "rating_deviation": rating_deviation,
        "reviewer_engagement_ratio": reviewer_engagement_ratio,
        "reviewer_social_reach": reviewer_social_reach,
        "reviewer_helpfulness_ratio": reviewer_helpfulness_ratio,
        "reviewer_activity_level": reviewer_activity_level,
    }