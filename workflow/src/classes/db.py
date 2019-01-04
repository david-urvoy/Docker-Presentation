import subprocess
import sys
from .static.join import join, cmd
from ..resources.config import APP_DIRECTORY, COMMIT_NB
from ..resources.assets.color import bluet as blue

NAME = "db-product"

def checkout():
    subprocess.run(["git", "checkout", f"master~{COMMIT_NB - 1}"])

def build():
    subprocess.run(["docker", "build", f"-t=db-product", f"-f={APP_DIRECTORY}/database/Dockerfile", f"{APP_DIRECTORY}/database/"])

def connect(network):
    command = ["docker", "network", "connect", f"{network}", "db-product"]
    input(cmd(command))
    subprocess.run(command)

def run(name = None, *args):
    '''
    --net=product-network
    -p 3306:3306
    '''
    global NAME
    if name == None:
        name = NAME
    command = ["docker", "run", "-dit", "--rm", f"--name={name}", "-e=MYSQL_ROOT_PASSWORD=root", "-e=MYSQL_USER=product", "-e=MYSQL_PASSWORD=product", "db-product"]
    input(cmd(command, blue(*args)))
    subprocess.run(join(command, *args))

def stop(name = None):
    global NAME
    if name == None:
        name = NAME
    command = ["docker", "stop", f"{name}"]
    input(cmd(command))
    subprocess.run(command)

if __name__ == "__main__":
    run(*sys.args[1:])
