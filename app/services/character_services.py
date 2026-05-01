from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.character_model import Character


db_dependency = Annotated[Session, Depends(get_db)]   


def get_all_characters(db: db_dependency = db_dependency):
    return db.query(Character).all()