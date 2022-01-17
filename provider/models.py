from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Nftdata(Base):
    __tablename__ = "nftdata"

    id = Column(String, primary_key=True)
    nft_id = Column(String, nullable=True)
    data_filename = Column(String, nullable=False)
    path_to_data = Column(String, nullable=False)

