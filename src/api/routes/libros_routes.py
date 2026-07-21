from repositories.libro_repository import (obtener_libros, obtener_libros_detallados_por_id, crear_libro, eliminar_libro, actualizar_libro)
from fastapi import APIRouter, HTTPException
from models.libro import Libro
from api.schemas.libro_schema import LibroCrear, LibroRespuesta
from psycopg.errors import UniqueViolation

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
    
    
def libro_detallado_a_diccionario(libro):
    return{
        "id_libro": libro[0],
        "isbn": libro[1],
        "titulo_libro": libro[2],
        "id_autor" : libro[3],
        "nombre_autor": f"{libro[4]} {libro[5]}",
        "id_categoria" : libro[6],
        "nombre_categoria": libro[7],
        "id_editorial" : libro[8],
        "nombre_editorial": libro[9],
        "anio_lanzamiento": libro[10],
        "existencias": libro[11]
    }


@router.get("", response_model=list[LibroRespuesta])
def listar_libros():
    libros = obtener_libros()
    libros_json = []
    for libro in libros:
        libros_json.append(libro_detallado_a_diccionario(libro))
    return libros_json


@router.get("/{id_libro}", response_model=LibroRespuesta)
def buscar_por_id(id_libro: int):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Ese libro no existe."
        )
    libro_json = libro_detallado_a_diccionario(libro)
    return libro_json


@router.post("", status_code=201, response_model=LibroRespuesta)
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
    
    try:
        id_libro = crear_libro(nuevo_libro)
    except UniqueViolation:
            raise HTTPException(
                status_code=409,
                detail="Ya existe un libro con ese ISBN "
            )

    libro = obtener_libros_detallados_por_id(id_libro)
    
    libro_json = libro_detallado_a_diccionario(libro)
    
    return libro_json


@router.delete("/{id_libro}")
def eliminar_un_libro(id_libro : int):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese libro no existe."
        )
    eliminar_libro(id_libro)
    return {"mensaje" : "Libro eliminado exitosamente."}


@router.put("/{id_libro}", response_model=LibroRespuesta)
def actualizar_un_libro(id_libro : int, datos_libro : LibroCrear):
    libro = obtener_libros_detallados_por_id(id_libro)
    if libro is None:
        raise HTTPException(
            status_code=404,
            detail= "Ese libro no existe."
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
    try:
        actualizar_libro(libro_actualizado)
    except UniqueViolation:
            raise HTTPException(
                status_code=409,
                detail="Ya existe un libro con ese ISBN "
            )
    
    libro_resultado = obtener_libros_detallados_por_id(id_libro)
    
    return libro_detallado_a_diccionario(libro_resultado)