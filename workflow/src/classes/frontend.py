import subprocess
from ..resources.config import APP_DIRECTORY, COMMIT_NB, DEMO_MODE
import src.resources.config as config
from .static.join import join, cmd
from ..resources.assets.color import bluet as blue

def implement():
    input("Let's implement the client side of the product app :")
    input("Code in progress...")
    if config.DEMO_MODE:
      subprocess.run(["git", "checkout", f"master~{COMMIT_NB - 3}"])
    print("The client part of the most beautiful React frontend ever has just been pushed on our GitLab repo !")

def build():
    app_path = APP_DIRECTORY + "/ui-product"
    input(cmd(["yarn", app_path]))
    subprocess.run(["docker", "run", "-it", "--rm", "--name=npm-env", f"-v={app_path}:{app_path}", f"-w={app_path}", f"-u={config.UID}:{config.UID}", "node:8", "yarn"])

def start_local():
    input(f'''Launching the application on your local environment :
>>> npm run start''')
    subprocess.run(["npm", "run", "start", APP_DIRECTORY + "/ui-product"])

def build_docker_image(name):
    command = ["docker", "build", f"-t={name}", f"-f={APP_DIRECTORY}/ui-product/Dockerfile", f"{APP_DIRECTORY}/ui-product"]
    input(cmd(command))
    subprocess.run(command)

def run(image="ui-product", *args):
    '''
    -p 3000:3000
    --net product-network
    '''
    command = ["docker", "run", "-dit", "--rm", f"--name={image}", f"{image}"]
    input(cmd(command, blue(*args)))
    subprocess.run(join(command, *args))

def stop():
    command = ["docker", "stop", "ui-product"]
    input(cmd(command))
    subprocess.run(command)
