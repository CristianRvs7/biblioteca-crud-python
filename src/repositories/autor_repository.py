from database.connection import obtener_conexion
from models.autor import Autor


## DEFINICION DE FUNCIONES ##

## =============================================================================================

def obtener_autores():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM autores ORDER BY id_autor ASC")
            resultados = cursor.fetchall()

    autores = []

    for fila in resultados:
        autor = Autor(
            id_autor=fila[0],
            nombre_autor=fila[1],
            apellido_autor=fila[2]
            )

        autores.append(autor)

    return autores

## =============================================================================================

def obtener_autor_por_id(id_autor):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM autores WHERE id_autor = %s", (id_autor,))
            fila = cursor.fetchone()
            if fila is None:
                return None
        autor = Autor(*fila)
    return autor



## =============================================================================================

def crear_autor(autor):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO autores (
                    nombre_autor, apellido_autor
                )
                VALUES (%s, %s)
                """,
                (
                    autor.nombre_autor,
                    autor.apellido_autor
                )
            )
            conexion.commit()

## ================================================================================================

def actualizar_autor(autor):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE autores
                SET nombre_autor = %s,
                    apellido_autor = %s
                WHERE id_autor = %s
                """,
                (
                    autor.nombre_autor,
                    autor.apellido_autor,
                    autor.id_autor
                )
            )
            conexion.commit()

## =================================================================================================

def eliminar_autor(id_autor):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM autores WHERE id_autor = %s",
                (id_autor,)
            )
            if cursor.rowcount == 0:
                print("No existe ese autor")
            else:
                conexion.commit()