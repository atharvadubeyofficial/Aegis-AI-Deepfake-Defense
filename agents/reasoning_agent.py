def reason_threat(perception, mission_mode):
    thresholds = {
        "Normal Surveillance": 0.7,
        "Field Operation": 0.4,
        "Critical Mission": 0.25
    }

    confidence = perception["confidence"]
    modality = perception["modality"]
    threshold = thresholds[mission_mode]

    decision = confidence >= threshold

    return {
        "decision": "Threat" if decision else "Safe",
        "confidence": round(confidence, 3),
        "threshold": threshold,
        "modality": modality,
        "mission": mission_mode,
        "evidence": perception.get("evidence")  #  IMPORTANT
    }
