import os
import json
from datetime import datetime

EVIDENCE_DIR = "evidence"

os.makedirs(EVIDENCE_DIR, exist_ok=True)
os.makedirs(f"{EVIDENCE_DIR}/audio", exist_ok=True)
os.makedirs(f"{EVIDENCE_DIR}/video", exist_ok=True)
os.makedirs(f"{EVIDENCE_DIR}/metadata", exist_ok=True)

def save_evidence(modality, data, confidence, mission):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    meta = {
        "modality": modality,
        "confidence": confidence,
        "mission_mode": mission,
        "timestamp": timestamp
    }

    # ---- AUDIO EVIDENCE ----
    if modality == "audio":
        audio_path = f"{EVIDENCE_DIR}/audio/audio_{timestamp}.wav"
        with open(audio_path, "wb") as f:
            f.write(data)

        meta["evidence_path"] = audio_path

    # ---- VIDEO EVIDENCE ----
    elif modality == "video":
        frame_path = f"{EVIDENCE_DIR}/video/frame_{timestamp}.jpg"
        data.save(frame_path)
        meta["evidence_path"] = frame_path

    # ---- METADATA ----
    meta_path = f"{EVIDENCE_DIR}/metadata/meta_{timestamp}.json"
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=4)

    return meta
