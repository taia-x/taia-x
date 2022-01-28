import uvicorn
import pysodium
from datetime import datetime
from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from uuid import uuid4
from pathlib import Path
from pyblake2 import blake2b
from encoding import scrub_input, base58_decode, base58_encode

import glob
import socket

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


def public_key_hash(public_point) -> str:
    """Creates base58 encoded public key hash for this key.

    :returns: the public key hash for this key
    """
    pkh = blake2b(data=public_point, digest_size=20).digest()
    prefix = b'tz1'
    return base58_encode(pkh, prefix).decode()


# get digital twin data by unique id
@app.post("/download/{unique_id}")
async def fetch_data(unique_id: int, data: AuthData):
    results = {"unique_id": unique_id}
    # results = {"unique_id": unique_id, "nft_id": data.nft_id, "sig": data.sig, "public key": data.pbkey}
    results.update({"data": data})
    print(results)

    # hash pbkey and check if it matches to account address that purchased nft_id
    pbk = scrub_input(data.pbkey)
    pbk2 = base58_decode(pbk)
    pkh = blake2b(data=pbk2, digest_size=20).digest()
    prefix = b'tz1'
    pbh2 = base58_encode(pkh, prefix).decode()
    pbh_of_buyer = ""  # to be called from database
    print("Check matching onchain PBK from buyer with consumer pbk..")
    if pbh2 == pbh_of_buyer:
        print("Verified account!")
    else:
        print("Not the same account!")
        # Change to return, but for test purposes, pass
        pass

    # verify signature to check authenticity of requester
    signature = scrub_input(data.sig)
    message = scrub_input(data.nft_id)

    signature = base58_decode(signature)

    digest = pysodium.crypto_generichash(message)
    try:
        pysodium.crypto_sign_verify_detached(signature, digest, pbk2)
    except ValueError:
        raise ValueError('Signature is invalid.')
    print("Signature is valid!")

    # file = glob.glob(f'assets/{unique_id}/*.zip')[0]
    return None  # return file


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
