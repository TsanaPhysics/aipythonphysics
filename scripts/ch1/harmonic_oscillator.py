import numpy as np
import matplotlib.pyplot as plt

def simulate_harmonic_oscillator(k=1.0, m=1.0, x0=1.0, v0=0.0, dt=0.01, duration=10):
    """
    Simulates a Simple Harmonic Oscillator using the Euler Method.
    
    Parameters:
    - k: spring constant
    - m: mass
    - x0: initial position
    - v0: initial velocity
    - dt: time step
    - duration: total simulation time
    """
    t = np.arange(0, duration, dt)
    x = np.zeros_like(t)
    v = np.zeros_like(t)
    
    x[0] = x0
    v[0] = v0
    
    for i in range(1, len(t)):
        # Calculate acceleration: a = -k/m * x
        a = -(k/m) * x[i-1]
        
        # Update velocity and position
        v[i] = v[i-1] + a * dt
        x[i] = x[i-1] + v[i] * dt
        
    return t, x, v

if __name__ == "__main__":
    t, x, v = simulate_harmonic_oscillator()
    
    # --- Visualization ---
    plt.figure(figsize=(12, 5))
    
    # Position vs Time
    plt.subplot(1, 2, 1)
    plt.plot(t, x, color='#00F2FF', linewidth=2)
    plt.title('Position vs Time (Synthetic)', fontsize=12, fontweight='bold')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Phase Space
    plt.subplot(1, 2, 2)
    plt.plot(x, v, color='#FF007C', linewidth=2)
    plt.title('Phase Space: Position vs Velocity', fontsize=12, fontweight='bold')
    plt.xlabel('Position (x)')
    plt.ylabel('Velocity (v)')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    # Save the result for LaTeX
    plt.savefig('../../latex/assets/ch1_oscillator_results.png', dpi=300)
    print("Plot saved to latex/assets/ch1_oscillator_results.png")
    
    # --- Data Output for LaTeX Table ---
    print("\nSimulation Data Sample (First 10 steps):")
    print("-" * 35)
    print(f"{'Time (s)':<10} | {'Pos (m)':<10} | {'Vel (m/s)':<10}")
    print("-" * 35)
    for i in range(0, 100, 10): # Sample every 10th step for brevity
        print(f"{t[i]:<10.2f} | {x[i]:<10.4f} | {v[i]:<10.4f}")
    print("-" * 35)
