import uvicorn

from fastapi import FastAPI

from . import models
from .db import SessionLocal, engine
from .core.ipfs import IPFSClient
from .core.config import IPFS_ADDRESS, IPFS_PORT


ipfs_client = IPFSClient(IPFS_ADDRESS, IPFS_PORT)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def connect_to_ipfs() -> None:
    ipfs_client.send_json({'message': 'hello world!'})

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
