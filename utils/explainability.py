def generate_explanation(confidence, modality):
    reasons = []

    if modality == "Video" and confidence > 0.5:
        reasons.append("Abnormal facial motion patterns detected across frames")

    if modality == "Audio" and confidence > 0.5:
        reasons.append("Spectral and MFCC inconsistencies indicate synthetic voice")

    if not reasons:
        reasons.append("No significant deepfake indicators detected")

    return reasons
