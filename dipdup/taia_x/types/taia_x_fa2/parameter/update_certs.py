# generated by datamodel-codegen:
#   filename:  update_certs.json

from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel, Extra


class Certify(BaseModel):
    class Config:
        extra = Extra.forbid

    dataset_id: str
    hash: str


class UpdateCertsParameterItem(BaseModel):
    class Config:
        extra = Extra.forbid

    certify: Certify


class Reject(BaseModel):
    class Config:
        extra = Extra.forbid

    dataset_id: str
    hash: str


class UpdateCertsParameterItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    reject: Reject


class UpdateCertsParameter(BaseModel):
    __root__: List[Union[UpdateCertsParameterItem, UpdateCertsParameterItem1]]