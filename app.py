import streamlit as st
from agents.perception_agent import perceive_media
from agents.reasoning_agent import reason_threat
from agents.action_agent import take_action

st.set_page_config(page_title="Aegis-AI", layout="centered")

st.title("🛡️ Aegis-AI: Deepfake Defense Agent")

mission_mode = st.selectbox(
    "Select Mission Mode",
    ["Normal Surveillance", "Field Operation", "Critical Mission"]
)

uploaded_file = st.file_uploader(
    "Upload Audio / Video File",
    type=["mp4", "wav", "mp3"]
)

if uploaded_file and st.button("Analyze Media"):
    perception_result = perceive_media(uploaded_file)
    decision = reason_threat(perception_result, mission_mode)
    response = take_action(decision)

    st.subheader("Analysis Result")
    st.write(response)
