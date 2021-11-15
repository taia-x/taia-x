from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Ontology(Base):
    __tablename__ = "ontologies"

    id = Column(Integer, primary_key=True, index=True)
    ontology_addr = Column(String, unique=True, index=True)
