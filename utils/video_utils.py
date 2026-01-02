def extract_flagged_frame(video_path, frame_scores, threshold=0.6):
    """
    Returns most suspicious frame (only if frame-wise scores exist)
    """

    # 🔒 Safety: frame_scores must be list of tuples
    if not isinstance(frame_scores, list):
        return None

    if len(frame_scores) == 0:
        return None

    flagged = max(frame_scores, key=lambda x: x[0])

    if flagged[0] > threshold:
        return flagged[1]  # numpy / PIL frame

    return None
