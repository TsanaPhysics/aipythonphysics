import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# Define the Neural Network Architecture
class PINN(nn.Module):
    def __init__(self):
        super(PINN, self).__init__()
        # 2 inputs: (x, t), 1 output: u(x,t)
        self.net = nn.Sequential(
            nn.Linear(2, 20), nn.Tanh(),
            nn.Linear(20, 20), nn.Tanh(),
            nn.Linear(20, 20), nn.Tanh(),
            nn.Linear(20, 1)
        )

    def forward(self, x, t):
        return self.net(torch.cat([x, t], dim=1))

def calculate_physics_loss(model, x, t, alpha=0.01):
    """
    Computes the residual of the Heat Equation: u_t - alpha * u_xx
    """
    x.requires_grad = True
    t.requires_grad = True
    u = model(x, t)
    
    # First derivatives
    u_t = torch.autograd.grad(u, t, torch.ones_like(u), create_graph=True)[0]
    u_x = torch.autograd.grad(u, x, torch.ones_like(u), create_graph=True)[0]
    
    # Second derivative with respect to x
    u_xx = torch.autograd.grad(u_x, x, torch.ones_like(u_x), create_graph=True)[0]
    
    # The PDE residual should be zero
    residual = u_t - alpha * u_xx
    return torch.mean(residual**2)

if __name__ == "__main__":
    # Example training points
    x_train = torch.rand(100, 1)
    t_train = torch.rand(100, 1)
    
    model = PINN()
    loss = calculate_physics_loss(model, x_train, t_train)
    
    print(f"Initial Physics Loss: {loss.item():.6f}")
    print("Optimization in progress...")
    # Typically followed by an optimizer (e.g., L-BFGS or Adam)
