from pydantic import BaseModel, Field

class EditorialCrear(BaseModel):
    nombre_editorial: str = Field(...,)