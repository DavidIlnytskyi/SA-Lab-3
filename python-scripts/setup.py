import subprocess
import configparser

NUMBER_NODES = 1

config = configparser.ConfigParser()

config.read('./ips.ini')

subprocess.run(["python3", "./python-scripts/facade_service.py", 
                config["DEFAULT"]["Facade-Service"], 
                config["DEFAULT"]["Logging-Service-0"],
                config["DEFAULT"]["Messages-Service"]
                ])

# for idx in range(NUMBER_NODES):
#     subprocess.run(["python3", "logging_service.py", config["DEFAULT"][f"Logging-Service-{idx}"], config["DEFAULT"][f"Hazelcast-Node-{idx}"]])
