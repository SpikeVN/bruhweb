import subprocess

if __name__ == "__main__":
    subprocess.run(["pc", "init"])
    subprocess.run(["pc", "run", "--env", "prod"])
