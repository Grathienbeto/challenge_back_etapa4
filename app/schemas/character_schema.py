from pydantic import BaseModel, Field


class CharacterRequest(BaseModel):
  
    name: str = Field(min_length=2, max_length=50)
    height: int = Field(gt=0, lt=500)
    mass: int = Field(gt=0, lt=2000)
    hair_color: str = Field(min_length=2, max_length=50)
    skin_color: str = Field(min_length=2, max_length=50)
    eye_color: int = Field(gt=0)
    
    model_config = {
        'json_schema_extra': {
            'example': {
                'name' : 'Kit Fisto',
                'height' : 196,
                'mass' : 87,
                'hair_color' : 'none',
                'skin_color' : 'green',
                'eye_color' : 'black',
                'birth_year' : 1999
            } 
        }
    }
    
    
    
class CharacterResponse(BaseModel):
    
    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    height: int = Field(gt=0, lt=500)
    mass: int = Field(gt=0, lt=2000)
    birth_year: int = Field(gt=0, lt=9999)