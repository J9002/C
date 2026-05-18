def write(file, text):
    with open(f"/workspaces/C/api/{file}", "w") as f:
        f.write(text)
        f.close