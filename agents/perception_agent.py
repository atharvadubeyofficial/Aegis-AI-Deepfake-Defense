import tempfile
from models.deepfake_model import analyze_video
from models.audio_deepfake_model import analyze_audio

def perceive_media(uploaded_file):
    suffix = uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as temp:
        temp.write(uploaded_file.read())
        path = temp.name

    if suffix in ["mp4", "avi"]:
        confidence = analyze_video(path)
        modality = "Video"
    else:
        confidence = analyze_audio(path)
        modality = "Audio"

    return {
        "confidence": confidence,
        "modality": modality
    }
