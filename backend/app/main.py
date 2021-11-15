import uvicorn
from fastapi import FastAPI

from . import models
from .db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
