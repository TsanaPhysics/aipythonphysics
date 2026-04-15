# คู่มือ: PlayCanvas สำหรับห้องปฏิบัติการเสมือนจริงระดับสูง

PlayCanvas เป็นเอนจิ้น WebGL ที่มีประสิทธิภาพสูงและมีตัวแก้ไขแบบภาพ (Visual Editor) เหมาะอย่างยิ่งสำหรับงาน "จุลชีววิทยา" ที่ต้องการรูปทรงออร์แกนิกและการจำลองปฏิสัมพันธ์ในห้องปฏิบัติการที่ซับซ้อน

## คุณสมบัติเด่น
*   **Visual Editor:** ตัวแก้ไขแบบ WYSIWYG ที่ใช้งานง่ายสำหรับการจัดแสง, เอฟเฟกต์อนุภาค (Particles) และฟิสิกส์
*   **Performance:** โหลดได้รวดเร็วและรันได้เสถียรกว่าการส่งออกงานจาก Unity ไปยัง WebGL
*   **Asset Management:** จัดการโมเดล 3 มิติของแบคทีเรีย, จานเพาะเชื้อ และกล้องจุลทรรศน์ได้ง่ายด้วยการลากวาง

## กรณีศึกษา: การเติบโตของจุลินทรีย์ (Bacterial Colony Simulation)
การจำลองการเติบโตของเชื้อ *E. coli* บนจานเพาะเชื้อโดยใช้สคริปต์เพื่อควบคุมขนาดของโมเดลตามเวลาที่ผ่านไป

### ตัวอย่างโค้ด: สคริปต์การเติบโตของแบคทีเรีย (PlayCanvas JS)
```javascript
var BacterialGrowth = pc.createScript('bacterialGrowth');

BacterialGrowth.attributes.add('growthRate', { type: 'number', default: 0.05 });
BacterialGrowth.attributes.add('maxScale', { type: 'number', default: 5 });

BacterialGrowth.prototype.update = function(dt) {
    // 1. รับขนาดปัจจุบันของกลุ่มจุลินทรีย์
    var currentScale = this.entity.getLocalScale();
    
    // 2. ตรรกะการเติบโตแบบเชิงเส้น (แบบง่าย)
    if (currentScale.x < this.maxScale) {
        var newScale = currentScale.x + (this.growthRate * dt);
        this.entity.setLocalScale(newScale, newScale, newScale);
    }
    
    // 3. การแสดงผล: เปลี่ยนสีเมื่อกลุ่มจุลินทรีย์โตเต็มที่
    var material = this.entity.render.meshInstances[0].material;
    material.diffuse.set(1, 1 - (currentScale.x / 10), 0); // จะค่อยๆ เปลี่ยนเป็นสีแดงมากขึ้น
    material.update();
};
```

## ข้อดี vs ข้อเสีย สำหรับงานจุลชีววิทยา
*   **ข้อดี:** คุณภาพของภาพดีที่สุดสำหรับการแสดงผลวัตถุทางชีวภาพ; มีระบบแอนิเมชั่นในตัว
*   **ข้อเสีย:** ขนาดไฟล์อาจใหญ่ขึ้นสำหรับห้องแล็บที่ซับซ้อน; ต้องการพื้นที่จัดเก็บใน PlayCanvas (หรือต้องโฮสต์เอง)
