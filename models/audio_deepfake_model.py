import librosa
import numpy as np
import torch
import torch.nn as nn

# Simple pretrained-style MLP (lightweight, edge-ready)
class AudioDeepfakeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(40, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)

model = AudioDeepfakeNet()
model.eval()  # assume pretrained weights loaded in real deployment

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_mean = np.mean(mfcc, axis=1)

    features = torch.tensor(mfcc_mean).float().unsqueeze(0)

    with torch.no_grad():
        output = model(features)
        confidence = torch.sigmoid(output).item()

    return confidence
