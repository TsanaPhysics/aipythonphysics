import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch10_visuals(save_path="latex/assets/ch10_trigger_roc.png"):
    """
    Generates a figure showing a Jet event graph and the ROC performance of an AI trigger.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Simplified Jet Graph Visualization
    n_hits = 15
    hit_pos = np.random.normal(size=(n_hits, 2))
    ax1.scatter(hit_pos[:, 0], hit_pos[:, 1], s=100, color='darkblue', label='Detector Hits (Nodes)')
    
    # Draw random 'edges' to represent GNN connections
    for i in range(n_hits):
        for j in range(i+1, n_hits):
            if np.linalg.norm(hit_pos[i] - hit_pos[j]) < 1.0:
                ax1.plot([hit_pos[i, 0], hit_pos[j, 0]], [hit_pos[i, 1], hit_pos[j, 1]], 
                         'gray', alpha=0.3, linewidth=1)
                
    ax1.set_title('Graph Representation of a Particle Jet')
    ax1.set_xlabel('Detector Layer $X$')
    ax1.set_ylabel('Detector Layer $Y$')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.3)
    
    # Plot 2: ROC Curve (AI Trigger Performance)
    # y_true = actual labels, y_score = AI confidence
    y_true = np.array([0, 0, 1, 1] * 25)
    y_score = np.random.rand(100)
    # Give the scores some realistic separation for the 'signal'
    y_score[y_true == 1] += 0.5 
    y_score = np.clip(y_score, 0, 1)
    
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)
    
    ax2.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:0.2f})')
    ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Chance')
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.05])
    ax2.set_xlabel('False Positive Rate (Background Leakage)')
    ax2.set_ylabel('True Positive Rate (Signal Efficiency)')
    ax2.set_title('AI Trigger Performance (ROC)')
    ax2.legend(loc="lower right")
    ax2.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 10 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch10_visuals()
