import streamlit as st
from agents.perception_agent import perceive_media
from agents.reasoning_agent import reason_threat
from agents.action_agent import take_action
from utils.explainability import generate_explanation
from utils.logger import log_detection   # ✅ logging added

st.set_page_config(page_title="Aegis-AI", layout="centered")

st.title("🛡️ Aegis-AI: Deepfake Defense Agent")

# Mission context selection
mission_mode = st.selectbox(
    "Select Mission Mode",
    ["Normal Surveillance", "Field Operation", "Critical Mission"]
)

# Media input
uploaded_file = st.file_uploader(
    "Upload Audio / Video File",
    type=["mp4", "avi", "wav", "mp3"]
)

# Analysis trigger
if uploaded_file and st.button("Analyze Media"):
    with st.spinner("Analyzing media using agentic AI..."):
        # Perception
        perception = perceive_media(uploaded_file)

        # Reasoning
        decision = reason_threat(perception, mission_mode)

        # Action
        response = take_action(decision)

        # 🔐 System logging (audit trail)
        log_detection(decision)

    # Output
    st.subheader("🔍 System Decision")
    st.write(response)
    st.write(f"**Modality:** {decision['modality']}")
    st.write(f"**Confidence Score:** {decision['confidence']}")
    st.write(f"**Mission Mode:** {decision['mission']}")

    # Explainability
    st.subheader("🧠 Explainability")
    explanations = generate_explanation(
        decision["confidence"],
        decision["modality"]
    )
    for e in explanations:
        st.write("•", e)
