import torch
import open_clip
from PIL import Image

model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32", pretrained="laion2b_s34b_b79k"
)
tokenizer = open_clip.get_tokenizer("ViT-B-32")
model.eval()

DISEASES = [
    "acne",
    "rosacea",
    "eczema",
    "psoriasis",
    "vitiligo",
    "basal cell carcinoma",
    "melanoma",
    "hives (urticaria)",
    "athlete's foot (tinea pedis)",
    "nail fungus (onychomycosis)",
    "contact dermatitis",
    "seborrheic dermatitis",
    "ringworm",
    "healthy skin"
]

def clip_predict(image_path):
    image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0)

    texts = [f"a clinical photograph of {d}" for d in DISEASES]
    text_tokens = tokenizer(texts)

    with torch.no_grad():
        img_feat = model.encode_image(image)
        txt_feat = model.encode_text(text_tokens)

        img_feat /= img_feat.norm(dim=-1, keepdim=True)
        txt_feat /= txt_feat.norm(dim=-1, keepdim=True)

        similarity = (img_feat @ txt_feat.T)[0]

    scores = similarity.softmax(dim=0).tolist()
    ranked = sorted(zip(DISEASES, scores), key=lambda x: x[1], reverse=True)

    return {
        "label": ranked[0][0],
        "confidence": ranked[0][1],   # DO NOT compare numerically
        "top5": ranked[:5]
    }
