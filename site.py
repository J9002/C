from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
from main import write

write("U1.txt", "")
count = 0

def run_script():
    subprocess.run(["python3", "IP.py"])

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        global count

        if self.path == "/" and count < 2:
            count += 1
            run_script()

        return super().do_GET()

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()