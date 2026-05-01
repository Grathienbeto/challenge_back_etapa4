from app.database.db import engine, get_db, Base
from fastapi import FastAPI, Depends

from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()


Base.metadata.create_all(bind = engine)


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/')
async def home():
    return {'message': 'Star Wars Character API'}