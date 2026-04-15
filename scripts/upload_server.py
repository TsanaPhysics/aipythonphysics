import http.server
import socketserver
import base64
import os

PORT = 9999
TARGET_PATH = "ar_portal/assets/targets/targets.mind"

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            # Save the binary data directly
            with open(TARGET_PATH, "wb") as f:
                f.write(post_data)
            
            print(f"\n[SUCCESS] File saved successfully to {TARGET_PATH}")
            print(f"[INFO] File size: {len(post_data) / 1024:.2f} KB")
            
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"OK - Saved")
            
            # Auto-shutdown after success
            # os._exit(0) 
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            self.send_response(500)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

with socketserver.TCPServer(("", PORT), UploadHandler) as httpd:
    print(f"Server started at port {PORT}. Waiting for data...")
    httpd.handle_request() # Wait for one request and then finish
