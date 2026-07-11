from pydantic import BaseModel, Field

class AutorCrear(BaseModel):
    nombre_autor: str = Field(..., min_length=1, max_length=50)
    apellido_autor: str = Field(..., min_length=1, max_length=50)