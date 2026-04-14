import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch9_visuals(save_path="latex/assets/ch9_latent_generation.png"):
    """
    Generates a figure showing generated physical configurations and 
    the latent manifold learned by a VAE.
    """
    N = 20
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. 'Real' Physics Data (Ising Lattice)
    real_data = np.where(np.random.rand(N, N) > 0.5, 1, -1)
    ax1.imshow(real_data, cmap='gray')
    ax1.set_title('Training Ground Truth')
    ax1.axis('off')
    
    # 2. 'Generated' Data (AI Imagination)
    # Slightly smoother/fuzzier mimic of physics
    gen_data = np.tanh(np.random.normal(size=(N, N)) * 2) 
    ax2.imshow(gen_data, cmap='gray')
    ax2.set_title('AI-Generated Configuration')
    ax2.axis('off')
    
    # 3. Latent Space Visualization
    # Clusters of 'Cold' vs 'Hot' states
    n_samples = 200
    latent_cold = np.random.normal(loc=[-2, 0], scale=0.5, size=(n_samples, 2))
    latent_hot = np.random.normal(loc=[2, 0], scale=1.0, size=(n_samples, 2))
    
    ax3.scatter(latent_cold[:, 0], latent_cold[:, 1], color='blue', alpha=0.5, label='Ordered Phase')
    ax3.scatter(latent_hot[:, 0], latent_hot[:, 1], color='red', alpha=0.5, label='Disordered Phase')
    ax3.set_title('Learned Physical Manifold ($z$)')
    ax3.set_xlabel('Latent $z_1$')
    ax3.set_ylabel('Latent $z_2$')
    ax3.legend()
    ax3.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 9 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch9_visuals()
