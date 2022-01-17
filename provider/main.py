from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import CreateNftdataRequest
from database import get_db
from models import Nftdata

app = FastAPI()

@app.post("/download")
def check_ownership(nft_id: str, sig: str, db: Session = Depends(get_db)):
    #TODO ownership verification needs to be implemented here, also sig as an argument
    return db.query(Nftdata).filter(Nftdata.nft_id == nft_id).first()

@app.post("/")
def create(details: CreateNftdataRequest, db: Session = Depends(get_db)):
    to_create = Nftdata(
        data_filename=details.filename,
        path_to_data=details.location
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.filename
    }