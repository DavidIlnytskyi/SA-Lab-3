from fastapi import FastAPI
import requests
import sys
import uvicorn
import uuid
import json
from domain import *
from urllib.parse import urlparse


MAX_RETRIES = 3
RETRY_DELAY = 2

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
    logging_response = requests.get(logging_url)
    logging_messages = json.loads(logging_response.content.decode("utf-8"))
    # messages_response = requests.get(messages_url)

    # "Messages response": messages_response.json()["msg"]

    return {"logging_response": logging_messages}

if __name__ == "__main__":
    host_url = urlparse(sys.argv[1])
    logging_url = sys.argv[2]
    messages_url = sys.argv[3]

    uvicorn.run(app, host=host_url.hostname, port=host_url.port)
