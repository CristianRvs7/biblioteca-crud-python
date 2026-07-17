from api.schemas.prestamo_schema import PrestamoCrear, PrestamoActualizar
from models.prestamo import Prestamo
from repositories.prestamo_repository import obtener_prestamos, obtener_prestamo_por_id, crear_prestamo, eliminar_prestamo, actualizar_prestamo
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix=("/prestamos"), tags= ["Prestamos"])

def prestamo_a_diccionario(prestamo):
    return {
        "id_prestamo": prestamo.id_prestamo,
        "id_usuario": prestamo.id_usuario,
        "nombre_usuario": prestamo.nombre_usuario,
        "id_libro": prestamo.id_libro,
        "titulo_libro": prestamo.titulo_libro,
        "fecha_prestamo": prestamo.fecha_prestamo,
        "fecha_limite": prestamo.fecha_limite,
        "fecha_devolucion": prestamo.fecha_devolucion,
        "estado": prestamo.estado
    }
    
@router.get("")
def listar_prestamos():
    prestamos = obtener_prestamos()
    prestamos_json = []
    for prestamo in prestamos:
        prestamos_json.append(prestamo_a_diccionario(prestamo))
    return prestamos_json

@router.get("/{id_prestamo}")
def obtener_un_prestamo(id_prestamo):
    prestamo = obtener_prestamo_por_id(id_prestamo)
    if prestamo is None:
        raise HTTPException(
            status_code=404,
            detail="Ese prestamo no existe."
        )
    return prestamo_a_diccionario(prestamo)

@router.post("", status_code=201)
def insertar_prestamo( datos_prestamo : PrestamoCrear):
    nuevo_prestamo = Prestamo(
        None,
        datos_prestamo.id_usuario,
        datos_prestamo.id_libro,
        None,
        datos_prestamo.fecha_limite,
        None,
        "Activo"
    )
    try:
        id_prestamo = crear_prestamo(nuevo_prestamo)

        return {
        "mensaje": "Préstamo creado exitosamente.",
        "id_prestamo": id_prestamo
        }     
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
            )
        
        
@router.delete("/{id_prestamo}")
def eliminar_un_prestamo(id_prestamo : int):
    prestamo = obtener_prestamo_por_id(id_prestamo)
    if prestamo is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese prestamo no existe."
        )
    eliminar_prestamo(id_prestamo)
    return {"mensaje" : "Prestamo eliminado exitosamente."}

@router.put("/{id_prestamo}")
def modificar_prestamo(
    id_prestamo: int,
    datos_prestamo: PrestamoActualizar
):
    try:
        actualizar_prestamo(
            id_prestamo,
            datos_prestamo
        )

        return {
            "mensaje": "Préstamo actualizado exitosamente"
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )