import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Academic Styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "figure.dpi": 300
})

def generate_ch6_visuals(save_path="latex/assets/ch6_spectrogram_chirp.png"):
    """
    Generates a figure showing a gravitational wave 'chirp' signal and its spectrogram.
    """
    fs = 4096 # Hz (LIGO standard)
    T = 1.0 # second
    t = np.linspace(0, T, int(fs * T))
    
    # Simulate a Chirp: frequency increasing with time
    f0 = 20
    f1 = 500
    # Analytic Chirp: sin(2 * pi * phase) where phase = int(f(t)dt)
    phi = f0 * t + (f1 - f0) * t**2 / (2 * T)
    chirp = np.sin(2 * np.pi * phi)
    
    # Add high-amplitude noise
    noise = 2.0 * np.random.normal(size=t.shape)
    strain = chirp + noise
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # Plot 1: Timedomain signals
    ax1.plot(t, strain, 'gray', alpha=0.3, label='Noisy Strain ($SNR \approx 0.5$)')
    ax1.plot(t, chirp, 'b-', linewidth=1.5, label='Pure Chirp Signal')
    ax1.set_title('Gravitational Waveform (Binary Merger Mimic)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Strain ($h$)')
    ax1.legend(loc='upper left')
    ax1.set_xlim(0.5, 1.0) # Zoom in on the chirp end
    
    # Plot 2: Spectrogram of the PURE chirp
    f, times, Sxx = spectrogram(chirp, fs, nperseg=256)
    im = ax2.pcolormesh(times, f, 10 * np.log10(Sxx + 1e-15), shading='gouraud', cmap='magma')
    ax2.set_title('Spectrogram (Frequency Evolution)')
    ax2.set_ylabel('Frequency [Hz]')
    ax2.set_xlabel('Time [sec]')
    ax2.set_ylim(0, 600)
    plt.colorbar(im, ax=ax2, label='Intensity [dB]')
    
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Chapter 6 visuals saved to {save_path}")

if __name__ == "__main__":
    generate_ch6_visuals()
