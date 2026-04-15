# Comparison Matrix: XR Tools for Science Education

Selecting the right XR tool is crucial for balancing academic rigor (scientific accuracy) with user accessibility. This table summarizes the strengths and weaknesses of the four recommended platforms for educational simulations.

| Feature | **Google Model-viewer** | **Three.js + Physics** | **PlayCanvas** | **AR.js** |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Use** | Quick 3D Object Inspection | Custom Mathematical Sims | Interactive Virtual Labs | Marker-based AR Textbooks |
| **Logic Depth** | Low (Pre-baked only) | **Very High (Custom Script)** | High (Built-in Physics) | Medium (A-Frame logic) |
| **Visual Quality** | Professional / Native | Highly Variable | **Premium / AAA** | Standard Web Graphics |
| **Physics Support** | None (Animations only) | **Real-time (Cannon/Ammo)** | Native (Rigid bodies) | Basic (A-Frame Physics) |
| **Learning Curve** | Lowest | Highest | Medium | Medium |
| **Device Support** | Excellent (Native AR) | Good (WebXR) | Good (WebGL Mobile) | Excellent (Legacy support) |

## Strategic Recommendations for "AI Python Physics"

### 🧪 Physics & Math Heavy Simulations
**Winner: Three.js + Physics Engines.**  
If you need to simulate planetary orbits, electromagnetic fields, or quantum wavefunctions based on Python-derived formulas, Three.js provides the "raw" control required to map math to 3D space.

### 🔬 Microscope & Microbiology
**Winner: PlayCanvas.**  
Microbiology requires high-fidelity textures (subsurface scattering for cells) and smooth interaction. PlayCanvas offers a visual editor that makes managing complex microbial models much easier than code-only Three.js.

### 🚜 Agricultural & Soil Analysis
**Winner: Google Model-viewer.**  
For visualizing soil sensors or NPK analysis kits in the field, Model-viewer's ability to run natively on Android/iOS via "Quick Look" without an app is unmatched for accessibility in agricultural contexts.

---
> [!TIP]
> **Pro-Tip for Academic Books:** Use **AR.js** as the "Gateway" (the marker in the book), but have it launch a **Model-viewer** or **Three.js** overlay to handle the actual scientific simulation.
