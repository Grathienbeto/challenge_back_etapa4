from app.models.eye_color_model import EyeColor
from app.schemas.eye_color_schema import EyeColorRequest
from sqlalchemy.orm import Session


def get_all_eye_colors(db: Session):
    return db.query(EyeColor).all()


def get_eye_color_by_id(db: Session, id: int):
    eye_color = db.query(EyeColor).filter(EyeColor.id == id).first()
    return eye_color
