from typing import Optional

from fastapi import FastAPI, Depends, File, UploadFile
from functools import lru_cache
import config
from uuid import uuid4
from pathlib import Path
# from sqlalchemy.orm import Session
# from schemas import CreateNftdataRequest
# from database import get_db
# from models import Nftdata

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()

#TAIA-X uses this API to fetch the real
@app.post("/download/{unique_id}")
def fetch_data(nft_id: str, sig: str, pbkey: str):
    #TODO ownership verification needs to be implemented here, also sig as an argument
    data_path = f'assets/{unique_id}'

# Providers API to upload data and mint NFT -> multiple files
#TODO Check file format if it's zip or not and respond accordingly
@app.post("/upload/")
async def upload(datafile: UploadFile = File(...), settings: config.Settings = Depends(get_settings)):
    uid = str(uuid4())
    store_path = f"assets/{uid}/"
    Path(store_path).mkdir(parents=True, exist_ok=True)
    data_path = store_path + datafile.filename
    with open(data_path, "wb+") as file_object:
        file_object.write(datafile.file.read())
    return {
        "success": f"{settings.app_server}/download/{uid}" #this will be visible only once
    }