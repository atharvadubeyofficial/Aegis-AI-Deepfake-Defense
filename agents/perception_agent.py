import tempfile
from models.deepfake_model import analyze_video

def perceive_media(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_file.read())
        video_path = temp.name

    confidence = analyze_video(video_path)

    return {
        "confidence": confidence,
        "label": "Deepfake" if confidence > 0.5 else "Authentic"
    }
