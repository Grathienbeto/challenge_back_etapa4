from starlette import status
from fastapi import APIRouter

from app.database.db import db_dependency
from app.services import eye_color_services


router = APIRouter()


@router.get('/getAll', status_code=status.HTTP_200_OK)
async def get_all_eye_colors(db: db_dependency):
    all_eye_colors = eye_color_services.get_all_eye_colors(db)
    return all_eye_colors