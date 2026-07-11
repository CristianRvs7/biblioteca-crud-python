from fastapi import APIRouter, HTTPException
from models.editorial import Editorial
from api.schemas.editorial_schema import EditorialCrear
from repositories.editorial_repository import obtener_editoriales, obtener_editorial_por_id, crear_editorial, eliminar_editorial, actualizar_editorial

router = APIRouter(
    prefix="/editoriales",
    tags=["Editorial"]
)

def convertir_editorial_a_diccionario(editorial):
    return {
        "id_editorial" : editorial.id_editorial,
        "nombre_editorial" : editorial.nombre_editorial
    }
    
@router.get("")
def listar_editoriales():
    editoriales = obtener_editoriales()
    
    editoriales_json = []
    
    for editorial in editoriales:
        editoriales_json.append(convertir_editorial_a_diccionario(editorial))
    
    return editoriales_json

@router.get("/{id_editorial}")
def buscar_por_id(id_editorial):
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail= "Esa editorial no existe."
        )
    return convertir_editorial_a_diccionario(editorial)

@router.post("", status_code=201)
def crear_una_editorial(datos_editorial : EditorialCrear):
    nueva_editorial = Editorial(
        None,
        datos_editorial.nombre_editorial
    )
    crear_editorial(nueva_editorial)
    return {"mensaje" : "Editorial creada exitosamente."}

@router.delete("/{id_editorial}")
def eliminar_una_editorial(id_editorial : int):
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Esa editorial no existe."
        )
    eliminar_editorial(id_editorial)
    return{"mensaje" : "Editorial eliminada exitosamente."}

@router.put("/{id_editorial}")
def actualizar_una_editorial(id_editorial : int, datos_editorial : EditorialCrear):
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Ese editorial no existe."
        )
    editorial_actualizado = Editorial(
        id_editorial,
        datos_editorial.nombre_editorial
    )
    actualizar_editorial(editorial_actualizado)
    return {"mensaje" : "Editorial actualizada exitosamente."}