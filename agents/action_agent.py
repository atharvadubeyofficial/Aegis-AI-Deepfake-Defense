def take_action(decision):
    if decision["decision"] == "Threat":
        if decision["mission"] == "Critical Mission":
            return "🚨 CRITICAL ALERT: Media flagged as deepfake. Mission integrity compromised."
        return "⚠️ Alert: Potential deepfake detected. Manual verification advised."
    else:
        return "✅ Media verified as authentic. No action required."
