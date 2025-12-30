def generate_explanation(video_conf=None, audio_conf=None):
    reasons = []

    if video_conf and video_conf > 0.5:
        reasons.append("Facial motion inconsistency detected")

    if audio_conf and audio_conf > 0.5:
        reasons.append("Spectral anomalies found in audio signal")

    if not reasons:
        reasons.append("No significant manipulation patterns detected")

    return reasons
