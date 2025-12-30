import librosa
import numpy as np
import torch
import torch.nn as nn

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
model.eval()

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

    segment_scores = []
    for i in range(mfcc.shape[1]):
        segment = mfcc[:, i]
        feature = torch.tensor(segment).float().unsqueeze(0)

        with torch.no_grad():
            score = torch.sigmoid(model(feature)).item()
            segment_scores.append(score)

    return float(np.mean(segment_scores)), segment_scores
