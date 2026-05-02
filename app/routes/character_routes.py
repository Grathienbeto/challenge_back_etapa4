from starlette import status
from fastapi import APIRouter, Path, HTTPException

from app.schemas.character_schema import CharacterRequest, CharacterResponse
from app.services import character_services

from app.database.db import db_dependency


router = APIRouter()


@router.get('/getAll', status_code= status.HTTP_200_OK, response_model=list[CharacterResponse])
async def get_all_characters(db: db_dependency):
    all_characters = character_services.get_all_characters(db)
    return all_characters


@router.get('/eye_colors')
async def get_eye_colors(db: db_dependency):
    all_eye_colors = character_services.get_all_eye_colors(db)
    return all_eye_colors