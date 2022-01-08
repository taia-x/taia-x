# generated by datamodel-codegen:
#   filename:  mint.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra


class MintParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    operator: Optional[str]
    owner: str
    token_metadata_uri: str