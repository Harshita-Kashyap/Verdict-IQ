from pathlib import Path

APP_TITLE = "Verdict IQ"
APP_SUBTITLE = "Paste in a review's details and get a clear, evidence-backed verdict on whether it's genuine or fake."

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_random_forest_model.pkl"
FEATURE_PATH = BASE_DIR / "models" / "final_feature_list.pkl"
THRESHOLD_PATH = BASE_DIR / "models" / "final_threshold.pkl"

MODEL_NAME = "Random Forest Classifier"
MODEL_VERSION = "v1.0"
PRIMARY_SIGNAL_TYPE = "Behavioral Reputation Analytics"
