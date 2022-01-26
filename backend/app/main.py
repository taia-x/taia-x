import uvicorn

from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.responses import FileResponse
from uuid import uuid4
from pathlib import Path
import glob
import socket

app = FastAPI()

#TAIA-X uses this API to fetch the data
@app.post("/download/{unique_id}")
def fetch_data(unique_id: str, nft_id: str, sig: str, pbkey: str):
    #TODO ownership verification needs to be implemented here, also sig as an argument
    file = glob.glob(f'assets/{unique_id}/*.zip')[0]
    return FileResponse(file)


# Providers API to upload data and mint NFT -> multiple files not handled
@app.post("/upload/")
async def upload(datafile: UploadFile = File(...)):
    supported_formats = ['zip', 'rar']
    if datafile.content_type.split("/")[1] in supported_formats:
        uid = str(uuid4())
        store_path = f"assets/{uid}/"
        Path(store_path).mkdir(parents=True, exist_ok=True)
        data_path = store_path + datafile.filename
        with open(data_path, "wb+") as file_object:
            file_object.write(datafile.file.read())
        return {
            "success": f"http://localhost:8000/download/{uid}" #this will be visible only once
        }
    else:
        return {
            "error": "Please upload either zip or rar file"
        }

@app.get("/health")
async def health():
    return

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
