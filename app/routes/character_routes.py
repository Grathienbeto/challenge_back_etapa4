from starlette import status
from fastapi import APIRouter, Path, HTTPException

from app.schemas.character_schema import CharacterRequest, CharacterResponse
from app.services import character_services

from app.database.db import db_dependency


router = APIRouter()


@router.get('/getAll', status_code= status.HTTP_200_OK, response_model=list[CharacterResponse])
async def get_all_characters(db: db_dependency) -> list[CharacterResponse]:
    all_characters = character_services.get_all_characters(db)
    return all_characters


@router.get('/get/{name}', status_code=status.HTTP_200_OK)
async def get_character_by_name(db: db_dependency, 
                                name: str = Path(min_length=2, max_length=50)) -> CharacterRequest:
    character = character_services.get_character_by_name(db, name)
    if character is None:
        raise HTTPException(status_code=404, detail='Character name not found')
    return character
    
    
@router.get('/eye_colors')
async def get_eye_colors(db: db_dependency):
    all_eye_colors = character_services.get_all_eye_colors(db)
    return all_eye_colors