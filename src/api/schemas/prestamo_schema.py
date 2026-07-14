from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal


class PrestamoCrear(BaseModel):
    id_usuario: int = Field(gt=0)
    id_libro: int = Field(gt=0)
    fecha_limite: datetime


class PrestamoActualizar(BaseModel):
    fecha_limite: datetime
    fecha_devolucion: datetime | None = None
    estado: Literal["Activo", "Devuelto", "Vencido"]