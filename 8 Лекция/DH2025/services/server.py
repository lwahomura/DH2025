import os
import socketserver
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        api_key = os.getenv("API_KEY")

        req = urlparse(self.path)
        params = parse_qs(req.query)
        if params.get('api_key')[0] != api_key:
            self.send_response(401)
            self.end_headers()
            return

        if req.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(bytes('{"message": "Hello World!"}', "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

class Server:
    def __init__(self, config):
        self.address, self.port = config.get_addr_and_port()

    def run(self):
        with socketserver.TCPServer((self.address, self.port), Handler) as httpd:
            print("serving at port", self.port)
            httpd.serve_forever()