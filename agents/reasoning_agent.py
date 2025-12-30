def reason_threat(result, mission_mode):
    threshold = {
        "Normal Surveillance": 0.7,
        "Field Operation": 0.4,
        "Critical Mission": 0.25
    }

    decision = result["confidence"] > threshold[mission_mode]
    return {
        "decision": "Threat" if decision else "Safe",
        "confidence": result["confidence"],
        "mission": mission_mode
    }
