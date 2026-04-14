import numpy as np
import matplotlib.pyplot as plt

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch7_visuals(save_path="latex/assets/ch7_pendulum_rl.png"):
    """
    Generates a figure showing Reinforcement Learning reward convergence and 
    physical balance stability.
    """
    epochs = np.arange(0, 200)
    
    # 1. Training Reward (Learning Curve)
    # Starts low, slowly improves as agent explores, then stabilizes
    reward = 200 / (1 + np.exp(-(epochs-80)/20)) + np.random.normal(0, 10, epochs.shape)
    reward = np.clip(reward, 0, 200)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Reward Convergence
    ax1.plot(epochs, reward, 'g-', label='Total Episode Reward')
    ax1.axhline(y=195, color='r', linestyle='--', label='Solved Threshold')
    ax1.set_title('DQN Learning Progress (Inverted Pendulum)')
    ax1.set_xlabel('Episodes')
    ax1.set_ylabel('Reward (Time Balancing)')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # Plot 2: Physical State (Theta) for a Trained Agent
    t = np.linspace(0, 10, 500)
    # Mimic a stable oscillation around vertical (theta=0)
    theta = 0.05 * np.exp(-0.2 * t) * np.cos(2 * np.pi * 0.5 * t) + 0.005 * np.random.normal(size=t.shape)
    
    ax2.plot(t, theta, 'b-', label='Pole Angle $\theta(t)$')
    ax2.axhline(y=0, color='black', linestyle='-')
    ax2.set_title('Post-Training Control Stability')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Deviation from Vertical (rad)')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 7 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch7_visuals()
