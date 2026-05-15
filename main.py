def write(file, text):
    with open(file, "w") as f:
        f.write(text)
        f.close

def read(file):
    with open(file, "r") as f:
        filecontents = f.read()
        f.close
        return filecontents