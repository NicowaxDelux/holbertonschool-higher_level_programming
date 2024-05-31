#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        data = {"name": "John", "age": 30, "city": "New York"}
        info = {"version": "1.0", "description": "A simple API built with http.server"}

        try:
            if self.path == '/data':
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                response_json = json.dumps(data)
                self.wfile.write(response_json.encode('utf-8'))
                
            if self.path == '/info':
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                response_json = json.dumps(info)
                self.wfile.write(response_json.encode('utf-8'))

            if self.path == '/':
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")
        except:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
 

httpd = HTTPServer(('', 8000), SimpleBaseHTTPRequestHandler)
httpd.serve_forever()