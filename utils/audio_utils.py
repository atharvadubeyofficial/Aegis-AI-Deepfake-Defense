import librosa
import soundfile as sf
import numpy as np
import tempfile

def extract_suspicious_audio(audio_path, scores, threshold=0.6):
    if not scores:
        return None

    idx = np.argmax(scores)
    if scores[idx] < threshold:
        return None

    y, sr = librosa.load(audio_path, sr=16000)
    start = idx * 512
    end = start + 16000

    suspicious = y[start:end]

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp.name, suspicious, sr)
    return temp.name
