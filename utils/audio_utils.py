import tempfile

def save_audio_temp(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(uploaded_file.read())
        return temp.name
