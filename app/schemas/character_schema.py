from pydantic import BaseModel, Field, field_validator


class CharacterRequest(BaseModel):
  
    name: str = Field(min_length=2, max_length=50)
    height: int = Field(gt=0, lt=500)
    mass: int = Field(gt=0, lt=2000)
    hair_color: str = Field(min_length=2, max_length=50)
    skin_color: str = Field(min_length=2, max_length=50)
    eye_color: str
    
    class Config:
        from_attributes = True
        
    @field_validator('eye_color', mode='before')
    @classmethod
    def extract_eye_color(cls, value): #(class, value)
        if hasattr(value, 'color'):
            return value.color
        return value
    
    
    
class CharacterResponse(BaseModel):
    
    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    height: int = Field(gt=0, lt=500)
    mass: int = Field(gt=0, lt=2000)
    eye_color: str
    
    class Config:
        from_attributes = True
        
    @field_validator('eye_color', mode='before')
    @classmethod
    def extract_eye_color(cls, value): #(class, value)
        if hasattr(value, 'color'):
            return value.color
        return value
    
    
## 1. SQLAlchemy query returns a Character object
# character = db.query(Character).first()
# character.eye_color is an EyeColor object, not a string!

# 2. You create the response
# response = CharacterResponse.model_validate(character)

# 3. Pydantic processes each field:
#    - id, name, height, mass → direct copy from character attributes
#    - eye_color → triggers the validator!

# 4. The validator runs:
#def extract_eye_color(cls, v):
    # v = EyeColor(id=1, color='blue')  ← the relationship object
    #if hasattr(v, 'color'):  # Does v have a 'color' attribute?
    #    return v.color  # Return 'blue' (string)
    #return v  # Fallback if v is already a string

# 5. Final result:
# CharacterResponse(id=1, name="Luke", height=172, mass=77, eye_color="blue")
