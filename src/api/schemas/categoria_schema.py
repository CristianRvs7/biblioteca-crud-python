from pydantic import BaseModel, Field

class CategoriaCrear(BaseModel):
    nombre_categoria : str = Field(..., min_length=1, max_length=50)