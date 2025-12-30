import tempfile
import cv2
import numpy as np
from models.deepfake_model import analyze_video
from models.audio_deepfake_model import analyze_audio
from utils.video_utils import extract_flagged_frame
from utils.audio_utils import extract_suspicious_audio

def perceive_media(uploaded_file):
    suffix = uploaded_file.name.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as temp:
        temp.write(uploaded_file.read())
        path = temp.name

    # 🎥 VIDEO
    if suffix in ["mp4", "avi", "mov"]:
        confidence, frame_scores = analyze_video(path)
        flagged_frame = extract_flagged_frame(path, frame_scores)

        return {
            "confidence": confidence,
            "modality": "video",
            "evidence": flagged_frame
        }

    # 🔊 AUDIO
    elif suffix in ["wav", "mp3"]:
        confidence, segment_scores = analyze_audio(path)
        suspicious_audio = extract_suspicious_audio(path, segment_scores)

        return {
            "confidence": confidence,
            "modality": "audio",
            "evidence": suspicious_audio
        }

    else:
        raise ValueError("Unsupported media format")
