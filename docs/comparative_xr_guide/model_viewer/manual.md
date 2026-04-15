# Manual: Google Model-viewer for Agricultural XR

Google's `<model-viewer>` is a standard-driven web component for displaying 3D models. It is the best choice for "Digital Agriculture" where users need to see hardware (sensors, NPK kits) with high-fidelity lighting.

## Key Features
*   **AR-First:** Built-in "View in space" button using ARCore (Android) or ARQuickLook (iOS).
*   **Annotations:** Add clickable labels to specific coordinates on a model.
*   **Progressive Loading:** Handles large files gracefully with low-res placeholders.

## Case Study: Soil Nutrient Sensor (NPK-pH Analyzer)
In an agricultural experiment, showing a 3D sensor and its depth in the soil helps students understand probe placement.

### Sample Code: Soil Sensor with Hotspots
```html
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer 
  src="assets/models/soil_sensor.glb" 
  ios-src="assets/models/soil_sensor.usdz"
  alt="Soil NPK and pH Sensor" 
  ar 
  ar-modes="webxr scene-viewer quick-look" 
  camera-controls 
  shadow-intensity="1">
  
  <!-- Hotspot for Nitrogen Probe -->
  <button class="hotspot" slot="hotspot-probe" data-position="0.2m 0.5m 0m" data-normal="0m 1m 0m">
    <div class="annotation">Nitrogen Sensor (N)</div>
  </button>

  <!-- Hotspot for pH Sensor -->
  <button class="hotspot" slot="hotspot-ph" data-position="-0.2m 0.5m 1m" data-normal="0m 1m 0m">
    <div class="annotation">pH Glass Electrode</div>
  </button>
</model-viewer>

<style>
  .hotspot { background: #00ffaa; border-radius: 50%; border: none; width: 20px; height: 20px; }
  .annotation { background: #000; color: #fff; padding: 5px; border-radius: 5px; position: absolute; transform: translateY(-30px); }
</style>
```

## Pros vs Cons for Agriculture
*   **Pros:** Native performance; no app download; works offline if cached.
*   **Cons:** Cannot simulate dynamic chemical changes in real-time.
