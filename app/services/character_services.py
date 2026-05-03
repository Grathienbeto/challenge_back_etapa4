from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.character_model import Character
from app.schemas.character_schema import CharacterRequest

from app.services import eye_color_services


def get_all_characters(db: Session):
    return db.query(Character).all()



def get_character_by_name(db: Session, name: str):
    character = db.query(Character).filter(Character.name.ilike(name)).first()
    
    return character



def create_character(db: Session, character: CharacterRequest):
    new_character = Character(**character.model_dump())

    # corroborar que existe el color de ojo
    validate_eye_color_exist(db, new_character.eye_color_id)

    # corroborar que no existe el personaje dependiendo el nombre
    validate_name_exist(db, new_character.name)
    
    # crear personaje
    db.add(new_character)
    db.commit()
    return new_character
    
    
    


def validate_eye_color_exist(db: Session, eye_color_id: int):
    eye_color = eye_color_services.get_eye_color_by_id(db, eye_color_id)
    if not eye_color:
        raise HTTPException(status_code=400, detail='Eye color not found')
    return eye_color


def validate_name_exist(db: Session, name: str):
    character = get_character_by_name(db, name)
    if character is not None:
        raise HTTPException(status_code=400, detail='Character name already used')
    