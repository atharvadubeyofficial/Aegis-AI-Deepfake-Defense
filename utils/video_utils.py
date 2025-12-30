def extract_flagged_frame(video_path, frame_scores, threshold=0.6):
    """
    Returns most suspicious frame
    """
    if not frame_scores:
        return None

    flagged = max(frame_scores, key=lambda x: x[0])

    if flagged[0] > threshold:
        return flagged[1]  # numpy frame

    return None
