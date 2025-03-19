import requests
import sys
import uvicorn
from random import randint
import uuid
import json
from fastapi import FastAPI
from domain import *
from urllib.parse import urlparse

messages_url = None
logging_urls = []

app = FastAPI()

def get_service_ips(service_name):
        try:
            response = requests.get(f"{config_server_url}/services/{service_name}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving {service_name} IPs: {e}")
            return []

@app.post("/")
def add_data(message: Message):
    uuid_val = uuid.uuid4()

    data = {"uuid": str(uuid_val), "msg": message.msg}

    logging_service_idx = randint(0, 2)
    response = requests.post(logging_urls[logging_service_idx], json=data, timeout=3)
    
    if response.status_code == 200:
        print("Message sent successfully")
        return {"msg": "success"}
    
    return {"msg": "logging service mistake"}
    

@app.get("/")
def get_data():
    logging_service_idx = randint(0, 2)

    logging_service_response = requests.get(logging_urls[logging_service_idx])
    logging_messages = json.loads(logging_service_response.content.decode("utf-8"))

    messages_service_response = requests.get(messages_urls[0])
    messages_service_messages = json.loads(messages_service_response.content.decode("utf-8"))

    return {"logging_service_response": logging_messages, "messages_service_response": messages_service_messages}

if __name__ == "__main__":
    host_url = urlparse(sys.argv[1])
    config_server_url = sys.argv[2]

    messages_url = get_service_ips("messages-service")
    logging_urls = get_service_ips("logging-service")

    print("Messages Service IPs:", messages_url)
    print("Logging Service IPs:", logging_urls)

    uvicorn.run(app, host=host_url.hostname, port=host_url.port)
