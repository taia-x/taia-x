import uvicorn

from fastapi import FastAPI

from . import models
from .db import SessionLocal, engine
from .routers import ontologies


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ontologies.router)


@app.get("/health")
async def health():
    return 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
