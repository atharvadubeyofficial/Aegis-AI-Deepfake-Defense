def fuse_confidence(video_conf=None, audio_conf=None, mission="Normal Surveillance"):
    weights = {
        "Normal Surveillance": (0.6, 0.4),
        "Field Operation": (0.5, 0.5),
        "Critical Mission": (0.4, 0.6)
    }

    wv, wa = weights[mission]

    if video_conf is None:
        return audio_conf
    if audio_conf is None:
        return video_conf

    return wv * video_conf + wa * audio_conf


def reason_threat(perception, mission_mode):
    threshold = {
        "Normal Surveillance": 0.7,
        "Field Operation": 0.4,
        "Critical Mission": 0.25
    }

    final_conf = fuse_confidence(
        video_conf=perception.get("video_conf"),
        audio_conf=perception.get("audio_conf"),
        mission=mission_mode
    )

    decision = final_conf > threshold[mission_mode]

    return {
        "decision": "Threat" if decision else "Safe",
        "final_confidence": round(final_conf, 3),
        "mission": mission_mode
    }
