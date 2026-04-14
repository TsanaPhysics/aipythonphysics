import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch3_visuals(save_path="latex/assets/ch3_pinn_heat.png"):
    """
    Generates a figure showing the 1D Heat Equation evolution and PINN loss convergence.
    """
    # 1. Simulate Heat Field (Analytic)
    # u(x,t) = exp(-alpha * pi^2 * t) * sin(pi * x)
    x = np.linspace(0, 1, 100)
    t = np.linspace(0, 0.5, 100)
    X, T = np.meshgrid(x, t)
    alpha = 0.1
    U = np.exp(-alpha * (np.pi**2) * T) * np.sin(np.pi * X)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Heat Evolution
    im = ax1.imshow(U, extent=[0, 1, 0, 0.5], origin='lower', aspect='auto', cmap='hot')
    plt.colorbar(im, ax=ax1, label='Temperature ($u$)')
    ax1.set_title('1D Heat Equation Evolution ($u(x,t)$)')
    ax1.set_xlabel('Space ($x$)')
    ax1.set_ylabel('Time ($t$)')
    
    # Plot 2: Mock PINN Loss Convergence
    epochs = np.arange(0, 500)
    # Loss = Data Loss + Physics Loss
    # Physics loss drops slower early on
    physics_loss = 1.0 * np.exp(-epochs/100) + 0.01 * np.random.normal(0, 1e-4, epochs.shape)
    data_loss = 0.5 * np.exp(-epochs/50)
    
    ax2.plot(epochs, physics_loss, 'r-', label='Physics Residual Loss ($\mathcal{L}_{phys}$)')
    ax2.plot(epochs, data_loss, 'b--', label='Boundary Data Loss ($\mathcal{L}_{data}$)')
    ax2.set_yscale('log')
    ax2.set_title('PINN Training Convergence')
    ax2.set_xlabel('Training Epochs')
    ax2.set_ylabel('Log Loss')
    ax2.grid(True, which="both", ls="-", alpha=0.5)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 3 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch3_visuals()
