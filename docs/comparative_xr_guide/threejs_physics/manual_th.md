# คู่มือ: Three.js + Physics สำหรับฟิสิกส์คำนวณ

Three.js คือพื้นฐานหลักของคอนเทนต์ 3 มิติบเกือบทั้งหมดบนเว็บ สำหรับโครงการ "AI Python Physics" เครื่องมือนี้สำคัญที่สุดเพราะคุณสามารถจับคู่การทำงานทางคณิตศาสตร์ใน Python (เช่น Euler, Runge-Kutta) มาไว้ในพื้นที่ 3 มิติได้โดยตรง

## คุณสมบัติเด่น
*   **Custom Geometry:** สร้างวัตถุที่เป็นตัวแทนของฟังก์ชันทางคณิตศาสตร์ (เช่น คลื่นไซน์)
*   **Physics Integration:** ใช้งานร่วมกับ **Cannon.js** หรือ **Ammo.js** เพื่อจำลองการเคลื่อนที่ของวัตถุแข็ง (Rigid body)
*   **Shaders:** การแสดงผลสนาม (Fields) ต่างๆ แบบ Real-time เช่น สนามแม่เหล็ก หรือสนามโน้มถ่วง โดยใช้ GPU

## กรณีศึกษา: ลูกตุ้มอย่างง่าย (Simple Pendulum) ด้วย Cannon.js
การทำนายการแกว่งของลูกตุ้มโดยใช้แรงโน้มถ่วงและข้อจำกัดของความยาวเชือก

### ตัวอย่างโค้ด: การจำลองลูกตุ้ม
```javascript
import * as THREE from 'three';
import * as CANNON from 'cannon-es';

// 1. ตั้งค่าโลกฟิสิกส์ด้วย Cannon.js
const world = new CANNON.World();
world.gravity.set(0, -9.82, 0); // แรงโน้มถ่วงระดับเมตร

// 2. สร้างลูกตุ้ม (Bob)
const radius = 1;
const bobShape = new CANNON.Sphere(radius);
const bobBody = new CANNON.Body({ mass: 5 }); // น้ำหนัก 5 กิโลกรัม
bobBody.addShape(bobShape);
bobBody.position.set(3, 5, 0); // จุดเริ่มต้น
world.addBody(bobBody);

// 3. สร้างจุดหมุน (Pivot) และข้อจำกัด (Constraint - แทนความยาวเชือก)
const pivot = new CANNON.Vec3(0, 10, 0);
const constraint = new CANNON.PointToPointConstraint(bobBody, new CANNON.Vec3(0, 0, 0), null, pivot);
world.addConstraint(constraint);

// 4. วนลูปแอนิเมชั่น
function animate() {
    requestAnimationFrame(animate);
    world.step(1/60); // ก้าวไปข้างหน้าทีละ 1/60 วินาที
    
    // อัปเดตตำแหน่ง Mesh ของ Three.js จาก Physics body
    bobMesh.position.copy(bobBody.position);
    bobMesh.quaternion.copy(bobBody.quaternion);
    
    renderer.render(scene, camera);
}
```

## ข้อดี vs ข้อเสีย สำหรับงานฟิสิกส์
*   **ข้อดี:** ควบคุมทางคณิตศาสตร์ได้อย่างแม่นยำ; เข้ากันได้ดีกับตรรกะแบบ NumPy/Scipy ในภาษา JavaScript
*   **ข้อเสีย:** ไม่มี Visual Editor; ต้องมีความรู้ด้าน JavaScript ที่แข็งแกร่ง
