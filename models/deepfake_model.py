import torch
import torchvision.transforms as transforms
import cv2
import numpy as np
from PIL import Image

model = torch.hub.load(
    'pytorch/vision:v0.10.0',
    'xception',
    pretrained=True
)
model.eval()

transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(),
])

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_scores = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        face = Image.fromarray(frame)
        face = transform(face).unsqueeze(0)

        with torch.no_grad():
            output = model(face)
            confidence = torch.sigmoid(output).item()
            frame_scores.append((confidence, frame))

    cap.release()

    if not frame_scores:
        return 0.0, []

    avg_conf = float(np.mean([x[0] for x in frame_scores]))
    return avg_conf, frame_scores
