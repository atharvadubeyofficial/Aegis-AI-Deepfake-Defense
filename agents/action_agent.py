def take_action(decision):
    if decision["decision"] == "Threat":
        return "🚨 Threat Detected. Immediate Alert Triggered."
    else:
        return "✅ Media Verified as Authentic."
