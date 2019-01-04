import subprocess
from .static.join import join, cmd
from ..resources.assets.color import bluet as blue

def ps(*args):
    command = ["docker", "ps"]
    input(cmd(command, blue(*args)))
    subprocess.run(command)

def images():
    command = ["docker", "images"]
    input(cmd(command))
    subprocess.run(command)

def run(image):
    subprocess.run(["docker", "run", "-dit", image])
