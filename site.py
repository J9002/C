from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
from main import write

write("U1.txt", "")
write("U2.txt", "")
count = 0

def run_script():
    subprocess.run(["python3", "IP.py"])

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global count
        if count < 2:
            count += 1
            run_script()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()