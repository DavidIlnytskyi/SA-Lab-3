from fastapi import FastAPI
import uvicorn
import sys
from domain import *

app = FastAPI()

@app.get("/")
def get_data():
    return {"msg": "Not implemented yet."}

if __name__ == "__main__":
    host_url = sys.argv[1]
    uvicorn.run(app, host=host_url[:-5], port=host_url[-5:])
