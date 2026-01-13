import joblib
import numpy as np
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

from ml_code.config import EMBEDDINGS_DIR, MODELS_DIR

MODELS_DIR.mkdir(parents=True, exist_ok=True)

X_train, y_train = joblib.load(EMBEDDINGS_DIR / "train_probs.joblib")
X_val,   y_val   = joblib.load(EMBEDDINGS_DIR / "val_probs.joblib")

# Random Forest
rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)

# XGBoost
xgb = XGBClassifier(
    n_estimators=400,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9,
    eval_metric="mlogloss",
    random_state=42
)
xgb.fit(X_train, y_train)

# Evaluate
rf_acc  = accuracy_score(y_val, rf.predict(X_val))
xgb_acc = accuracy_score(y_val, xgb.predict(X_val))

print(f"RF Val Acc : {rf_acc:.3f}")
print(f"XGB Val Acc: {xgb_acc:.3f}")

# Save
joblib.dump(rf,  MODELS_DIR / "rf_ensemble.joblib")
joblib.dump(xgb, MODELS_DIR / "xgb_ensemble.joblib")

print("Ensemble models saved.")
