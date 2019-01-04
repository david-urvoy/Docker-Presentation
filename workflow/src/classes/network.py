import subprocess
from .static.join import join, cmd

def create(name="product-network", gateway="172.16.1.1", subnet="172.16.1.0/24"):
    command = ["docker", "network", "create", f"--gateway={gateway}", f"--subnet={subnet}", f"{name}"]
    input(f"Creating a network '{name}' for our containers !")
    input(cmd(command))
    subprocess.run(command)

def remove():
    command = ["docker", "network", "rm", "product-network"]
    subprocess.run(command)

def ls():
    command = ["docker", "network", "ls"]
    input(cmd(command))
    subprocess.run(command)

def connect(network, container):
    command = ["docker", "network", "connect", network, container]
    subprocess.run(command)
