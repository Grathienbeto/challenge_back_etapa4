from starlette import status
from fastapi import APIRouter, Path, HTTPException

from app.schemas.character_schema import CharacterRequest, CharacterResponse
from app.services import character_services


# router = APIRouter()


# @router.get('/getAll', status_code= status.HTTP_200_OK, response_model=list[CharacterResponse] )
# async def get_all_characters():
#     all_characters = character_services.get_all_characters()
#     return all_characters