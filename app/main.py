from fastapi import FastAPI, Depends

from app.routes.character_routes import router as character_routes
from app.routes.eye_color_routes import router as eye_color_routes
from app.models.character_model import Character
from app.models.eye_color_model import EyeColor
from app.database.db import engine, Base

app = FastAPI()
Base.metadata.create_all(bind= engine)


app.include_router(character_routes, prefix='/character', tags=['Characters'])
app.include_router(eye_color_routes, prefix='/eye_color', tags=['EyeColor'])


@app.get('/')
async def home():
    return {'message': 'Star Wars Character API'}