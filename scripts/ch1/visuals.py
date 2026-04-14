import numpy as np
import matplotlib.pyplot as plt

# Academic Plot Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "legend.fontsize": 10,
    "figure.dpi": 300
})

def generate_oscillator_visuals(save_path="latex/assets/ch1_oscillator.png"):
    """
    Generates a high-fidelity academic figure comparing theoretical harmonic 
    motion with noisy observation.
    """
    t = np.linspace(0, 10, 500)
    omega = 2 * np.pi * 0.5 # 0.5 Hz
    x_ideal = np.cos(omega * t)
    
    # Gaussian Noise (LIGO mimic)
    sigma = 0.1
    noise = np.random.normal(0, sigma, t.shape)
    x_noisy = x_ideal + noise
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotting
    ax.plot(t, x_ideal, 'b-', linewidth=2, label=r'Theoretical Model: $x(t) = A\cos(\omega_0 t)$')
    ax.scatter(t, x_noisy, color='r', s=15, alpha=0.4, label='Noisy Experimental Data ($SNR \approx 10$)')
    
    # Formatting
    ax.set_xlabel('Time (s)', fontweight='bold')
    ax.set_ylabel('Displacement (m)', fontweight='bold')
    ax.set_title('Bridges Between Theory and Observation in Physics', fontsize=16)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper right', frameon=True, shadow=True)
    
    # Save for LaTeX
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Academic figure saved to {save_path}")

if __name__ == "__main__":
    generate_oscillator_visuals()
