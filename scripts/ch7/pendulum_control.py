import torch
import torch.nn as nn
import torch.optim as optim

class PolicyNetwork(nn.Module):
    """
    Simple Reinforcement Learning Policy for Inverted Pendulum control.
    Takes 4 states (position, velocity, angle, angular velocity) 
    and outputs 2 action probabilities (Left, Right).
    """
    def __init__(self, state_dim=4, action_dim=2):
        super(PolicyNetwork, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.net(x)

def select_action(model, state):
    state = torch.from_numpy(state).float().unsqueeze(0)
    probs = model(state)
    m = torch.distributions.Categorical(probs)
    action = m.sample()
    return action.item(), m.log_prob(action)

if __name__ == "__main__":
    # Mock physical state: [cart_pos, cart_vel, pole_angle, pole_vel]
    import numpy as np
    mock_state = np.array([0.1, 0.05, 0.02, 0.01])
    
    model = PolicyNetwork()
    action, log_prob = select_action(model, mock_state)
    
    print(f"Agent chose action: {'RIGHT' if action == 1 else 'LEFT'}")
    print(f"Action Log-Probability: {log_prob.item():.4f}")
