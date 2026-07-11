from fastapi import APIRouter, HTTPException
from api.schemas.autor_schema import AutorCrear
from models.autor import Autor
from repositories.autor_repository import obtener_autor_por_id, obtener_autores, crear_autor, eliminar_autor, actualizar_autor

router = APIRouter(
    prefix="/autores",
    tags=["Autores"])

def convertir_autor_a_diccionario(autor):
    return {
        "id_autor": autor.id_autor,
        "nombre_autor": autor.nombre_autor,
        "apellido_autor": autor.apellido_autor
    }

@router.get("")
def listar_autores():
    autores = obtener_autores()

    autores_json = []
    
    for autor in autores:
        autores_json.append(convertir_autor_a_diccionario(autor))
    
    return autores_json

@router.get("/{id_autor}")
def buscar_por_id(id_autor : int):
    autor = obtener_autor_por_id(id_autor)
    if autor is None:
        raise HTTPException(
            status_code= 404,
            detail="Ese autor no existe"
        )
    return convertir_autor_a_diccionario(autor)

@router.post("", status_code=201)
def crear_un_autor(datos_autor : AutorCrear):
    nuevo_libro = Autor(
        None,
        datos_autor.nombre_autor,
        datos_autor.apellido_autor
    )
    
    crear_autor(nuevo_libro)
    return{"mensaje" : "Autor creado existosamente."}

@router.delete("/{id_autor}")
def eliminar_un_autor(id_autor):
    autor = obtener_autor_por_id
    if autor is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese autor no existe"
        )
    eliminar_autor(id_autor)
    return {"mensaje" : "Autor eliminado exitosamente."}

@router.put("/{id_autor}")
def actualizar_datos(id_autor: int, datos_autor: AutorCrear):
    autor = obtener_autor_por_id(id_autor)

    if autor is None:
        raise HTTPException(
            status_code=404,
            detail="Ese autor no existe"
        )
    autor_actualizado = Autor(
        id_autor,
        datos_autor.nombre_autor,
        datos_autor.apellido_autor
    )
    actualizar_autor(autor_actualizado)
    return {"mensaje": "El autor ha sido actualizado correctamente"}