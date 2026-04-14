import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch5_visuals(save_path="latex/assets/ch5_hnn_conservation.png"):
    """
    Generates a figure showing the difference between a standard neural network 
    and a Hamiltonian Neural Network in terms of energy conservation.
    """
    t = np.linspace(0, 50, 500)
    
    # 1. Standard MLP (Numerical Heating - Spirals Out)
    # Simulation: q = A*exp(gamma*t)*cos(omega*t)
    gamma = 0.05
    q_mlp = np.exp(gamma * t) * np.cos(t)
    p_mlp = -np.exp(gamma * t) * np.sin(t)
    
    # 2. HNN (Energy Conserving - Closed Orbit)
    q_hnn = np.cos(t)
    p_hnn = -np.sin(t)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Phase Space Comparison
    ax1.plot(q_mlp, p_mlp, 'r--', alpha=0.6, label='Standard MLP (Drift)')
    ax1.plot(q_hnn, p_hnn, 'b-', linewidth=2, label='HNN (Energy Conserving)')
    ax1.set_title('Phase Space Trajectories ($q, p$)')
    ax1.set_xlabel('Position ($q$)')
    ax1.set_ylabel('Momentum ($p$)')
    ax1.axis('equal')
    ax1.legend()
    
    # Plot 2: Total Energy over Time
    # E = 0.5 * (p^2 + q^2)
    E_mlp = 0.5 * (p_mlp**2 + q_mlp**2)
    E_hnn = 0.5 * (p_hnn**2 + q_hnn**2)
    
    ax2.plot(t, E_mlp, 'r-', label='Standard MLP Energy')
    ax2.plot(t, E_hnn, 'b-', label='HNN Total Energy')
    ax2.set_title('Energy Consistency Check')
    ax2.set_xlabel('Time ($t$)')
    ax2.set_ylabel('Total Energy ($H$)')
    ax2.set_ylim(0, 10)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 5 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch5_visuals()
