import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch8_visuals(save_path="latex/assets/ch8_symbolic_pareto.png"):
    """
    Generates a figure showing the Pareto Front for Symbolic Regression 
    and the discovered physical law.
    """
    # 1. Pareto Front Data (Complexity vs Accuracy)
    # Typically, as complexity increases, log(MSE) decreases
    complexity = np.array([1, 2, 3, 5, 7, 10, 15])
    # The 'Elbow' usually happens at a certain complexity (e.g., complexity=5)
    mse = np.array([10.0, 5.0, 2.0, 0.05, 0.045, 0.042, 0.040])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Pareto Front
    ax1.plot(complexity, mse, 'o-', color='darkred', markersize=8, label='Candidate Equations')
    # Mark the 'Elbow' (Occam's choice)
    ax1.annotate('Physical Law (The "Elbow")', xy=(5, 0.05), xytext=(7, 1.0),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
    ax1.set_yscale('log')
    ax1.set_title('Pareto Front: Accuracy vs. Complexity')
    ax1.set_xlabel('Equation Complexity (Number of Operators)')
    ax1.set_ylabel('Log(Mean Squared Error)')
    ax1.grid(True, which="both", ls="-", alpha=0.3)
    ax1.legend()
    
    # Plot 2: Discovered Law (Kepler 3rd Law mimic)
    a = np.linspace(1, 10, 50)
    T_clean = a**1.5
    T_noisy = T_clean + 0.1 * np.random.normal(size=a.shape)
    
    ax2.scatter(a, T_noisy, color='gray', alpha=0.5, label='Noisy Observation Data')
    ax2.plot(a, T_clean, 'b-', linewidth=2, label=r'Discovered: $T \propto a^{1.5}$')
    ax2.set_title("Rediscovering Kepler's Third Law")
    ax2.set_xlabel('Semi-major axis ($a$)')
    ax2.set_ylabel('Period ($T$)')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 8 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch8_visuals()
