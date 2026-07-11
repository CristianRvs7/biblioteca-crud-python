from repositories.libro_repository import (obtener_libros_detallados, obtener_libros_detallados_por_id, crear_libro, eliminar_libro, actualizar_libro)
from fastapi import APIRouter, HTTPException
from models.libro import Libro
from api.schemas.libro_schema import LibroCrear

router = APIRouter(
    prefix="/libros",
    tags=["Libros"]
)

def convertir_libro_a_diccionario(libro):
    return {
        "id_libro": libro[0],
        "isbn": libro[1],
        "titulo_libro": libro[2],
        "autor": f"{libro[3]} {libro[4]}",
        "categoria": libro[5],
        "editorial": libro[6],
        "anio_lanzamiento": libro[7],
        "existencias": libro[8]
    }

@router.get("")
def listar_libros():
    libros = obtener_libros_detallados()

    libros_json = []

    for libro in libros:
        libros_json.append(convertir_libro_a_diccionario(libro))

    return libros_json

@router.get("/{id_libro}")
def buscar_por_id(id_libro: int):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )
    return convertir_libro_a_diccionario(libro)

@router.post("", status_code=201)
def crear_un_libro(datos_libro: LibroCrear):
    nuevo_libro = Libro(
        
        None,
        datos_libro.isbn,
        datos_libro.titulo_libro,
        datos_libro.id_autor,
        datos_libro.id_categoria,
        datos_libro.id_editorial,
        datos_libro.anio_lanzamiento,
        datos_libro.existencias
    )

    crear_libro(nuevo_libro)

    return {"mensaje": "Libro creado exitosamente"}

@router.delete("/{id_libro}")
def eliminar_un_libro(id_libro : int):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese libro no existe"
        )
    eliminar_libro(id_libro)
    return {"mensaje" : "Libro eliminado correctamente"}

@router.put("/{id_libro}")
def actualizar_un_libro(id_libro : int, datos_libro : LibroCrear):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese libro no existe"
        )
    libro_actualizado = Libro(
        id_libro,
        datos_libro.isbn,
        datos_libro.titulo_libro,
        datos_libro.id_autor,
        datos_libro.id_categoria,
        datos_libro.id_editorial,
        datos_libro.anio_lanzamiento,
        datos_libro.existencias
    )
    actualizar_libro(libro_actualizado)
    return {"mensaje" : "El libro se ha actualizado correctamente"}