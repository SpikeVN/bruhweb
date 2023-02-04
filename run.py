import subprocess
import os

if __name__ == "__main__":
    subprocess.run("pc init", shell=True)
    subprocess.run("apt install npm", shell=True)
    subprocess.run("npm install -g next", shell=True)
    subprocess.run(f"pc run --port {os.environ['PORT']}", shell=True)
