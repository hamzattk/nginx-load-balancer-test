import http.server
import socketserver

PORT = 5002

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Merhaba, ben hamza2")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Sunucu {PORT} portunda çalışıyor")
    httpd.serve_forever()
