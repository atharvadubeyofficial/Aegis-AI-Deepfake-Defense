import streamlit as st
from agents.perception_agent import perceive_media
from agents.reasoning_agent import reason_threat
from agents.action_agent import take_action
from utils.explainability import generate_explanation
from utils.logger import log_detection

st.set_page_config(page_title="Aegis-AI", layout="centered")

st.title("🛡️ Aegis-AI: Deepfake Defense Agent")

mission_mode = st.selectbox(
    "Select Mission Mode",
    ["Normal Surveillance", "Field Operation", "Critical Mission"]
)

uploaded_file = st.file_uploader(
    "Upload Audio / Video File",
    type=["mp4", "avi", "wav", "mp3"]
)

if uploaded_file and st.button("Analyze Media"):
    with st.spinner("Analyzing media using agentic AI..."):
        perception = perceive_media(uploaded_file)
        decision = reason_threat(perception, mission_mode)
        response = take_action(decision)
        log_detection(decision)

    # 🧠 Decision
    st.subheader("🔍 System Decision")
    st.write(response)

    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence", decision["confidence"])
    col2.metric("Threshold", decision["threshold"])
    col3.metric("Mission", decision["mission"])

    # 🧾 Explainability
    st.subheader("🧠 Explainability")
    explanations = generate_explanation(
        decision["confidence"],
        decision["modality"]
    )
    for e in explanations:
        st.write("•", e)

    # 🧪 Evidence Preview (🔥 BIG IMPACT)
    if decision["decision"] == "Threat" and decision.get("evidence") is not None:
        st.subheader("📌 Captured Evidence")

        if decision["modality"] == "video":
            st.image(decision["evidence"], caption="Flagged Frame")

        elif decision["modality"] == "audio":
            st.audio(decision["evidence"])
