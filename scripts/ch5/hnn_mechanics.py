import torch
import torch.nn as nn

class HNN(nn.Module):
    """
    Hamiltonian Neural Network (HNN)
    Learns the scalar Hamiltonian function H(q, p) instead of direct physics.
    """
    def __init__(self, input_dim=2, hidden_dim=64):
        super(HNN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim), nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim), nn.Tanh(),
            nn.Linear(hidden_dim, 1) # Output is scalar energy
        )

    def forward(self, state):
        return self.net(state)

def compute_hnn_dynamics(model, q, p):
    """
    Using the learned Hamiltonian H, compute the dynamics:
    dq/dt = dH/dp, dp/dt = -dH/dq
    """
    q.requires_grad = True
    p.requires_grad = True
    
    H = model(torch.cat([q, p], dim=1))
    
    # Compute derivatives via Autograd
    dH_dp = torch.autograd.grad(H, p, torch.ones_like(H), create_graph=True)[0]
    dH_dq = torch.autograd.grad(H, q, torch.ones_like(H), create_graph=True)[0]
    
    dq_dt = dH_dp
    dp_dt = -dH_dq
    
    return dq_dt, dp_dt

if __name__ == "__main__":
    q = torch.randn(1, 1)
    p = torch.randn(1, 1)
    model = HNN()
    
    dq, dp = compute_hnn_dynamics(model, q, p)
    print(f"HNN Predicted Velocity (dq/dt): {dq.item():.4f}")
    print(f"HNN Predicted Force (dp/dt): {dp.item():.4f}")
