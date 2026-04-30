from pydantic import BaseModel, Field


class EyeColorRequest(BaseModel):
  
    eye_color: str = Field(min_length=2, max_length=50)