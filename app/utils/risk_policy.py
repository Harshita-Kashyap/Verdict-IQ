def get_risk_level(probability):
    percentage = probability * 100
    if percentage < 30:
        return "Low Risk"
    if percentage < 60:
        return "Medium Risk"
    if percentage < 80:
        return "High Risk"
    return "Critical Risk"


def get_risk_css_class(risk_level):
    return {
        "Low Risk": "risk-low",
        "Medium Risk": "risk-medium",
        "High Risk": "risk-high",
        "Critical Risk": "risk-critical",
    }.get(risk_level, "risk-medium")


def get_risk_message(risk_level):
    return {
        "Low Risk": "The reviewer's behavior looks like that of a genuine customer.",
        "Medium Risk": "A few patterns here don't quite add up. Nothing alarming yet, but worth a second glance.",
        "High Risk": "This reviewer's behavior closely matches known fake-review patterns.",
        "Critical Risk": "This review shows strong, multiple signs of being fake.",
    }.get(risk_level, "This review should be checked carefully.")


def get_recommended_action(risk_level):
    return {
        "Low Risk": {
            "title": "No action needed",
            "severity": "Normal",
            "description": "This review can be trusted at face value. No follow-up is necessary.",
            "next_steps": ["Treat the review as genuine", "No further checks needed"],
        },
        "Medium Risk": {
            "title": "Keep an eye on it",
            "severity": "Light check",
            "description": "Nothing conclusive, but a couple of details stand out. A quick look at the reviewer's profile would settle it.",
            "next_steps": ["Skim the reviewer's other reviews", "Compare against the business's typical reviews"],
        },
        "High Risk": {
            "title": "Take a closer look",
            "severity": "Recommended",
            "description": "Several behavioral signals line up with fake-review patterns. Worth a manual review before deciding.",
            "next_steps": ["Check the reviewer's posting history", "Look for similar reviews posted around the same time"],
        },
        "Critical Risk": {
            "title": "Flag this review",
            "severity": "Urgent",
            "description": "Multiple strong signals point to a fake review. This is a good candidate to flag or report.",
            "next_steps": ["Flag the review for removal", "Report the account if the pattern repeats elsewhere"],
        },
    }.get(
        risk_level,
        {
            "title": "Review manually",
            "severity": "Unknown",
            "description": "Additional review is recommended.",
            "next_steps": ["Review manually"],
        },
    )


def get_threshold_margin(probability, threshold):
    return probability - float(threshold)


def get_threshold_status(probability, threshold):
    margin = get_threshold_margin(probability, threshold)
    return "Above the flag cutoff" if margin >= 0 else "Below the flag cutoff", margin


def get_confidence_note(probability, threshold):
    margin = abs(get_threshold_margin(probability, threshold))
    if margin < 0.05:
        return "This one sits close to the cutoff, so treat it as a borderline call."
    if margin < 0.15:
        return "The score sits a moderate distance from the cutoff, which adds some confidence."
    return "The score sits clearly away from the cutoff, which makes this a fairly confident call."
