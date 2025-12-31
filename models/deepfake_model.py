import torch
import timm
import torchvision.transforms as transforms
import cv2
import numpy as np
from PIL import Image

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# REAL Xception model
model = timm.create_model(
    "xception",
    pretrained=True,
    num_classes=2
)

model.eval()
model.to(device)

transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5]
    )
])

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_scores = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face = Image.fromarray(frame_rgb)
        face = transform(face).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(face)
            prob = torch.softmax(output, dim=1)[0][1].item()
            frame_scores.append((prob, frame))

    cap.release()

    if not frame_scores:
        return 0.0, []

    avg_conf = float(np.mean([x[0] for x in frame_scores]))
    return avg_conf, frame_scores
