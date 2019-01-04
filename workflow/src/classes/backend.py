import subprocess
from ..resources.config import HOME, APP_DIRECTORY, COMMIT_NB, DEMO_MODE
from .static.join import cmd, join
from ..resources.assets.color import bluet as blue
import src.resources.config as config

def implement():
    input("Let's implement a REST API for a product app :")
    if DEMO_MODE:
        subprocess.run(["git", "checkout", f"master~{COMMIT_NB - 2}"])
    subprocess.run("clear")
    input("Coding in progress...")
    print("The dev team just finished implementing the Kotlin REST webservices for the Product Application !")

def package():
    input("Packaging the application as a jar")
    input("You will find it in the /target folder :")
    input(f"{APP_DIRECTORY}/ws-product/target")
    input("Note : I did not have time to optimize the project pom at all, so the following might take some time, sorry by advance :'(")
    app_path = f"{APP_DIRECTORY}/ws-product"
    input(f">>> mvn package -f {app_path}")
    subprocess.run(["docker", "run", "-it", "--rm", "--name=maven-env", f"-v={HOME}/.m2:/var/maven/.m2", f"-v={app_path}:{app_path}", f"-w={app_path}", f"-u={config.UID}:{config.UID}", "maven" , "mvn", "package"])
    input("Finished compiling !!")
    ls_command = ["ls", "-al", app_path]
    input(cmd(ls_command))
    subprocess.run(ls_command)

def start_local():
    input("Launching the application on your local environment :")
    input(f">>> java -jar {APP_DIRECTORY}/ws-product/target/product-app-0.0.1-SNAPSHOT.jar")
    subprocess.run(["java", "-jar", f"{APP_DIRECTORY}/ws-product/target/product-app-0.0.1-SNAPSHOT.jar"])

def build_docker_image(name="ws-product"):
    command = ["docker", "build", f"-t={name}", f"-f={APP_DIRECTORY}/ws-product/Dockerfile", f"{APP_DIRECTORY}/ws-product/"]
    input(cmd(command))
    subprocess.run(command)

def run(image="ws-product", *args):
    ''' -p=8080:8080 --net=product-network --ip=172.17.0.10 '''
    command = ["docker", "run", "-dit", "--rm", f"--name={image}", "-e=SPRING_PROFILES_ACTIVE=dev", image]
    input(cmd(command, blue(*args)))
    subprocess.run(join(command, *args))

def curl():
    curl = ["curl", "http://localhost:8080/product"]
    if DEMO_MODE:
        input("We are going to use the GET endpoint /product to get all the elements.")
        input("But feel free to test any endpoint defined in the ProductController class.")
    input(cmd(curl))
    subprocess.run(curl)

def stop():
    command = ["docker", "stop", "ws-product"]
    input(cmd(command))
    subprocess.run(command)
