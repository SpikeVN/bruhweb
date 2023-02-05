import subprocess
import os

if __name__ == "__main__":
    subprocess.run("pip3 install -r requirements.txt", shell=True)
    subprocess.run("curl -fsSL https://deb.nodesource.com/setup_16.x | bash -", shell=True)
    subprocess.run("apt install -y nodejs", shell=True)
    subprocess.run("pc init", shell=True)
    subprocess.run("apt install npm", shell=True)
    subprocess.run("npm install -g next @chakra-ui/descendant", shell=True)
    subprocess.run(f"pc run --port {os.environ['PORT']} --env prod", shell=True)
