# Manual: Three.js + Physics for Computational Physics

Three.js is the foundation for almost all web-based 3D content. For "AI Python Physics", it is the most important tool because you can directly map Python numerical methods (Euler, Runge-Kutta) to the 3D scene.

## Key Features
*   **Custom Geometry:** Create objects representing mathematical functions (e.g., Sine waves).
*   **Physics Integration:** Use **Cannon.js** or **Ammo.js** for rigid body dynamics.
*   **Shaders:** Real-time visualization of fields (Magnetic, Gravitational) using GPU.

## Case Study: Simple Pendulum with Cannon.js
Predicting the swing of a pendulum using gravity and length constraints.

### Sample Code: Pendulum Simulation
```javascript
import * as THREE from 'three';
import * as CANNON from 'cannon-es';

// 1. Setup Cannon.js World
const world = new CANNON.World();
world.gravity.set(0, -9.82, 0); // Meter-scale gravity

// 2. Create Pendulum Bob
const radius = 1;
const bobShape = new CANNON.Sphere(radius);
const bobBody = new CANNON.Body({ mass: 5 }); // 5kg
bobBody.addShape(bobShape);
bobBody.position.set(3, 5, 0); // Starting point
world.addBody(bobBody);

// 3. Create Pivot point and Constraint (The String)
const pivot = new CANNON.Vec3(0, 10, 0);
const constraint = new CANNON.PointToPointConstraint(bobBody, new CANNON.Vec3(0, 0, 0), null, pivot);
world.addConstraint(constraint);

// 4. Animation Loop
function animate() {
    requestAnimationFrame(animate);
    world.step(1/60); // Advance time by 1/60th second
    
    // Update Three.js mesh from Physics body
    bobMesh.position.copy(bobBody.position);
    bobMesh.quaternion.copy(bobBody.quaternion);
    
    renderer.render(scene, camera);
}
```

## Pros vs Cons for Physics
*   **Pros:** Exact mathematical control; compatible with NumPy/Scipy-like logic in JS.
*   **Cons:** No visual editor; requires strong JavaScript knowledge.
