import textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils.labels import FEATURE_LABELS, FEATURE_EXPLANATIONS


def get_shap_values_for_fake_class(explainer, input_df):
    shap_values = explainer.shap_values(input_df)

    if isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
        return shap_values[:, :, 1]

    if isinstance(shap_values, list):
        return shap_values[1]

    return shap_values


def get_top_explanation_signals(input_df, shap_values_fake, top_n=5):
    explanation_df = pd.DataFrame(
        {
            "Feature": input_df.columns,
            "Display Feature": [FEATURE_LABELS.get(col, col) for col in input_df.columns],
            "Value": input_df.iloc[0].values,
            "Impact": shap_values_fake[0],
        }
    )
    explanation_df["Absolute Impact"] = explanation_df["Impact"].abs()
    return explanation_df.sort_values(by="Absolute Impact", ascending=False).head(top_n)


def create_compact_shap_chart(shap_values_fake, input_df, top_n=8):
    values = shap_values_fake[0]
    feature_names = [FEATURE_LABELS.get(col, col) for col in input_df.columns]

    chart_df = pd.DataFrame(
        {"Feature": feature_names, "Impact": values, "AbsImpact": np.abs(values)}
    ).sort_values("AbsImpact", ascending=False).head(top_n)

    chart_df = chart_df.sort_values("Impact", ascending=True)
    chart_df["Feature"] = chart_df["Feature"].apply(lambda x: "\n".join(textwrap.wrap(x, 24)))

    bar_colors = ["#B5471B" if v > 0 else "#2F6B4F" for v in chart_df["Impact"]]

    plt.rcParams["font.family"] = "DejaVu Sans"
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    ax.barh(chart_df["Feature"], chart_df["Impact"], color=bar_colors, height=0.62, edgecolor="none")
    ax.axvline(0, linewidth=1, color="#5B5A55")
    ax.set_xlabel("Effect on fake-review score  (right = more suspicious, left = more trustworthy)", fontsize=9, color="#5B5A55")
    ax.set_ylabel("")
    ax.set_title("What pushed the score up or down", fontsize=12, fontweight="bold", color="#1B1B1F", loc="left")
    ax.tick_params(axis="y", labelsize=9, colors="#1B1B1F")
    ax.tick_params(axis="x", labelsize=8.5, colors="#5B5A55")
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#E6E0D2")
    ax.grid(axis="x", color="#E6E0D2", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


def format_input_summary(input_df):
    summary_df = input_df.T.reset_index()
    summary_df.columns = ["Feature", "Value"]
    summary_df["Feature Name"] = summary_df["Feature"].map(FEATURE_LABELS).fillna(summary_df["Feature"])
    summary_df["Meaning"] = summary_df["Feature"].map(FEATURE_EXPLANATIONS).fillna("-")
    summary_df["Value"] = summary_df["Value"].apply(lambda x: round(float(x), 3))
    return summary_df[["Feature Name", "Value", "Meaning"]]


def style_summary_table(summary_df):
    return (
        summary_df.style
        .set_properties(
            **{
                "text-align": "center",
                "padding": "10px 14px",
                "font-size": "14px",
                "white-space": "normal",
            }
        )
        .set_table_styles(
            [
                {"selector": "th", "props": [("text-align", "center"), ("font-weight", "800"), ("color", "#1B1B1F"), ("background-color", "#FBF8F1"), ("padding", "11px 14px"), ("border-bottom", "1px solid #E6E0D2")]},
                {"selector": "td", "props": [("border-bottom", "1px solid #E6E0D2")]},
                {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#FBF8F1")]},
            ]
        )
    )
