from http.server import BaseHTTPRequestHandler, HTTPServer
import json

FLAG = "FLAG{ARP_MITM_HEADER_CHANGED}"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.reply(200, {
                "message": "ARP MITM CTF server",
                "goal": "Send Lab-Token: modified"
            })
        elif self.path == "/flag":
            token = self.headers.get("Lab-Token", "")
            print(f"[server] client={self.client_address[0]} token={token!r}", flush=True)
            if token == "modified":
                self.reply(200, {"status": "success", "flag": FLAG})
            else:
                self.reply(403, {
                    "status": "blocked",
                    "hint": "The server only accepts Lab-Token: modified"
                })
        else:
            self.reply(404, {"error": "not found"})

    def reply(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[server-http] {self.client_address[0]} {fmt % args}", flush=True)

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
