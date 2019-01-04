from src.classes import network, db, backend, frontend, docker
from src.resources.config import APP_DIRECTORY, YES, COMMIT_NB
from src.classes.static.join import cmd, join
from src.classes.static.progress_bar import progress_bar
from src.resources.ascii.dora import DORA
from src.resources.ascii.bridged_ws import BRIDGED_WS
from src.resources.ascii.db_closed_port import DB_CLOSED_PORT
from src.resources.ascii.db_open_port import DB_OPEN_PORT
from src.resources.ascii.full_containerized import FULL_CONTAINERIZED
from src.resources.ascii.full_local import FULL_LOCAL
from src.resources.ascii.multi_instances import MULTI_INSTANCES
import subprocess

def start(demo=True):
    subprocess.run(["clear"])
    input("Welcome to this Docker presentation !")
    wait()
    input("Don't mind me, i'm just initializing a few things you will use later on, i'm at you in a few seconds...")
    db.build()
    subprocess.run(["clear"])
    wait()
    input("OK, done !")
    wait()
    if demo:
        input("We are going to go through the basics of Docker")
        input("While building a demo application until it is converted to a set of docker images that we will deploy and use as if it was a production server.")
        input("Let's go !!")

    wait()

    if (input("Do you want to go through the basic commands of Docker (ps, images, run, start, stop, etc.) ? [Y/N]) : ") in YES):
        wait()
        basic_commands()

    wait()

# MYSQL #
    input("First, Let's initialize a database container. It is a MySQL database, with pre-configured tables")
    input("I will not give you more details about it for now, as it might be easier to learn things with the applicative part of the project")
    input(f"But if you are curious about it, you'll find the Dockerfile and SQL scripts in this directory: {APP_DIRECTORY}/database")
    wait()
    db.run()
    wait()
    progress_bar()

# BACKEND #
  # Implement and test backend
    subprocess.run("clear")
    backend.implement()

    wait()
    if demo:
        input("Now that's some Java code (Kotlin), which consists in a minimalistic REST API for an application that handles some products.")
        input("You can have a look at the code here :")
        input(APP_DIRECTORY + "/ws-product")
        input("Let's package it, so we can launch and test it !!")

    wait()
    backend.package()
    wait()

    if demo:
        input("Packaging done, time to test the backend API !")
        input("Try to run this in an other terminal :")
    input(">>> java -jar {dir}/ws-product/target/<your jar>".format(dir = APP_DIRECTORY))
    wait()
    if demo:
        input("Are you done yet ?")

# ==> Oh shit, cannot connect to MySQL

        input("Didn't work well, did it ? Looking at the stacktrace, it seems that your backend cannot connect to the mysql running container...")
        input("Here, have a look at what is happening :")
    print(DB_CLOSED_PORT)
    wait()
    if demo:
        input("The application webserver is trying to communicate with the 3306 port, because it's configured to do so, when it requires a database access.")
        input("But by default, a docker container does not expose its ports on the host.")
        input("Let's stop this container and rerun it with its port (3306) open on our Host")

    db.stop()
    wait()
    db.run("db-product", "-p=3306:3306")
    progress_bar()
    wait()
    input("As you can see, we passed a parameter to the docker run command : '-p=3306:3306' which is a port forwarding that maps the port number of the app inside the container to expose it outside as an other port.")
    wait()

    if demo:
        input("Now, since the application is trying to reach a mysql instance on localhost:3306 (see properties of the backend app), it should work.")
    print(DB_OPEN_PORT)
    wait()

    if demo:
        input("Try running the jar in an other terminal again and see if it works.")
        input('''Remember the command ? It's :
>>> java -jar {dir}/ws-product/target/<your jar>'''.format(dir = APP_DIRECTORY))
        input("When it has started, come back here to test the API.")
        wait()
        input("Hehe, told you it would run !")
        input("Well, if not, sorry, but I'm just a script, I cannot do miracles...")
    input("Let's try to call our rest API from a terminal, using <curl>")
    backend.curl()
    wait()
    if demo:
        input("Yes, we did it !!!")
        input(DORA)
        wait()

# FRONTEND #
  # Implement and test frontend
    if demo:
        input("Now... We have a backend connected to a database running.")
        input("How about implementing a web client ?")
    subprocess.run("clear")

    frontend.implement()
    wait()
    if demo:
        input("You may have a look at the code over here :")
        input(APP_DIRECTORY + "/ui-product")
    input("Let's install its dependencies :")
    frontend.build()
    if demo:
        input("Time to test the web UI !")
        input("In order to keep this script running in this window, you should try to run it in an other terminal instance.")
        input("Try to run this command :")
        input(">>> npm run start --prefix {dir}/ui-product".format(dir = APP_DIRECTORY))
    wait()
    if demo:
        input("Done ? The web page should have launched in your default browser. If not, try visiting this url : http://localhost:3000")
    print(FULL_LOCAL)
    wait()
    if demo:
        input("Ok, all the application layers are now running.")
        input("We just hit the typical production-ready point for this demo application, if we didn't care about devops.")

    if input("Do you want some details about why we're going to use Docker ? [Y/N] : ") in YES:
        _docker_explanations()

    subprocess.run("clear")
    input("Now, please, stop the running instances of ws-product and ui.")
    if demo:
        input("We would like to get the 3000 port back, so we can redeploy the application.")
        input("And even though we should not require the 8080 port, we are going to let it open in the following solution, as explained earlier.")

# FIRST USE OF DOCKER
    # BACKEND
    input("Dockerize the backend !")
    wait()
    backend.build_docker_image()
    if demo:
        input("And run it with the port 8080 open, so we can curl on it.")
    backend.run("ws-product", "-p=8080:8080")
    progress_bar()
    wait()
    input("Let's try to call our containerized backend :")
    backend.curl()
    wait()
    if demo:
        input("hmmmm, it doesn't work...")
        input('''Do you have an idea why ?
    > ''')
        wait()
        input("Whatever, I can't read anyways :-)")
        wait()
        input("The webservice container cannot reach the mysql container, even though mysql exposes its port on localhost, and the web container is trying to reach it")
        input("because they are still running on the default bridge network")
    wait()
    if demo:
        input("The default network is convenient for quick bootstraping purposes.")
        input("But it comes with it flaws (cf Docker Docs), one of them being the containers it hosts cannot communicate with each other.")
    print(BRIDGED_WS)
    wait()
    network.ls()
    wait()
    input("We have to create a user-defined network :")
    network.create()
    wait()
    input("We are going to link the ws-product to the network. But first, we need to restart the application since it failed to start.")
    backend.stop()
    wait()
    if demo:
        input("The database is still running with its port open. We needed it because our containers were communicating through the host.")
        input("But we don't anymore, since all the containers on a docker user-defined network have all ports open on this network :")
    db.stop()
    wait()

    full_containerized_app()

    if demo:
        input("Great, now, we have a fully containerized application running.")
    print(FULL_CONTAINERIZED)
    wait()
    input("As a last step, in order to illustrate how we can make dockerized applications cohabitate on a unique server,")
    input("we are going to run multiple instances of our 'stack', as if it were distinct applications.")
    input("Each one of our instances will be identified by a color, to prove we are attacking distinct APIs, and displaying distinct interfaces.")
    wait()
    input("The problem is that a rest web server communicates through the 8080 port, by convention.")
    input("A web client may communicate on the 4000 or 3000 port, for instance.")
    input("But you cannot predict what port will be available on a given production server.")
    input("And as we previously explained, with Docker, we don't want to have to deal with such constraints.")
    input("We would rather want try to abstract them, so our stack can easily run anywhere, and be fully reproductible, portable, scalable.")
    input("The key for such a solution is Networking.")
    wait()

    input("We are going to modelize two other distinct apps running on our server, by slightly modifying our Product App :")
    input("Both replica will be identified by a color, which will be represented as the background of the web ui,")
    input("And the REST Api will prefix the products' names with this designated color.")
    wait()

    red_replica()
    wait()
    green_replica()
    print(MULTI_INSTANCES)
    wait()
    input("You can now verify that the application fronts are available on localhost, on ports numbers 3000, 4000 and 5000. That's all for now !")



def red_replica():
    subprocess.run(["git", "checkout", f"master~{COMMIT_NB - 5}"])
    app_replica("red", 4000, "172.16.2.1", "172.16.2.0/24")

def green_replica():
    subprocess.run(["git", "checkout", f"master~{COMMIT_NB - 6}"])
    app_replica("green", 5000, "172.16.3.1", "172.16.3.0/24")

def app_replica(color, port, gateway, subnet):
    input(f"We are building a {color} version of the Product App :")
    input("First, we need to create a dedicated network for the application :")
    network.create(f"{color}-product-network", f"{gateway}", f"{subnet}")
    db.run(f"{color}-db-product", f"--net={color}-product-network")
    backend.package()
    backend.build_docker_image(color + "-ws-product")
    backend.run(f"{color}-ws-product", f"--net={color}-product-network")
    frontend.build()
    frontend.build_docker_image(color + "-ui-product")
    frontend.run(f"{color}-ui-product", f"--net={color}-product-network", f"-p={port}:3000")


def full_containerized_app():
    input("First, we are going to run the database container on the newly created network.")
    wait()
    db.run("db-product", "--net=product-network")
    progress_bar()
    wait()
    input("No need to open its port, as containers on the same network can communicate with each others without it.")
    wait()
    input("Now, we are starting again the backend webservices application, with its port open, only so we can still curl it from outside the network (on localhost) and confirm that it is running")
    wait()
    backend.run("ws-product", "--net=product-network", "-p=8080:8080")
    progress_bar()
    backend.curl()
    wait()
    input("As expected, our containers can now communicate through the network.")
    wait()
    input("We can finally run the frontend container of the application, open for the outside on the port 3000 :")
    frontend.build_docker_image("ui-product")
    wait()
    frontend.run("ui-product", "--net=product-network", "-p=3000:3000")
    wait()



def basic_commands():
    input("Here are a few basic commands :")
    input("[docker ps] - will list your running containers.")
    input("It may take some arguments, like [-a] to list ALL containers, including those which are stopped.")
    wait()
    input("First, let's start a container :")
    wait()
    docker.run("alpine")
    wait()
    docker.ps()
    wait()
    input("Do not be afraid to read the docker documentation or at least have a look at it to get a more comprehensive overview of Docker. Like most things, that's probably the best way to master it !")
    input("You may already have a few containers running, at least the little one that we just launched.")
    input("You can already see that a container is identified by a unique [CONTAINER ID].")
    input("A container is a running instance of an [IMAGE]. A bit like an object is an istance of a class.")
    input("It has a [STATUS] (Up, stopped, starting, etc.) and a [NAME] so you can easily find it if you named it appropriately.")
    wait()
    input("Let's have a look at your docker images now :")
    wait()
    docker.images()
    wait()
    input("Like a container, an image has a unique [IMAGE ID].")
    input("But it often is easier to refer to its name, which is a combination of its [REPOSITORY] and [TAG] (you can have multiple versions of an image).")
    input("Feel free to run any of those commands, at any time.")
    input("But keep an other terminal open for this please, so you won't kill me :(")
    wait()
    input("Here is an other command : [docker run <image>].")
    input("It can take a LOT of arguments, and is used to create a container based on an image.")
    input("For this presentation, please, let me launch the containers for you.")
    input("I will always print the commands I launch with this indicator '>>>'")
    input("So try not to start any container yourself, as it could conflict with what I am doing, or restart me :-)")
    input("Moreover, if you appear to restart this demo, you'll have to remember to clear the environment that I have started, using the commands you will learn next")
    input("That means stopping and killing the containers that I have started, Otherwise, they will end up conflincting with the new instances that I will try to run during the subsequent demos")
    input("[docker run] will try to fetch an image on the DockerHub (which is a global repository) if you don't have this image in your docker root dir (/var/lib/docker).")
    input("[docker info] will give you more details about your docker installation.")
    wait()
    input("But you can pull an image without starting a container with [docker pull <image<:tag>>]")
    input("[docker stop <container>] will stop a container (and remove it if it was created with the [--rm] parameter).")
    input("[docker start <container>] will start a stopped container. You can refer to the container's name or id.")
    input("[docker rm <container>] to remove a stopped container and [docker kill <container>] to kill it.")

def _docker_explanations():
    input("Well, this setup provides many flaws :")

    input("- Our mysql container is now blocking the 3306 port on our host, which would not be convenient on a production server.")
    input("We'll soon see how we can improve this (networking).")
    wait()
    input("- Our backend app is blocking the 8080 port (web server port) which can be resolved with the same solution than before (we'll see how in the next part)")
    input("But in this presentation we'll probably keep our backend open to our host like this, so we can curl on it any time.")
    input("On a production server, you would probably want to only get access to your webserver's logs.")
    input("You could use the 'docker logs' command, or use a volume to get them on a directory on your host.")
    input("That way, you could stop exposing your webserver's port, and only give access to it through your web client, using to the networking solution.")
    wait()
    input("In order to be deployed to production,")
    input("We would have to manually setup quite a lot of things on that server.")
    wait()
    input("##### REPRODUCTIBILITY and SCALABILITY #####")
    wait()
    input("That includes defining environment variables, creating the appropriate filesystem, creating users, groups and their rights,")
    input("You will probably be using some specific version of Java, Javascript dependencies, or whatever version of a library.")
    input("Setting up all that stuff would be quite boring, right ?")
    input("And what about working on some serious customer environment ?")
    input("It could include a DEVELOPMENT environment, an internal TESTING environment, external TESTING, HOMOLOGATION, PRE-PRODUCTION, PRODUCTION...")
    input("Of course, on some of those environments, for scalability and safety reasons")
    input("There are multiple load-balanced servers that hosts the same applications.")
    input("Those duplicata multiplies how many times you will have to do the same setup.")
    input("You would need to automate a lot of things, and still be prepared to face a lot of unexpected issues, be it while deploying or at runtime.")
    wait()
    input("With Docker, EVERYTHING your application needs is either defined in the Dockerfile (meaning it will be embedded in your docker image once built)"),
    input("...or in the command you launch your containers with, for what is runtime specific.")
    input("You can declare those parameters in a docker-compose file, so you don't have to remember and repeat them over and over, or implement them in specific aliases and bash functions.")
    wait()
    input("That way, you can easily pull your set of docker images on any server with docker installed, run it, and you are done !")
    input("The entire definition of your application environment is embedded in an isolated set of Linux containers (LXC), which leads us to :")
    wait()
    input("##### ISOLATION #####")
    wait()
    input("Requiring a variable set of dependencies of versions is not the only issue :")
    input("Each one of them might create conflicts with what is already installed on the server.")
    input("Those conflicts might show up when the application starts, or at runtime.")
    input("Whereas with Docker, we are going to build a full packaging of everything our environment needs.")
    wait()
    input("An other issue is the ports used on the server :")
    input("You never think about it while you are working on your local environment, most of the time, when an application cannot start because the port is already busy,")
    input("you just shut the conflicting application down (it is often just an other instance of the same app, that you forgot to stop).")
    input("Of course, it is not even thinkable on a production server.")
    wait()
    input("Again, you would need to deal with many networking issues on each one of the servers you are deploying to.")
    input("Is this port free and open ? Why it is not, I just used it on the pre production environment...")
    input("There already is an instance of postgreSQL or Kafka running. Can I connect my application to it without any risk ?")
    input("Docker helps you easily resolving this issue while defining an isolated realm of containers. We'll soon see how.")
    wait()
    input("##### CONTINUOUS INTEGRATION (CI) #####")
    wait()
    input("Docker is a major devops tool and an ideal candidate for inclusion in a CI pipeline.")
    input("The dockerization of an application, its versioning on the DockerHub, or an artifactory instance, and the deployment on multiple production environments can be flawlessly integrated to a GitLab-CI or Jenkins pipeline, for instance...")

def wait():
    #input("...")
    #input("......")
    #input(".........")
    input('''
...
    ''')
