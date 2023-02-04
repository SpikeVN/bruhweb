import subprocess

if __name__ == "__main__":
    subprocess.run("pc init", shell=True)
    subprocess.run("pc run --env prod", shell=True)
