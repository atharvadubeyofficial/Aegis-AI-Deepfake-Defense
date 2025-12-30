import datetime

LOG_FILE = "logs/detections.log"

def log_detection(decision):
    timestamp = datetime.datetime.utcnow().isoformat()

    log_entry = (
        f"[{timestamp}] | "
        f"Mission: {decision['mission']} | "
        f"Modality: {decision['modality']} | "
        f"Confidence: {decision['confidence']} | "
        f"Decision: {decision['decision']}\n"
    )

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
