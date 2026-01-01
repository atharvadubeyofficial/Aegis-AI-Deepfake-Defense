import torch
import timm
import torchvision.transforms as transforms
import cv2
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN

# -----------------------------
# Device (Edge-aware)
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# REAL pretrained backbone
# -----------------------------
model = timm.create_model("xception", pretrained=True)
model.eval()
model.to(device)

# -----------------------------
# Face detector (edge-capable)
# -----------------------------
mtcnn = MTCNN(keep_all=False, device=device)

# -----------------------------
# ImageNet-consistent transform
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -----------------------------
# Agent: Video perception
# -----------------------------
def analyze_video(video_path, frame_skip=5):
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    anomaly_scores = []
    flagged_frame = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_idx += 1
        if frame_idx % frame_skip != 0:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)

        face = mtcnn(img)
        if face is None:
            continue

        face = face.unsqueeze(0).to(device)

        with torch.no_grad():
            features = model.forward_features(face)
            score = torch.mean(features).item()

        anomaly_scores.append(score)

        # store first suspicious frame
        if flagged_frame is None:
            flagged_frame = Image.fromarray(rgb)

    cap.release()

    if not anomaly_scores:
        return 0.0, None

    confidence = float(np.tanh(np.mean(anomaly_scores)))
    return confidence, flagged_frame
