from api.schemas.categoria_schema import CategoriaCrear
from models.categoria import Categoria
from repositories.categoria_repository import obtener_categoria, obtener_categoria_id, crear_categoria, eliminar_categoria, actualizar_categoria
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"])

def convertir_categoria_a_diccionario(categoria):
    return {
        "id_categoria" : categoria.id_categoria,
        "nombre_categoria" : categoria.nombre_categoria
    }
    

@router.get("")
def mostrar_categorias():
    categorias = obtener_categoria()
    
    categorias_json = []
    
    for categoria in categorias:
        categorias_json.append(categoria)
    
    return categorias_json


@router.get("/{id_categoria}")
def mostrar_categoria_por_id(id_categoria: int):
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="No existe esa categoria"
        )
    return convertir_categoria_a_diccionario(categoria)


@router.post("", status_code=201)
def crear_nueva_categoria(datos_categoria : CategoriaCrear):
    nueva_categoria = Categoria(
        None,
        datos_categoria.nombre_categoria
    )
    crear_categoria(nueva_categoria)
    return {"mensaje" : "Categoria creada correctamente"}


@router.delete("/{id_categoria}")
def borrar_categoria(id_categoria : int):
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail= "Esa categoria no existe"
        )
    eliminar_categoria(id_categoria)
    return {"mensaje" : "La categoria ha sido eliminada exitosamente"}


@router.put("/{id_categoria}")
def editar_una_categoria(id_categoria : int, categoria_actualizada : CategoriaCrear):
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail= "Esa categoria no existe"
        )
    datos_actualizados = Categoria(
        None,
        categoria_actualizada.nombre_categoria
    )
    actualizar_categoria(datos_actualizados)
    return {"mensaje" : "La categoria se actualizo correctamente"}
    