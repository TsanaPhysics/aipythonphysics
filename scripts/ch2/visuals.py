import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def orbit_dynamics(t, state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    G_M = 1.0 # Normalized units for visual clarity
    ax = -G_M * x / r**3
    ay = -G_M * y / r**3
    return [vx, vy, ax, ay]

def generate_ch2_visuals(save_path="latex/assets/ch2_orbit_stability.png"):
    """
    Generates a figure demonstrating orbital stability vs numerical precision.
    """
    y0 = [1.0, 0, 0, 0.8] # Elliptical initial condition
    t_span = (0, 20)
    
    # Low precision vs High precision
    sol_low = solve_ivp(orbit_dynamics, t_span, y0, rtol=1e-3, atol=1e-3)
    sol_high = solve_ivp(orbit_dynamics, t_span, y0, rtol=1e-12, atol=1e-12)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: The Orbit
    ax1.plot(sol_high.y[0], sol_high.y[1], 'b-', label='Stable Orbit (High Prec)')
    ax1.plot(sol_low.y[0], sol_low.y[1], 'r--', alpha=0.6, label='Decaying Orbit (Low Prec)')
    ax1.plot(0, 0, 'go', label='Central Mass')
    ax1.set_title('Phase Space Stability')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.axis('equal')
    ax1.legend()
    
    # Plot 2: Energy Conservation Error
    def energy(sol):
        r = np.sqrt(sol.y[0]**2 + sol.y[1]**2)
        v2 = sol.y[2]**2 + sol.y[3]**2
        return 0.5 * v2 - 1.0/r
    
    e_low = energy(sol_low)
    e_high = energy(sol_high)
    
    ax2.plot(sol_low.t, np.abs(e_low - e_low[0]) + 1e-15, 'r-', label='Low Precision Error')
    ax2.plot(sol_high.t, np.abs(e_high - e_high[0]) + 1e-15, 'b-', label='High Precision Error')
    ax2.set_yscale('log')
    ax2.set_title('Numerical Energy Leak')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Absolute Energy Error')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 2 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch2_visuals()
