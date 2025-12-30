import tempfile
from models.deepfake_model import analyze_video
from models.audio_deepfake_model import analyze_audio

def perceive_media(uploaded_file):
    suffix = uploaded_file.name.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as temp:
        temp.write(uploaded_file.read())
        path = temp.name

    if suffix in ["mp4", "avi", "mov"]:
        confidence = analyze_video(path)
        modality = "Video"

    elif suffix in ["wav", "mp3"]:
        confidence = analyze_audio(path)
        modality = "Audio"

    else:
        raise ValueError("Unsupported media format")

    return {
        "confidence": float(confidence),
        "modality": modality
    }
