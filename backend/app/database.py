from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata_obj = MetaData()

purchase = Table(
    'purchase', 
    metadata_obj,
    Column('token_id', Integer, primary_key=True),
    Column('account_id', String(60), nullable=False),
)

# SessionLocal will be used in a single request, and then close it once the request is finished.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()