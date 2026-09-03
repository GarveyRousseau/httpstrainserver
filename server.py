#!/usr/bin/env python3
"""Plain HTTPS server - just serves files in this folder via HTTPS"""
import http.server
import ssl
import os

HOST = "0.0.0.0"
PORT = 4443
CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

class Handler(http.server.SimpleHTTPRequestHandler):
    # log requests to console so you can see HTTP in action
    def log_message(self, format, *args):
        print(f"{self.client_address[0]} - {format % args}")

    def end_headers(self):
        # no cache so you always see fresh requests
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

# generate cert if missing
if not (os.path.exists(CERT_FILE) and os.path.exists(KEY_FILE)):
    print("Generating self-signed cert...")
    os.system(f'openssl req -x509 -newkey rsa:2048 -keyout {KEY_FILE} -out {CERT_FILE} -days 365 -nodes -subj "/CN=localhost"')

httpd = http.server.HTTPServer((HOST, PORT), Handler)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(CERT_FILE, KEY_FILE)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print(f"\nServing plain site at https://localhost:{PORT}/")
print(f"Files: index.html, hello.html - just open in browser via https://")
print(f"For group: https://<your-ip>:{PORT}/  (browser will warn about cert -> Advanced -> Proceed)")
print("Press Ctrl+C to stop\n")

httpd.serve_forever()
