import subprocess
import configparser
import os
import signal

NUMBER_NODES = 3

config = configparser.ConfigParser()
config.read('./ips.ini')

def start_config_service():
    print(f"Starting config service...")

    try:
        request = ["python3", "./python-scripts/config_service.py", config["DEFAULT"]["Config-Service"]]
        return subprocess.Popen(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
    except Exception as e:
        print(f"Error starting server {idx}: {e}")
        return None

def start_messages_service():
    print("Starting messages service...")

    try:
        request = ["python3", "./python-scripts/messages_service.py", config["DEFAULT"]["Messages-Service"]]
        return subprocess.Popen(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
    except Exception as e:
        print(f"Error starting server {idx}: {e}")
        return None

def start_logging_service(idx):
    print(f"Starting logging service {idx}...")

    try:
        logging_service = config["DEFAULT"].get(f"Logging-Service-{idx}", "default_logging_service")
        hazelcast_node = config["DEFAULT"].get(f"Hazelcast-Node-{idx}", "default_hazelcast_node")
        
        request = ["python3", "./python-scripts/logging_service.py", logging_service, hazelcast_node]
        return subprocess.Popen(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
    except Exception as e:
        print(f"Error starting server {idx}: {e}")
        return None

if __name__ == "__main__":
    processes = []

    try:
        process = start_config_service()
        if process:
            processes.append(process)

        for idx in range(NUMBER_NODES):
            process = start_logging_service(idx)
            if process:
                processes.append(process)

        process = start_messages_service()
        if process:
            processes.append(process)

        while True:
            pass  

    except KeyboardInterrupt:
        print("\nShutting down all servers...")

        for process in processes:
            if process.poll() is None:
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)

        print("All servers stopped.")
