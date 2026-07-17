from api.schemas.usuario_schema import UsuarioCrear
from models.usuario import Usuario
from repositories.usuario_repository import obtener_usuarios, obtener_usuario_por_id, crear_usuario, eliminar_usuario, actualizar_usuario
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix= "/usuarios",
    tags= ["Usuarios"])

def convertir_usuario_a_diccionario(usuario):
    return{
        "id_usuario" : usuario.id_usuario,
        "nombres_usuario" : usuario.nombres_usuario,
        "apellidos_usuario" : usuario.apellidos_usuario,
        "docidentificacion" : usuario.docidentificacion,
        "correo_usuario" : usuario.correo_usuario,
        "contacto_usuario" : usuario.contacto_usuario,
        "fecha_registro" : usuario.fecha_registro
        
    }
    

@router.get("")
def mostrar_usuarios():
    usuarios = obtener_usuarios()
    
    usuarios_json = []
    
    for usuario in usuarios:
        usuarios_json.append(convertir_usuario_a_diccionario(usuario))
    return usuarios_json


@router.get("/{id_usuario}")
def mostrar_usuario_por_id(id_usuario : int):
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="No existe este usuario"
        )
    return convertir_usuario_a_diccionario(usuario)


@router.post("", status_code=201)
def crear_un_usuario(datos_usuario : UsuarioCrear):
    
    nuevo_usuario = Usuario(
        None,
        datos_usuario.nombres_usuario,
        datos_usuario.apellidos_usuario,
        datos_usuario.docidentificacion,
        datos_usuario.correo_usuario,
        datos_usuario.contacto_usuario,
        None
    )
    crear_usuario(nuevo_usuario)
    return {"mensaje" : "Usuario creado exitosamente."}


@router.delete("/{id_usuario}")
def borrar_usuario(id_usuario : int):
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe."
        )
    eliminar_usuario(id_usuario)
    return{"mensaje" : "Usuario eliminado exitosamente."}

@router.put("/{id_usuario}")
def actualizar_un_usuario(id_usuario : int, datos_usuario : UsuarioCrear):
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Ese usuario no existe."
        )
    usuario_actualizado = Usuario(
        id_usuario,
        datos_usuario.nombres_usuario,
        datos_usuario.apellidos_usuario,
        datos_usuario.docidentificacion,
        datos_usuario.correo_usuario,
        datos_usuario.contacto_usuario,
        usuario.fecha_registro
    )
    actualizar_usuario(usuario_actualizado)
    return{"mensaje" : "Usuario actualizado exitosamente."}