import numpy as np
import joblib
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from ml_code.config import (
    TRAIN_DIR, VAL_DIR, IMG_SIZE, BATCH_SIZE,
    CNN_MODEL, TEMPERATURE_NPY, EMBEDDINGS_DIR
)

EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)

# Load model and temperature
model = load_model(CNN_MODEL, compile=False)
T = float(np.load(TEMPERATURE_NPY))

def softmax(x):
    e = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

def extract(dir_path, out_path):
    gen = ImageDataGenerator(rescale=1./255)
    data = gen.flow_from_directory(
        dir_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        shuffle=False,
    )
    probs = model.predict(data, verbose=1)
    logits = np.log(np.clip(probs, 1e-8, 1.0))
    calibrated = softmax(logits / T)
    joblib.dump((calibrated, data.classes), out_path)
    print(f"Saved: {out_path}")

extract(TRAIN_DIR, EMBEDDINGS_DIR / "train_probs.joblib")
extract(VAL_DIR,   EMBEDDINGS_DIR / "val_probs.joblib")
