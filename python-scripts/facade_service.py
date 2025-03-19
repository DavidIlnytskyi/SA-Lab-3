import requests
import sys
import uvicorn
import uuid
import json
from fastapi import FastAPI
from domain import *
from urllib.parse import urlparse

logging_url = None
messages_url = None

app = FastAPI()

@app.post("/")
def add_data(message: Message):
    uuid_val = uuid.uuid4()

    data = {"uuid": str(uuid_val), "msg": message.msg}

    response = requests.post(logging_url, json=data, timeout=3)
    
    if response.status_code == 200:
        print("Message sent successfully")
        return {"msg": "success"}
    
    return {"msg": "logging service mistake"}
    

@app.get("/")
def get_data():
    logging_service_response = requests.get(logging_url)
    logging_messages = json.loads(logging_service_response.content.decode("utf-8"))
    messages_service_response = requests.get(messages_url)
    messages_service_messages = json.loads(messages_service_response.content.decode("utf-8"))

    return {"logging_service_response": logging_messages, "messages_service_response": messages_service_messages}

if __name__ == "__main__":
    host_url = urlparse(sys.argv[1])
    logging_url = sys.argv[2]
    messages_url = sys.argv[3]

    uvicorn.run(app, host=host_url.hostname, port=host_url.port)
