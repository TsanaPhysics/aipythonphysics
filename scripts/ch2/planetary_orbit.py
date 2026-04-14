import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Physical constants
G = 6.67430e-11  # Gravitational constant
M_sun = 1.989e30  # Mass of the Sun

def planetary_dynamics(t, state):
    """
    Defines the derivatives for a planet orbiting a central mass.
    state = [x, y, vx, vy]
    """
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    
    # Gravitational acceleration components
    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3
    
    return [vx, vy, ax, ay]

def run_simulation():
    # Initial conditions: Earth at perihelion
    # Position ~1.47e11 m, Velocity ~30.3e3 m/s
    y0 = [1.47e11, 0, 0, 3.03e4]
    
    # Time span: one year in seconds
    t_span = (0, 3.154e7)
    t_eval = np.linspace(0, 3.154e7, 1000)
    
    # Solve the ODE
    # rtol/atol define numerical precision
    sol = solve_ivp(planetary_dynamics, t_span, y0, t_eval=t_eval, rtol=1e-8)
    
    return sol

if __name__ == "__main__":
    sol = run_simulation()
    
    plt.figure(figsize=(8, 8))
    plt.plot(sol.y[0], sol.y[1], 'b-', label='Earth Orbit')
    plt.plot(0, 0, 'yo', markersize=15, label='Sun')
    plt.title('Planetary Motion Simulation (Newtonian Gravity)')
    plt.xlabel('x (meters)')
    plt.ylabel('y (meters)')
    plt.axis('equal')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()
