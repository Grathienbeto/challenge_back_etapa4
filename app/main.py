from fastapi import FastAPI, Depends

# from app.routes.character_routes import router as character_routes
from app.models.character_model import Character
from app.models.eye_color_model import EyeColor
import app.models
from app.database.db import engine, Base

app = FastAPI()
Base.metadata.create_all(bind= engine)


# app.include_router(character_routes, prefix='/characters', tags=['Characters'])


@app.get('/')
async def home():
    return {'message': 'Star Wars Character API'}