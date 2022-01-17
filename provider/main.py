from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import CreateNftdataRequest
from database import get_db
from models import Nftdata

app = FastAPI()

#TAIA-X uses this API to fetch the real
@app.post("/download")
def check_ownership(nft_id: str, sig: str, db: Session = Depends(get_db)):
    #TODO ownership verification needs to be implemented here, also sig as an argument
    return db.query(Nftdata).filter(Nftdata.nft_id == nft_id).first()

# Providers API to upload data and mint NFT
@app.post("/upload")
def create(details: CreateNftdataRequest, db: Session = Depends(get_db)):
    #TODO mint a NFT and add the NFT id in the Nftdata as well
    to_create = Nftdata(
        data_filename=details.filename,
        path_to_data=details.location
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True
    }