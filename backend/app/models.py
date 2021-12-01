from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session

from .db import Base


class Ontology(Base):
    __tablename__ = "ontologies"

    id = Column(Integer, primary_key=True, index=True)
    ontology_addr = Column(String, unique=True, index=True)

#TODO: make a cleaner get_or_create function
def get_or_create_ontology(db: Session, hash_address: str) -> (Ontology, bool):
    exists = db.query(Ontology).filter_by(ontology_addr=hash_address).one_or_none()
    if exists:
        return exists, False
    else:
        db_ontology = Ontology(ontology_addr=hash_address)
        db.add(db_ontology)
        db.commit()
        db.refresh(db_ontology)
        return db_ontology, True