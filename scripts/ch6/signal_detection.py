import torch
import torch.nn as nn

class WaveformCNN(nn.Module):
    """
    1D Convolutional Neural Network for detecting physical signals (e.g. chirps)
    in noisy time-series data like LIGO strain data.
    """
    def __init__(self, input_length=1000):
        super(WaveformCNN, self).__init__()
        self.conv = nn.Sequential(
            # Large kernel to capture oscillating patterns
            nn.Conv1d(1, 16, kernel_size=64, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(4),
            nn.Conv1d(16, 32, kernel_size=32, stride=1),
            nn.ReLU(),
            nn.MaxPool1d(4),
            nn.Flatten()
        )
        
        # Calculate flattened dimension
        self.fc = nn.Sequential(
            nn.Linear(self._get_flatten_dim(input_length), 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid() # Binary probability: Signal vs Noise
        )

    def _get_flatten_dim(self, length):
        with torch.no_grad():
            x = torch.zeros(1, 1, length)
            x = self.conv(x)
            return x.shape[1]

    def forward(self, x):
        features = self.conv(x)
        return self.fc(features)

if __name__ == "__main__":
    model = WaveformCNN()
    # Mock data: 1 channel, 1000 time steps
    noisy_signal = torch.randn(1, 1, 1000)
    prob = model(noisy_signal)
    print(f"Signal Presence Probability: {prob.item() * 100:.2f}%")
