import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch4_visuals(save_path="latex/assets/ch4_ising_phases.png"):
    """
    Generates a figure showing spin lattice configurations and magnetization phase transition.
    """
    N = 20
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. Ferromagnetic phase (Cold)
    # Most spins aligned
    cold_lattice = np.where(np.random.rand(N, N) > 0.1, 1, -1)
    ax1.imshow(cold_lattice, cmap='gray', interpolation='nearest')
    ax1.set_title('Ordered Phase ($T < T_c$)')
    ax1.axis('off')
    
    # 2. Paramagnetic phase (Hot)
    # Random spins
    hot_lattice = np.random.choice([1, -1], size=(N, N))
    ax2.imshow(hot_lattice, cmap='gray', interpolation='nearest')
    ax2.set_title('Disordered Phase ($T > T_c$)')
    ax2.axis('off')
    
    # 3. Magnetization Curve
    T = np.linspace(1.5, 3.5, 100)
    Tc = 2.269
    # Analytic-like magnetization for 2D Ising
    M = np.where(T < Tc, (1 - np.sinh(2/T)**-4)**(1/8), 0)
    
    ax3.plot(T, M, 'b-', linewidth=2)
    ax3.axvline(x=Tc, color='r', linestyle='--', label='$T_c \approx 2.27$')
    ax3.set_title('Phase Transition: Magnetization')
    ax3.set_xlabel('Temperature ($T$)')
    ax3.set_ylabel('Mean Magnetization ($|M|$)')
    ax3.legend()
    ax3.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 4 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch4_visuals()
