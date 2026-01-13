import json
import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from ml_code.config import (
    CNN_MODEL,
    CLASSES_JSON,
    IMG_SIZE
)

from ml_code.open_set.clip_predict import clip_predict
from ml_code.hybrid.decision import hybrid_decision


# -----------------------------
# Load CNN + classes (ONCE)
# -----------------------------
print("Loading CNN model...")
cnn_model = load_model(CNN_MODEL, compile=False)

print("Loading class mappings...")
with open(CLASSES_JSON) as f:
    class_map = json.load(f)
inv_class_map = {v: k for k, v in class_map.items()}


# -----------------------------
# CNN prediction
# -----------------------------
def cnn_predict(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = cnn_model.predict(x)[0]
    idx = int(np.argmax(preds))
    conf = float(preds[idx])

    return {
        "label": inv_class_map[idx],
        "confidence": conf
    }


# -----------------------------
# FULL PIPELINE
# -----------------------------
def predict_image(img_path):
    # 1. CNN prediction
    cnn_result = cnn_predict(img_path)

    # 2. CLIP open-set prediction
    clip_result = clip_predict(img_path)

    # 3. Hybrid decision
    final = hybrid_decision(cnn_result, clip_result)

    # --------------------------------------------------
    # Confidence source control (NO UI logic here)
    # --------------------------------------------------
    if final["source"] == "cnn":
        final_confidence = cnn_result["confidence"]
    else:
        final_confidence = clip_result["confidence"]

    return {
        "final_label": final["final_label"],
        "confidence": final_confidence,
        "source": final["source"],
        "reason": final["reason"],
        "cnn": cnn_result,
        "clip_top5": clip_result["top5"]
    }


# -----------------------------
# CLI support
# -----------------------------
if __name__ == "__main__":
    img = sys.argv[1]
    result = predict_image(img)
    print(json.dumps(result, indent=2))
