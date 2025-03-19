from fastapi import FastAPI
import uvicorn
import hazelcast
from domain import *
import sys

app = FastAPI()
messages = dict()

@app.post("/")
def add_data(data: DataModel):
    distributed_map = client.get_map("my-distributed-map").blocking()

    if data.uuid in messages.keys():
        print(f"UUID Duplication for msg: {data.msg}")
        return {"msg": "duplication"}

    messages[data.uuid] = data.msg

    distributed_map.set(data.uuid, data.msg)

    return {"msg": "success"}

@app.get("/")
def get_data():
    distributed_map = client.get_map("my-distributed-map").blocking()

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

    uvicorn.run(app, host=host_url[:-5], port=int(host_url[-4:]))
