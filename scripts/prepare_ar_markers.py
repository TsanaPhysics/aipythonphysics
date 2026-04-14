import os
import shutil
from PIL import Image, ImageEnhance

# Configuration
source_dir = "/Applications/XAMPP/xamppfiles/htdocs/new_book2026/aipythonphysics/latex/assets/"
output_dir = "/Applications/XAMPP/xamppfiles/htdocs/new_book2026/aipythonphysics/ar_portal/assets/markers_to_compile/"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define target images and their corresponding AR chapter indices
# Map: Chapter Prefix -> Marker Filename
target_chapters = [
    ("ch1", "ch1_oscillator_results.png"),
    ("ch2", "ch2_orbit_results.png"),
    ("ch3", "ch3_pinn_results.png"),
    ("ch4", "ch4_ising_results.png"),
    ("ch5", "ch5_hnn_results.png"),
    ("ch6", "ch6_results.png"),
    ("ch7", "ch7_results.png"),
    ("ch8", "ch8_results.png"),
    ("ch9", "ch9_results.png"),
    ("ch10", "ch10_results.png")
]

processed_count = 0

print("-" * 40)
print("🚀 AR Marker Preparation Start")
print("-" * 40)

for i, (chap_id, filename) in enumerate(target_chapters):
    src_path = os.path.join(source_dir, filename)
    
    if os.path.exists(src_path):
        try:
            # Open and Optimize for AR Tracking
            img = Image.open(src_path)
            
            # 1. Convert to RGB (in case of RGBA)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # 2. Enhance Contrast (Crucial for AR.js/MindAR feature point detection)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.8) # High contrast for better edge detection
            
            # 3. Sharpen slightly
            sharpness = ImageEnhance.Sharpness(img)
            img = sharpness.enhance(1.2)
            
            # 4. Save with indexed filename for AR logic (target0.png, target1.png, ...)
            dest_filename = f"target{i}.png"
            dest_path = os.path.join(output_dir, dest_filename)
            img.save(dest_path, quality=95)
            
            print(f"✅ [Target {i}] Processed: {filename} -> {dest_filename}")
            processed_count += 1
            
        except Exception as e:
            print(f"❌ [Target {i}] Error processing {filename}: {str(e)}")
    else:
        print(f"⚠️ [Target {i}] Missing: {filename}")

print("-" * 40)
print(f"✨ Task Complete: {processed_count} markers ready in:")
print(f"📂 {output_dir}")
print("-" * 40)
print("👉 INSTRUCTION: Go to https://hiukim.github.io/mind-ar-js-doc/tools/compile")
print("👉 Drag all 'targetX.png' files into the web tool, compile, and save as 'targets.mind'")
