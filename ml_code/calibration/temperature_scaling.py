# ml_code/calibration/temperature_scaling.py

import numpy as np
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from scipy.optimize import minimize

from ml_code.config import VAL_DIR, IMG_SIZE, BATCH_SIZE

# -------------------------------------------------
# CORRECT MODEL PATH (matches your folder)
# -------------------------------------------------
MODEL_PATH = Path("artifacts/models/cnn_balanced_finetuned.h5")
TEMP_PATH  = Path("artifacts/models/temperature.npy")

assert MODEL_PATH.exists(), f"Model not found at {MODEL_PATH}"

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
model = load_model(MODEL_PATH, compile=False)
print("Loaded model:", MODEL_PATH)

# -------------------------------------------------
# LOAD VALIDATION DATA
# -------------------------------------------------
val_gen = ImageDataGenerator(rescale=1.0 / 255)

val_data = val_gen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False,
)

y_true = val_data.classes
num_classes = val_data.num_classes

print(f"Validation samples: {len(y_true)}")
print(f"Classes: {num_classes}")

# -------------------------------------------------
# GET PREDICTIONS (LOGITS)
# -------------------------------------------------
probs = model.predict(val_data, verbose=1)

# Convert probabilities → logits safely
logits = np.log(np.clip(probs, 1e-8, 1.0))

# -------------------------------------------------
# NEGATIVE LOG LIKELIHOOD
# -------------------------------------------------
def nll_loss(T):
    T = T[0]
    scaled_logits = logits / T
    exp_logits = np.exp(scaled_logits)
    scaled_probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)
    return -np.mean(np.log(scaled_probs[np.arange(len(y_true)), y_true]))

# -------------------------------------------------
# OPTIMIZE TEMPERATURE
# -------------------------------------------------
opt = minimize(
    nll_loss,
    x0=[1.0],
    bounds=[(0.5, 5.0)],
    method="L-BFGS-B",
)

T_opt = float(opt.x[0])
print(f"\n✅ Optimal Temperature: {T_opt:.3f}")

# -------------------------------------------------
# SAVE TEMPERATURE
# -------------------------------------------------
TEMP_PATH.parent.mkdir(parents=True, exist_ok=True)
np.save(TEMP_PATH, T_opt)

print("Temperature saved to:", TEMP_PATH)
