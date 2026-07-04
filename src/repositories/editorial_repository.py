from database.connection import obtener_conexion
from models.editorial import Editorial

## DEFINICION DE FUNCIONES ##

## ============================================================================================= ##

def obtener_editoriales():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM editoriales ORDER BY id_editorial ASC")
            resultados = cursor.fetchall()

    editoriales = []

    for fila in resultados:
        editorial = Editorial(
            id_editorial=fila[0],
            nombre_editorial=fila[1]
        )

        editoriales.append(editorial)

    return editoriales

## ============================================================================================= ##

def obtener_editorial_por_id(id_editorial):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM editoriales WHERE id_editorial = %s", (id_editorial,))
            fila = cursor.fetchone()
            if fila is None:
                return None
        editorial = Editorial(*fila)
    return editorial

## ============================================================================================= ##

def crear_editorial(editorial):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO editoriales (
                    nombre_editorial
                )
                VALUES (%s)
                """,
                (
                    editorial.nombre_editorial,
                )
            )
            conexion.commit()

## ============================================================================================= ##

def actualizar_editorial(editorial):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE editoriales
                SET nombre_editorial = %s
                WHERE id_editorial = %s
                """,
                (
                    editorial.nombre_editorial,
                    editorial.id_editorial
                )
            )
            conexion.commit()

## ============================================================================================= ##

def eliminar_editorial(id_editorial):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM editoriales WHERE id_editorial = %s", (id_editorial,))
            conexion.commit()

## ============================================================================================= ##