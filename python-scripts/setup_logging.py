import subprocess
import configparser

NUMBER_NODES = 1

config = configparser.ConfigParser()

config.read('./ips.ini')

for idx in range(NUMBER_NODES):
    request = ["python3", "./python-scripts/logging_service.py", config["DEFAULT"][f"Logging-Service-{idx}"], config["DEFAULT"][f"Hazelcast-Node-{idx}"]]
    subprocess.run(request)
