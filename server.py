from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

# Basic request handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Welcome to DevLab API"}).encode())
        
        elif self.path == '/lessons':
            with open('data/lessons.json', 'r') as file:
                lessons = json.load(file)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(lessons).encode())
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Page not found"}')

# Run the server
def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
