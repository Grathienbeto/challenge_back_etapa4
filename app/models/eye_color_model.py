from app.database.db import Base
from sqlalchemy import Column, Integer, String


class EyeColor(Base):
    __tablename__ = 'eye_colors'
    
    id = Column(Integer, primary_key= True, index= True)
    color = Column(String(100), nullable= False)