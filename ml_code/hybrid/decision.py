CNN_CONF_THRESHOLD = 0.75
CLIP_TOP_K = 5

def hybrid_decision(cnn_result, clip_result):
    cnn_label = cnn_result["label"]
    cnn_conf = cnn_result["confidence"]

    clip_top_labels = [d for d, _ in clip_result["top5"][:CLIP_TOP_K]]

    # CNN confident + CLIP agrees
    if cnn_conf >= CNN_CONF_THRESHOLD and cnn_label in clip_top_labels:
        return {
            "final_label": cnn_label,
            "confidence": cnn_conf,
            "source": "cnn",
            "reason": "CNN confident and CLIP agreement"
        }

    # CNN confident but CLIP disagrees → reject CNN
    if cnn_conf >= CNN_CONF_THRESHOLD and cnn_label not in clip_top_labels:
        return {
            "final_label": clip_result["label"],
            "confidence": clip_result["confidence"],
            "source": "open-set",
            "reason": "CNN rejected by CLIP semantic validation"
        }

    # CNN low confidence → open-set
    return {
        "final_label": clip_result["label"],
        "confidence": clip_result["confidence"],
        "source": "open-set",
        "reason": "CNN low confidence"
    }
