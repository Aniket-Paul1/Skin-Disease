import cv2
import numpy as np
from ultralytics import YOLO

YOLO_MODEL_PATH = "ml_code/detection/yolo_lesion.pt"

yolo = YOLO(YOLO_MODEL_PATH)

def crop_lesion(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image could not be loaded")

    results = yolo(img, conf=0.25, verbose=False)[0]

    if results.boxes is None or len(results.boxes) == 0:
        # Fallback: return original image
        return img

    # Take the largest box (safest for lesions)
    boxes = results.boxes.xyxy.cpu().numpy()
    areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    box = boxes[areas.argmax()]

    x1, y1, x2, y2 = map(int, box)

    h, w, _ = img.shape
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w, x2), min(h, y2)

    crop = img[y1:y2, x1:x2]

    if crop.size == 0:
        return img

    return crop
