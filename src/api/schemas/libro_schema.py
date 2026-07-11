from pydantic import BaseModel, Field


class LibroCrear(BaseModel):
    isbn: str = Field(..., min_length=13, max_length=13)
    titulo_libro: str = Field(..., min_length=1, max_length=150)
    id_autor: int = Field(..., gt=0)
    id_categoria: int = Field(..., gt=0)
    id_editorial: int = Field(..., gt=0)
    anio_lanzamiento: int = Field(..., ge=1440)
    existencias: int = Field(..., ge=0)