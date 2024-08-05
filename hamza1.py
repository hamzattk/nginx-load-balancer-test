import http.server
import socketserver

PORT = 5001

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Merhaba, ben hamza1</h1>")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Sunucu {PORT} portunda çalışıyor")
    httpd.serve_forever()
