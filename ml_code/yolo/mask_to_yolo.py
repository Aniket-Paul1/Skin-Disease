import cv2
import os
import numpy as np
from tqdm import tqdm

IMG_DIR  = "ml_code/yolo/images/train"
MASK_DIR = "external_datasets/isic2018/masks"
LBL_DIR  = "ml_code/yolo/labels/train"

os.makedirs(LBL_DIR, exist_ok=True)

for img_name in tqdm(os.listdir(IMG_DIR)):
    if not img_name.lower().endswith(".jpg"):
        continue

    mask_name = img_name.replace(".jpg", "_segmentation.png")
    mask_path = os.path.join(MASK_DIR, mask_name)

    if not os.path.exists(mask_path):
        continue

    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    h, w = mask.shape

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        continue

    cnt = max(contours, key=cv2.contourArea)
    x, y, bw, bh = cv2.boundingRect(cnt)

    xc = (x + bw / 2) / w
    yc = (y + bh / 2) / h
    bw /= w
    bh /= h

    with open(
        os.path.join(LBL_DIR, img_name.replace(".jpg", ".txt")), "w"
    ) as f:
        f.write(f"0 {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

print("YOLO labels generated.")
