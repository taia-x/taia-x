from abc import ABC
from typing import Optional, List, Literal, Union

from pydantic import BaseModel, Field, root_validator


# Abstract class for all schema fields and content types in DigitalTwinInterface
class BaseContent(ABC, BaseModel):
    #TODO: raise error if field '@type' not implemented in child classes
    name: str = Field(min_length=1, max_length=64, regex='^[a-zA-Z](?:[a-zA-Z0-9_]*[a-zA-Z0-9])?$')
    id_field: Optional[str] = Field(max_length=2048, alias='@id')
    comment: Optional[str] = Field(max_length=512)
    description: Optional[str] = Field(max_length=512)
    display_name: Optional[str] = Field(max_length=64)


# helper function to generate '@type' field
def content_type_field(name: str) -> Field:
    return Field(default=name, alias='@type', regex=f'^{name}')


class Telemetry(BaseContent):
    type_field: str = content_type_field('Telemetry')
    schema_field: str = Field(alias='schema')  #TODO: implement -> https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#schemas
    unit: Optional[str]  #TODO: implement -> https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#semantic-types


class Property(BaseContent):
    type_field: str = content_type_field('Property')
    writable: Optional[bool]


class Command(BaseContent):
    type_field: Literal['Command'] = Field(alias='@type')
    command_type: Optional[str] # deprecated either `synchronous` or `asynchronous`
    request: Optional[str]  #TODO: implement -> https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#commandpayload
    response: Optional[str] #TODO: same as in request


class Relationship(BaseModel):
    #TODO: raise error if max_multiplicity < min_multiplicity
    type_field: Literal['Relationship'] = Field(alias='@type')
    min_multiplicity: Optional[int] = Field(default=0, ge=0)
    max_multiplicity: Optional[int] = Field(ge=1)
    properties: Optional[List[Property]] = Field(max_items=300)
    target: Optional[str] #TODO: implement
    writable: Optional[bool]


class Component(BaseModel):
    type_field: Literal['Component'] = Field(alias='@type')
    schema_field: str = Field(alias='schema')  #TODO: implement -> https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#schemas


class DigitalTwinInterface(BaseModel):
    #TODO: id is a DTMI, implement class following: https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#digital-twin-model-identifier
    id_field: str = Field(max_length=128, alias='@id') 
    type_field: Literal['Interface'] = Field(alias='@type')
    context: Literal['dtmi:dtdl:context;2'] = Field(alias='@context')
    comment: Optional[str] = Field(max_lenth=512)
    contents: Optional[List[Union[Telemetry, Property, Command, Relationship, Component]]] = Field(max_items=300)
    description: Optional[str] = Field(max_lenth=512)
    display_name: Optional[str] = Field(max_lenth=64)
    #TODO: make validations for extends and schemas
    extends: Optional[List[str]] = Field(max_items=2) #TODO: list of DTMI
    schemas: Optional[List[BaseContent]]


class OntologyInput(BaseModel):
    name: str = Field(max_length=128)
    ontology: DigitalTwinInterface
    