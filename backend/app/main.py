import uvicorn

import glob
import socket

from datetime import datetime
from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from uuid import uuid4
from pathlib import Path

from .database import SessionLocal, engine
from .utils import signature_verification


app = FastAPI()

origins = ["*"]

# add cors middleware to allow cors requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AuthData(BaseModel):
    nft_id: str
    sig: str
    pbkey: str


# get digital twin data by unique id
@app.post("/download/{unique_id}")
async def fetch_data(unique_id: int, data: AuthData, db: Session = Depends(get_db)):
    # hash pbkey and check if it matches to account address that purchased nft_id
    if signature_verification(**data, db):
        file = glob.glob(f'assets/{unique_id}/*.zip')[0]
        return file
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


# upload new digital twin data and save on file system
@app.post("/upload")
async def upload(archive: UploadFile = File(...)):
    supported_formats = ['zip']
    if archive.content_type.split("/")[1] in supported_formats:
        uid = str(uuid4())
        store_path = f"assets/{uid}/"
        Path(store_path).mkdir(parents=True, exist_ok=True)
        data_path = store_path + 'Archive_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.zip'
        with open(data_path, "wb+") as zip_file:
            zip_file.write(archive.file.read())
        return {
            "artifactUri": f"http://localhost:8000/download/{uid}"
            # returns artifactUri to be stored in token metadatafile
        }
    else:
        return {
            "error": "Unsupported file format! Please upload either zip or rar file."
        }


@app.get("/health")
async def health():
    return "healthy"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
