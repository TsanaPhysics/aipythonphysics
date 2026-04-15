# Manual: AR.js for Interactive Textbooks

AR.js is the most versatile tool for augmenting physical books. It allows you to transform static diagrams into interactive simulations using simple markers (QR-code-like images).

## Key Features
*   **Web-standard:** Runs in any browser without an app.
*   **Marker/Image Tracking:** Stable tracking of book pages.
*   **Location-based:** Overlay data in physical locations.

## Case Study: Soil Nutrient (NPK) pH Indicator Test
Visualizing the color change of a pH indicator strip when exposed to different soil sample values.

### Sample Code: pH Indicator Simulation (AR.js + A-Frame)
```html
<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>

<a-scene embedded arjs>
  <!-- 1. Define Marker (e.g., pH Scale in the book) -->
  <a-marker preset="hiro">
    
    <!-- 2. The pH Indicator Strip Model -->
    <a-box id="pH_strip" position="0 0 0" scale="2 0.1 0.5" color="#f1c40f">
      <a-text value="pH: 7.0 (Neutral)" position="0 0.5 0" align="center" color="#000"></a-text>
    </a-box>
    
    <!-- 3. Animation: Simulating Chemical Reaction -->
    <a-animation 
      attribute="material.color" 
      from="#f1c40f" to="#e74c3c" 
      dur="3000" 
      direction="alternate" 
      repeat="indefinite">
    </a-animation>
    
  </a-marker>
  <a-entity camera></a-entity>
</a-scene>
```

## Pros vs Cons for Soil Analysis
*   **Pros:** Perfect for "Field Manuals" where 3D content must be anchored to a physical book.
*   **Cons:** Tracking can be jittery in low-light conditions (common in farms/laboratories).
