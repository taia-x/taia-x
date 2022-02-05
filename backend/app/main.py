import uvicorn

import glob
import socket

from datetime import datetime
from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from uuid import uuid4
from pathlib import Path

from .database import get_db, purchase
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
    proof = dict(data)
    try:
        buyer = signature_verification(**proof)
    except ValueError:
        raise HTTPException(status_code=403, detail="Forbidden")

    # check that the given token is in the DB 
    try:
        token_was_bought = db.query(purchase) \
            .filter(purchase.c.nft_id==data.nft_id, purchase.c.buyer==buyer) \
            .one()
    except NoResultFound as e:
        print(f'Given token was not found: {e}')
        raise HTTPException(status_code=403, detail="Forbidden")
    except MultipleResultsFound as e:
         print(f'Multiple results were found: {e}')
         raise HTTPException(status_code=403, detail="Forbidden")
    
    # check that requested_file exists
    files_found = glob.glob(f'assets/{unique_id}/*.zip')
    if len(files_found) < 1:
        raise HTTPException(status_code=404, detail="Not Found")

    return files_found[0]
    
        

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
