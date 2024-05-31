#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        data = {"name": "John", "age": 30, "city": "New York"}
        info = {"version": "1.0", "description": "A simple API built with http.server"}

        if self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response_json = json.dumps(data)
            self.wfile.write(response_json.encode())
            return

        if self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return
            
        if self.path == '/info':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response_json = json.dumps(info)
            self.wfile.write(response_json.encode())
            return

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"404 Not Found")
 

def run(server_class=HTTPServer, handler_class=SimpleBaseHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()
if __name__ == '__main__':
    run()