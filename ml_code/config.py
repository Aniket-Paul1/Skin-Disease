# ml_code/config.py

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# Project root
# =========================
# ml_code/config.py -> project root is one level up
ROOT = Path(__file__).resolve().parents[1]

# =========================
# Dataset (ALREADY SPLIT)
# =========================
# Structure:
# ml_code/data/
# ├── train/
# └── val/
DATA_DIR = ROOT / "ml_code" / "data"
TRAIN_DIR = DATA_DIR / "train"
VAL_DIR   = DATA_DIR / "val"

# =========================
# Artifacts
# =========================
ARTIFACTS_DIR  = ROOT / "artifacts"
MODELS_DIR     = ARTIFACTS_DIR / "models"
EMBEDDINGS_DIR = ARTIFACTS_DIR / "embeddings"

# =========================
# Models
# =========================
CNN_MODEL = MODELS_DIR / "cnn_balanced_finetuned.h5"
CLIP_PTH  = MODELS_DIR / "skinclip_finetuned.pth"

# Calibration
TEMPERATURE_NPY = MODELS_DIR / "temperature.npy"

# =========================
# Class mappings
# =========================
CLASSES_JSON   = MODELS_DIR / "classes.json"
CLASSES_JOBLIB = MODELS_DIR / "classes.joblib"

# =========================
# Embeddings (for ensemble)
# =========================
TRAIN_EMB = EMBEDDINGS_DIR / "train_embeddings.pkl"
VAL_EMB   = EMBEDDINGS_DIR / "val_embeddings.pkl"

# =========================
# Training / inference params
# =========================
IMG_SIZE     = (224, 224)
BATCH_SIZE  = 16
RANDOM_SEED = 42

# =========================
# (Optional) YOLO placeholders
# =========================
YOLO_DIR        = ROOT / "ml_code" / "detection"
YOLO_MODEL_PTH  = YOLO_DIR / "yolo_lesion.pt"

# =========================
# Sanity checks (fail fast)
# =========================
assert ROOT.exists(), f"ROOT not found: {ROOT}"
assert TRAIN_DIR.exists(), f"TRAIN_DIR not found: {TRAIN_DIR}"
assert VAL_DIR.exists(), f"VAL_DIR not found: {VAL_DIR}"
assert MODELS_DIR.exists(), f"MODELS_DIR not found: {MODELS_DIR}"
assert CNN_MODEL.exists(), f"CNN model not found: {CNN_MODEL}"
assert TEMPERATURE_NPY.exists(), f"Temperature file not found: {TEMPERATURE_NPY}"

# =========================
# Public exports
# =========================
__all__ = [
    "ROOT",
    "DATA_DIR", "TRAIN_DIR", "VAL_DIR",
    "ARTIFACTS_DIR", "MODELS_DIR", "EMBEDDINGS_DIR",
    "CNN_MODEL", "CLIP_PTH", "TEMPERATURE_NPY",
    "CLASSES_JSON", "CLASSES_JOBLIB",
    "TRAIN_EMB", "VAL_EMB",
    "IMG_SIZE", "BATCH_SIZE", "RANDOM_SEED",
    "YOLO_DIR", "YOLO_MODEL_PTH",
]