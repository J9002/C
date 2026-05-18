from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/run")
def run_script():
    with open("input.txt", "w") as f:
        f.write("hello world")

    subprocess.run(["python3", "api/run.py"], check=True)

    if os.path.exists("output.txt"):
        with open("output.txt") as f:
            return {"output": f.read()}
    return {"error": "output.txt not found"}