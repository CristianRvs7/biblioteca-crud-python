from database.connection import obtener_conexion
from models.categoria import Categoria


## DEFINICION DE FUNCIONES ##

## =============================================================================================

def obtener_categoria():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM categorias ORDER BY id_categoria ASC")
            resultados = cursor.fetchall()

    categorias = []

    for fila in resultados:
        categoria = Categoria(
            id_categoria=fila[0],
            nombre_categoria=fila[1]
        )

        categorias.append(categoria)

    return categorias

## ========================================================================================================

def obtener_categoria_id(id_categoria):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM categorias WHERE id_categoria = %s", (id_categoria,))
            fila = cursor.fetchone()
            if fila is None:
                return None
        categoria = Categoria(*fila)
    return categoria



## =============================================================================================

def crear_categoria(categoria):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO categorias (
                    nombre_categoria
                )
                VALUES (%s)
                """,
                (
                    categoria.nombre_categoria,
                )
            )
            conexion.commit()

## ================================================================================================

def actualizar_categoria(categoria):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE categorias
                SET nombre_categoria = %s
                WHERE id_categoria = %s
                """,
                (
                    categoria.nombre_categoria,
                    categoria.id_categoria
                )
            )
            conexion.commit()

## =================================================================================================

def eliminar_categoria(id_categoria):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM categorias WHERE id_categoria = %s",
                (id_categoria,)
            )
            if cursor.rowcount == 0:
                print("No existe esa categoria")
            else:
                conexion.commit()

