from pydantic import BaseModel


class CreateNftdataRequest(BaseModel):
    data_filename: str
    path_to_data: str