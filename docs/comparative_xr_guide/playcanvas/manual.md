# Manual: PlayCanvas for High-End Virtual Labs

PlayCanvas is a high-performance, WebGL-native engine with a visual editor. It is ideal for "Microbiology" where organic shapes and complex laboratory interactions are required.

## Key Features
*   **Visual Editor:** Real-time WYSIWYG editor for lighting, particles, and physics.
*   **Performance:** Faster loading and run-time than Unity-to-WebGL exports.
*   **Asset Management:** Drag and drop 3D models of bacteria, petri dishes, and microscopes.

## Case Study: Microbial Growth (Bacterial Colony Simulation)
Simulating the growth of *E. coli* on an agar plate using a script that scales models over time.

### Sample Code: Bacterial Growth Script (PlayCanvas JS)
```javascript
var BacterialGrowth = pc.createScript('bacterialGrowth');

BacterialGrowth.attributes.add('growthRate', { type: 'number', default: 0.05 });
BacterialGrowth.attributes.add('maxScale', { type: 'number', default: 5 });

BacterialGrowth.prototype.update = function(dt) {
    // 1. Get current scale of the colony
    var currentScale = this.entity.getLocalScale();
    
    // 2. Linear growth logic (Simplified science)
    if (currentScale.x < this.maxScale) {
        var newScale = currentScale.x + (this.growthRate * dt);
        this.entity.setLocalScale(newScale, newScale, newScale);
    }
    
    // 3. Visualization: Change color as colony matures
    var material = this.entity.render.meshInstances[0].material;
    material.diffuse.set(1, 1 - (currentScale.x / 10), 0); // Becomes redder
    material.update();
};
```

## Pros vs Cons for Microbiology
*   **Pros:** Best visual quality for organic materials; built-in animation system.
*   **Cons:** Higher file size for complex labs; require hosting on PlayCanvas (or self-hosting).
