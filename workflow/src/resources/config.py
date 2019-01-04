import subprocess, pwd, getpass, os

HOME = subprocess.check_output("echo $HOME", shell=True).decode("utf-8").rstrip()
APP_DIRECTORY = f"{os.getcwd()}/product-app"
UID = pwd.getpwnam(getpass.getuser()).pw_uid
BLANK = " "

COMMIT_NB = 6
DEMO_MODE = True

YES = ["Y", "y", "O", "o"]
