from starlette import status
from fastapi import APIRouter, Path, HTTPException

from app.database.db import db_dependency
from app.schemas.character_schema import CharacterRequest, CharacterResponse, CharacterResponseComplete
from app.services import character_services



router = APIRouter()


@router.get('/getAll', status_code= status.HTTP_200_OK, response_model=list[CharacterResponse])
async def get_all_characters(db: db_dependency) -> list[CharacterResponse]:
    all_characters = character_services.get_all_characters(db)
    return all_characters



@router.get('/get/{name}', status_code=status.HTTP_200_OK)
async def get_character_by_name(db: db_dependency, 
                                name: str = Path(min_length=2, max_length=50)) -> CharacterResponseComplete:
    character = character_services.get_character_by_name(db, name)
    if character is None:
        raise HTTPException(status_code=404, detail='Character name not found')
    return character



@router.post('/add', status_code=status.HTTP_201_CREATED)
async def create_character(db: db_dependency,
                           character_request: CharacterRequest):
    character_services.create_character(db, character_request)

    