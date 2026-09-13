from http.server import BaseHTTPRequestHandler, HTTPServer
import time



class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/flag":

            flag = "FLAG{ARP_SPOOFING_LAB}"

            print(f"[Server] Sending flag to {self.client_address}")

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(flag.encode())

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Flag server running on port 8080")

server.serve_forever()