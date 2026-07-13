from pydantic import BaseModel, Field, EmailStr

class UsuarioCrear(BaseModel):
    nombres_usuario : str = Field(..., min_length=1, max_length=50)
    apellidos_usuario : str = Field(..., min_length=1, max_length=50)
    docidentificacion : str = Field(..., min_length=1, max_length=20)
    correo_usuario : EmailStr
    contacto_usuario : str = Field(..., min_length=1, max_length=20)
    
    