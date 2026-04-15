# คู่มือ: Google Model-viewer สำหรับงาน XR ทางการเกษตร

`<model-viewer>` ของ Google เป็นส่วนประกอบเว็บมาตรฐาน (Web Component) สำหรับการแสดงผลโมเดล 3 มิติ ถือเป็นตัวเลือกที่ดีที่สุดสำหรับ "การเกษตรดิจิทัล" ที่ผู้ใช้งานต้องดูอุปกรณ์ฮาร์ดแวร์ (เช่น เซ็นเซอร์, ชุดทดสอบ NPK) ด้วยแสงและเงาที่สมจริง

## คุณสมบัติเด่น
*   **AR-First:** มีปุ่ม "View in space" ในตัว โดยใช้ ARCore (Android) หรือ ARQuickLook (iOS)
*   **Annotations:** เพิ่มป้ายกำกับที่คลิกได้ไปยังพิกัดที่เฉพาะเจาะจงบนโมเดล
*   **Progressive Loading:** จัดการไฟล์ขนาดใหญ่ได้อย่างราบรื่นด้วยการใช้ภาพตัวอย่างที่มีความละเอียดต่ำก่อน

## กรณีศึกษา: เซ็นเซอร์วัดธาตุอาหารในดิน (NPK-pH Analyzer)
ในการทดลองทางการเกษตร การแสดงโมเดลเซ็นเซอร์ 3 มิติพร้อมระดับความลึกในดิน ช่วยให้ผู้เรียนเข้าใจตำแหน่งที่ถูกต้องของการวางโพรบ (Probe)

### ตัวอย่างโค้ด: เซ็นเซอร์ดินพร้อมจุดแจ้งเตือน (Hotspots)
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
  
  <!-- Hotspot สำหรับ Nitrogen Probe -->
  <button class="hotspot" slot="hotspot-probe" data-position="0.2m 0.5m 0m" data-normal="0m 1m 0m">
    <div class="annotation">Nitrogen Sensor (N)</div>
  </button>

  <!-- Hotspot สำหรับ pH Sensor -->
  <button class="hotspot" slot="hotspot-ph" data-position="-0.2m 0.5m 1m" data-normal="0m 1m 0m">
    <div class="annotation">pH Glass Electrode</div>
  </button>
</model-viewer>

<style>
  .hotspot { background: #00ffaa; border-radius: 50%; border: none; width: 20px; height: 20px; }
  .annotation { background: #000; color: #fff; padding: 5px; border-radius: 5px; position: absolute; transform: translateY(-30px); }
</style>
```

## ข้อดี vs ข้อเสีย สำหรับงานเกษตร
*   **ข้อดี:** ประสิทธิภาพการทำงานสูง (Native); ไม่ต้องโหลดแอปเพิ่ม; ใช้งานออฟไลน์ได้หากเก็บแคชไว้
*   **ข้อเสีย:** ไม่สามารถจำลองการเปลี่ยนแปลงทางเคมีที่ซับซ้อนแบบ Real-time ได้
