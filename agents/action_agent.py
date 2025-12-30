from utils.evidence_manager import save_evidence

def take_action(decision):
    """
    decision dict must contain:
    - decision: Threat / Safe
    - confidence
    - modality
    - mission
    - evidence (optional but required if Threat)
    """

    if decision["decision"] == "Threat":

        # 🔐 Evidence capture (ONLY when threat)
        if "evidence" in decision and decision["evidence"] is not None:
            save_evidence(
                modality=decision["modality"],
                data=decision["evidence"],
                confidence=decision["confidence"],
                mission=decision["mission"]
            )

        # 🎯 Mission-aware response
        if decision["mission"] == "Critical Mission":
            return "🚨 CRITICAL ALERT: Deepfake confirmed. Evidence captured. Mission integrity compromised."

        return "⚠️ Alert: Potential deepfake detected. Evidence stored for verification."

    # ✅ SAFE CASE
    return "✅ Media verified as authentic. No action required."
