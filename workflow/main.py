import subprocess
import sys
from src.resources import config
from src.classes import network, db, backend, frontend
import workflow

# ==================================================
                     # GIT #
# ==================================================

def init(demo_mode=False):
    '''
    demo_mode: set to True for a complete docker demonstration, starting from a blank application environment (product app non existant and all required ports and network free)
    '''
    config.demo_mode = demo_mode
    if demo_mode:
        subprocess.run(["git", "checkout", f"master~{config.COMMIT_NB}"])
    workflow.start()

def implement_python_app():
    print("To start with, let's build a minimalistic REST WebService using Python+Flask")
    subprocess.run(["git", "checkout", f"master~{config.COMMIT_NB - 1}"])
    input("Now, launch it on this local environment")

# ==================================================
                    # DOCKER #
# ==================================================

def run():
    network.create()
    db.run("--net=product-network")
    backend.run("-p=8080:8080", "--net=product-network")
    frontend.run("-p=3000:3000", "--net=product-network")

def stop():
    subprocess.run(["docker", "stop", "mysql", "sqli-ws-product", "sqli-ui-product"])
    network.remove()

if __name__ == "__main__":
    args = sys.argv
    demo = True if len(args) == 1 or args[1] == "True" else False
    init(demo)
