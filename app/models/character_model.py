from app.database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(100), nullable=False)
    skin_color = Column(String(100), nullable=False)
    eye_color_id = Column(Integer, ForeignKey('eye_colors.id'), nullable= False)
    
    eye_color = relationship('EyeColor')