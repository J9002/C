from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
from main import write

write("U1.txt", "")
count = 0

def run_script():
    subprocess.run(["python3", "script.py"])

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global count

        if self.path == "/" and count < 2:
            count += 1
            run_script()
        return super().do_GET()

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()
=