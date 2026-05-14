import requests
import os
ip = requests.get("https://api.ipify.org").text
if os.path.exists("U1.txt") and os.path.getsize("U1.txt") == 0:
    with open("U1.txt", "w") as f:
        f.write(ip)
else:
    with open("U2.txt", "w") as f:
        f.write(ip)
f.close()