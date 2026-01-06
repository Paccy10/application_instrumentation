from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import start_http_server


class HandleRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes(
                "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>This is a Heading</h1><p>This is a paragraph.</p></body></html>",
                "utf-8",
            )
        )
        # self.wfile.close()


if __name__ == "__main__":
    # Start Prometheus metrics server on port 8083
    start_http_server(8083)

    # Start HTTP server on port 8082
    port = 8082
    server_address = ("localhost", port)
    server = HTTPServer(server_address, HandleRequests)

    print(f"Starting server on port {port}...")
    server.serve_forever()
