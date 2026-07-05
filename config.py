import os

# Get project root (fake-review-detector/)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Standard paths
DATA_PATH = os.path.join(PROJECT_ROOT, "data")
RAW_PATH = os.path.join(DATA_PATH, "raw")
CLEANED_PATH = os.path.join(DATA_PATH, "cleaned")
PROCESSED_PATH = os.path.join(DATA_PATH, "processed")

MODEL_PATH = os.path.join(PROJECT_ROOT, "models")
NOTEBOOKS_PATH = os.path.join(PROJECT_ROOT, "notebooks")