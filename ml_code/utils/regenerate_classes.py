import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from ml_code.config import TRAIN_DIR, IMG_SIZE, BATCH_SIZE, MODELS_DIR

datagen = ImageDataGenerator(rescale=1.0 / 255)

gen = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

MODELS_DIR.mkdir(parents=True, exist_ok=True)

with open(MODELS_DIR / "classes.json", "w") as f:
    json.dump(gen.class_indices, f, indent=2)

print("classes.json regenerated successfully:")
print(gen.class_indices)
