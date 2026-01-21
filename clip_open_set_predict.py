import torch
import open_clip
from PIL import Image
import sys

# Load CLIP model
model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32", pretrained="laion2b_s34b_b79k"
)
tokenizer = open_clip.get_tokenizer("ViT-B-32")
model.eval()

# OPEN-SET DISEASE LIST (YOU CAN EXTEND THIS)
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

def predict(image_path):
    image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0)

    texts = [f"a clinical photograph of {disease}" for disease in DISEASES]
    text_tokens = tokenizer(texts)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_tokens)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        similarity = (image_features @ text_features.T).softmax(dim=-1)

    probs = similarity[0].tolist()
    ranked = sorted(zip(DISEASES, probs), key=lambda x: x[1], reverse=True)

    top = ranked[0]
    return {
        "label": top[0],
        "confidence": round(top[1], 3),
        "top5": [(d, round(p, 3)) for d, p in ranked[:5]]
    }

if __name__ == "__main__":
    img = sys.argv[1]
    result = predict(img)
    print(result)
