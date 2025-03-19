import subprocess
import configparser

NUMBER_NODES = 1

config = configparser.ConfigParser()

config.read('./ips.ini')

subprocess.run(["python3", "./python-scripts/messages_service.py", config["DEFAULT"]["Messages-Service"]])
