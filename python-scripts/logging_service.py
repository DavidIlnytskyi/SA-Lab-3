from fastapi import FastAPI
import uvicorn
import hazelcast
from domain import *
import sys

app = FastAPI()
distributed_map = None

@app.post("/")
def add_data(data: DataModel):
    distributed_map.set(data.uuid, data.msg)

    return {"msg": "success"}

@app.get("/")
def get_data():

    messages = distributed_map.entry_set()

    return {"messages": messages}

if __name__ == "__main__":
    host_url = sys.argv[1]
    hazelcast_url = sys.argv[2]

    client = hazelcast.HazelcastClient(
        cluster_members=[
            hazelcast_url,
        ]
    )

    distributed_map = client.get_map("my-distributed-map").blocking()

    uvicorn.run(app, host=host_url[:-5], port=int(host_url[-4:]))
