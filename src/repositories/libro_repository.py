from database.connection import obtener_conexion
from models.libro import Libro


## DEFINICION DE FUNCIONES ##

## =============================================================================================

def obtener_libros():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM libros ORDER BY id_libro ASC")
            resultados = cursor.fetchall()

    libros = []

    for fila in resultados:
        libro = Libro(
            id_libro=fila[0],
            isbn=fila[1],
            titulo=fila[2],
            id_autor=fila[3],
            id_categoria=fila[4],
            id_editorial=fila[5],
            anio_lanzamiento=fila[6],
            existencias=fila[7]
        )

        libros.append(libro)

    return libros

## =============================================================================================

def obtener_libros_detallados():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                ORDER BY l.id_libro ASC
                """
            )

            resultados = cursor.fetchall()

    return resultados

## ========================================================================================================

def obtener_libros_id(id_libro):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM libros WHERE id_libro = %s", (id_libro,))
            fila = cursor.fetchone()
            if fila is None:
                return None
        libro = Libro(*fila)
    return libro



## =============================================================================================

def crear_libro(libro):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO libros (
                    isbn, titulo_libro, id_autor, id_categoria,
                    id_editorial, anio_lanzamiento, existencias
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    libro.isbn,
                    libro.titulo,
                    libro.id_autor,
                    libro.id_categoria,
                    libro.id_editorial,
                    libro.anio_lanzamiento,
                    libro.existencias
                )
            )
            conexion.commit()

## ================================================================================================

def actualizar_libro(libro):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE libros
                SET isbn = %s,
                    titulo_libro = %s,
                    id_autor = %s,
                    id_categoria = %s,
                    id_editorial = %s,
                    anio_lanzamiento = %s,
                    existencias = %s
                WHERE id_libro = %s
                """,
                (
                    libro.isbn,
                    libro.titulo,
                    libro.id_autor,
                    libro.id_categoria,
                    libro.id_editorial,
                    libro.anio_lanzamiento,
                    libro.existencias,
                    libro.id_libro
                )
            )
            conexion.commit()

## =================================================================================================

def eliminar_libro(id_libro):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM libros WHERE id_libro = %s",
                (id_libro,)
            )
            if cursor.rowcount == 0:
                print("No existe ese libro")
            else:
                conexion.commit()
                
## ==================================================================================================

def obtener_libros_detallados_por_id(id_libro):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE l.id_libro = %s
                """,
                (id_libro,)
            )

            resultados = cursor.fetchone()

    return resultados

## =================================================================================================

def obtener_libros_por_existencias():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE l.existencias > 0
                ORDER BY l.id_libro ASC
                """
            )

            resultados = cursor.fetchall()

    return resultados

## =================================================================================================

def obtener_libros_agotados():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE l.existencias = 0
                ORDER BY l.id_libro ASC
                """
            )

            resultados = cursor.fetchall()

    return resultados

## =================================================================================================

def obtener_libros_por_nombre(nombre):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                    SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE l.titulo_libro ILIKE %s
                ORDER BY l.id_libro ASC
                """,
                (f"%{nombre}%",)
            )

            resultados = cursor.fetchall()

    return resultados

## =================================================================================================

def obtener_libros_por_autor(nombre_autor):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a.apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE CONCAT(a.nombre_autor, ' ', a.apellido_autor) ILIKE %s
                ORDER BY l.id_libro ASC
                """,
                (f"%{nombre_autor}%",)
            )

            resultados = cursor.fetchall()

    return resultados

## ====================================================================================================

def obtener_libros_por_editorial(nombre_editorial):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                        SELECT
                    l.id_libro,
                    l.isbn,
                    l.titulo_libro,
                    a.nombre_autor,
                    a,apellido_autor,
                    c.nombre_categoria,
                    e.nombre_editorial,
                    l.anio_lanzamiento,
                    l.existencias
                FROM libros l
                JOIN autores a ON l.id_autor = a.id_autor
                JOIN categorias c ON l.id_categoria = c.id_categoria
                JOIN editoriales e ON l.id_editorial = e.id_editorial
                WHERE e.nombre_editorial ILIKE %s
                ORDER BY l.id_libro ASC""", (f"%{nombre_editorial}",))
            
            resultados = cursor.fetchall()
            
    return resultados