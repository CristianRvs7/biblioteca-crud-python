from database.connection import obtener_conexion
from models.prestamo import Prestamo
from datetime import datetime

## ================================================================================

def obtener_prestamos():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT
                    p.id_prestamo,
                    CONCAT(u.nombres_usuario, ' ', u.apellidos_usuario) AS nombres_usuario,
                    l.titulo_libro,
                    p.fecha_prestamo,
                    p.fecha_limite,
                    p.fecha_devolucion,
                    p.estado
                FROM prestamos p
                INNER JOIN usuarios u
                    ON p.id_usuario = u.id_usuario
                INNER JOIN libros l
                    ON p.id_libro = l.id_libro
                ORDER BY p.id_prestamo;
            """)
            resultados = cursor.fetchall()

    prestamos = []

    if len(resultados) == 0:
        print("No hay préstamos registrados")
        return prestamos

    for fila in resultados:
        prestamo = Prestamo(
            id_prestamo=fila[0],
            id_usuario=fila[1],
            id_libro=fila[2],
            fecha_prestamo=fila[3],
            fecha_limite=fila[4],
            fecha_devolucion=fila[5],
            estado=fila[6]
        )

        prestamos.append(prestamo)

    return prestamos
    
 ## ===============================================================================

def obtener_prestamo_por_id(id_prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM prestamos WHERE id_prestamo = %s",
                (id_prestamo,)
            )
            fila = cursor.fetchone()

            if fila is None:
                return None

            prestamo = Prestamo(*fila)
        return prestamo

## ==================================================================================

def crear_prestamo(prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT existencias FROM libros WHERE id_libro = %s",
                (prestamo.id_libro,)
            )

            fila = cursor.fetchone()

            if fila is None:
                print("El libro no existe")
                return

            existencias = fila[0]

            if existencias <= 0:
                print("No hay existencias disponibles")
                return

            cursor.execute(
                """
                INSERT INTO prestamos (
                    id_usuario,
                    id_libro,
                    fecha_limite,
                    fecha_devolucion,
                    estado
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    prestamo.id_usuario,
                    prestamo.id_libro,
                    prestamo.fecha_limite,
                    prestamo.fecha_devolucion,
                    prestamo.estado
                )
            )

            cursor.execute(
                """
                UPDATE libros
                SET existencias = existencias - 1
                WHERE id_libro = %s
                """,
                (prestamo.id_libro,)
            )

        conexion.commit()
## ===========================================================================================

def devolver_prestamo(id_prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id_libro, estado
                FROM prestamos
                WHERE id_prestamo = %s
                """,
                (id_prestamo,)
            )

            fila = cursor.fetchone()

            if fila is None:
                print("El préstamo no existe")
                return

            id_libro = fila[0]
            estado = fila[1]

            if estado == "Devuelto":
                print("Ese préstamo ya fue devuelto")
                return

            cursor.execute(
                """
                UPDATE prestamos
                SET estado = %s,
                    fecha_devolucion = %s
                WHERE id_prestamo = %s
                """,
                (
                    "Devuelto",
                    datetime.now(),
                    id_prestamo
                )
            )

            cursor.execute(
                """
                UPDATE libros
                SET existencias = existencias + 1
                WHERE id_libro = %s
                """,
                (id_libro,)
            )

            conexion.commit()

            print("Préstamo devuelto correctamente")

## ==============================================================================================

def eliminar_prestamo(id_prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM prestamos WHERE id_prestamo = %s",
                (id_prestamo,)
            )

            if cursor.rowcount == 0:
                print("El préstamo no existe")
                return

            conexion.commit()
            print("Préstamo eliminado correctamente")
            
## ==============================================================================================

def actualizar_prestamo(prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE prestamos
                SET id_usuario = %s,
                    id_libro = %s,
                    fecha_prestamo = %s,
                    fecha_limite = %s,
                    fecha_devolucion = %s,
                    estado = %s
                WHERE id_prestamo = %s
                """,
                (
                    prestamo.id_usuario,
                    prestamo.id_libro,
                    prestamo.fecha_prestamo,
                    prestamo.fecha_limite,
                    prestamo.fecha_devolucion,
                    prestamo.estado,
                    prestamo.id_prestamo
                )
            )
            conexion.commit()

## ==============================================================================================

def devolver_prestamo(id_prestamo):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_libro, estado
                FROM prestamos
                WHERE id_prestamo = %s
            """, (id_prestamo,))

            fila = cursor.fetchone()

            if fila is None:
                print("No existe un préstamo con ese ID.")
                return

            id_libro = fila[0]
            estado = fila[1]

            if estado == "Devuelto":
                print("Este préstamo ya fue devuelto.")
                return

            cursor.execute("""
                UPDATE prestamos
                SET fecha_devolucion = CURRENT_DATE,
                    estado = 'Devuelto'
                WHERE id_prestamo = %s
            """, (id_prestamo,))

            cursor.execute("""
                UPDATE libros
                SET existencias = existencias + 1
                WHERE id_libro = %s
            """, (id_libro,))

        conexion.commit()
        
## =============================================================================================

def obtener_prestamos_vencidos():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT
                    p.id_prestamo,
                    CONCAT(u.nombres_usuario, ' ', u.apellidos_usuario) AS nombres_usuario,
                    l.titulo_libro,
                    p.fecha_prestamo,
                    p.fecha_limite,
                    p.fecha_devolucion,
                    p.estado
                FROM prestamos p
                INNER JOIN usuarios u ON p.id_usuario = u.id_usuario
                INNER JOIN libros l ON p.id_libro = l.id_libro
                WHERE p.estado = 'Prestado' AND p.fecha_limite < CURRENT_DATE
                ORDER BY p.fecha_limite ASC;
            """)
            resultados = cursor.fetchall()

    prestamos_vencidos = []

    for fila in resultados:
        prestamo = Prestamo(
            id_prestamo=fila[0],
            id_usuario=fila[1],
            id_libro=fila[2],
            fecha_prestamo=fila[3],
            fecha_limite=fila[4],
            fecha_devolucion=fila[5],
            estado=fila[6]
        )
        prestamos_vencidos.append(prestamo)

    return prestamos_vencidos

## ============================================================================================

def obtener_prestamos_por_usuario(id_usuario):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT
                    p.id_prestamo,
                    CONCAT(u.nombres, ' ', u.apellidos),
                    l.titulo_libro,
                    p.fecha_prestamo,
                    p.fecha_limite,
                    p.fecha_devolucion,
                    p.estado
                FROM prestamos p
                JOIN usuarios u ON p.id_usuario = u.id_usuario
                JOIN libros l ON p.id_libro = l.id_libro
                WHERE p.id_usuario = %s
                ORDER BY p.fecha_prestamo DESC;
            """, (id_usuario,))

            resultados = cursor.fetchall()

    return [Prestamo(*fila) for fila in resultados]

