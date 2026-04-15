# คู่มือ: AR.js สำหรับหนังสือเรียนที่มีปฏิสัมพันธ์

AR.js เป็นเครื่องมือที่อเนกประสงค์ที่สุดสำหรับการเพิ่มข้อมูล 3 มิติลงในหนังสือจริง ช่วยให้คุณเปลี่ยนไดอะแกรมที่หยุดนิ่งให้กลายเป็นการจำลองที่โต้ตอบได้โดยใช้ Marker หรือรูปภาพในหน้าหนังสือ

## คุณสมบัติเด่น
*   **Web-standard:** รันบนเบราว์เซอร์ใดก็ได้โดยไม่ต้องลงแอป
*   **Marker/Image Tracking:** ตรวจจับหน้ากระดาษหนังสือได้อย่างเสถียร
*   **Location-based:** วางข้อมูลดิจิทัลซ้อนทับบนสถานที่จริงตามพิกัด GPS

## กรณีศึกษา: การทดสอบธาตุอาหารในดิน (NPK) และค่า pH
การจำลองการเปลี่ยนสีของแผ่นทดสอบค่า pH เมื่อเจอกับค่าความเป็นกรด-ด่างของตัวอย่างดินที่แตกต่างกัน

### ตัวอย่างโค้ด: การจำลองการเปลี่ยนสีของแผ่นวัดค่า pH (AR.js + A-Frame)
```html
<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>

<a-scene embedded arjs>
  <!-- 1. นิยาม Marker (เช่น รูปแถบวัดค่า pH ในหนังสือ) -->
  <a-marker preset="hiro">
    
    <!-- 2. โมเดลแถบวัดค่า pH -->
    <a-box id="pH_strip" position="0 0 0" scale="2 0.1 0.5" color="#f1c40f">
      <a-text value="pH: 7.0 (Neutral)" position="0 0.5 0" align="center" color="#000"></a-text>
    </a-box>
    
    <!-- 3. แอนิเมชั่น: จำลองปฏิกิริยาทางเคมี -->
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

## ข้อดี vs ข้อเสีย สำหรับงานวิเคราะห์ดิน
*   **ข้อดี:** เหมาะสำหรับการทำ "คู่มือภาคสนาม" (Field Manuals) ที่ต้องการแสดงเนื้อหา 3 มิติยึดติดกับหนังสือจริง
*   **ข้อเสีย:** การตรวจจับภาพอาจสั่นไหวได้ในสภาวะที่มีแสงน้อย (เช่น ในโรงเรือนหรือศูนย์ทดลองบางแห่ง)
