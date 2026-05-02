from app.database.db import db_dependency
from app.models.character_model import Character
from app.models.eye_color_model import EyeColor
from sqlalchemy.orm import Session


def get_all_characters(db: Session):
    return db.query(Character).all()

def get_all_eye_colors(db: Session):
    return db.query(EyeColor).all()