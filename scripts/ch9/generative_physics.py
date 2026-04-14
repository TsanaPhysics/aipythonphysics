import torch
import torch.nn as nn

class PhysicalGenerator(nn.Module):
    """
    Generative Adversarial Network (GAN) Generator
    Learns to generate 2D physical grid data (e.g. Ising configurations)
    from a random latent space.
    """
    def __init__(self, latent_dim=100, grid_size=20):
        super(PhysicalGenerator, self).__init__()
        self.grid_size = grid_size
        self.main = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(True),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(True),
            nn.Linear(256, grid_size * grid_size),
            nn.Tanh() # Output scaled to [-1, 1] for spin up/down
        )

    def forward(self, z):
        return self.main(z).view(-1, 1, self.grid_size, self.grid_size)

if __name__ == "__main__":
    latent_dim = 100
    generator = PhysicalGenerator(latent_dim=latent_dim)
    
    # Generate 16 random physical configurations
    z = torch.randn(16, latent_dim)
    fake_physics_data = generator(z)
    
    print(f"Generated data batch shape: {fake_physics_data.shape}")
    print("This GAN can simulate field configurations without MCMC.")
