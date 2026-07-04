from models.prestamo import Prestamo
from repositories.prestamo_repository import (obtener_prestamos, obtener_prestamo_por_id, crear_prestamo, actualizar_prestamo,eliminar_prestamo, obtener_prestamos_vencidos, devolver_prestamo, obtener_prestamos_por_usuario)
from repositories.usuario_repository import obtener_usuario_por_id
from repositories.libro_repository import obtener_libros_id
from utils.validaciones import leer_int, leer_texto, confirmar_accion, leer_fecha
from datetime import datetime


def menu_prestamos():
    while True:
        print("""
\n========== MENU DE PRESTAMOS ==========\n

1. Listar préstamos

2. Listar préstamos vencidos

3. Buscar préstamo por ID

4. Crear préstamo

5. Actualizar préstamo

6. Devolver préstamo

7. Eliminar préstamo


0. Volver al menú principal
              """)

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_prestamos()
        elif opcion == "2":
            mostrar_prestamos_vencidos()
        elif opcion == "3":
            buscar_prestamo_por_id()
        elif opcion == "4":
            ingresar_prestamo()
        elif opcion == "5":
            actualizar_un_prestamo()
        elif opcion == "6":
            devolver_un_prestamo()
        elif opcion == "7":
            eliminar_un_prestamo()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

## =================================================================

def mostrar_prestamos():
    prestamos = obtener_prestamos()

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for prestamo in prestamos:
        print(prestamo)

## =================================================================

def buscar_prestamo_por_id():
    id_prestamo = leer_int("Ingrese el ID del préstamo: ")
    prestamo = obtener_prestamo_por_id(id_prestamo)

    if prestamo is None:
        print("No existe un préstamo con ese ID.")
        return

    print(prestamo)

## =================================================================

def ingresar_prestamo():
    id_usuario = leer_int("Ingrese el ID del usuario: ")
    usuario = obtener_usuario_por_id(id_usuario)

    if usuario is None:
        print("No existe un usuario con ese ID.")
        return

    id_libro = leer_int("Ingrese el ID del libro: ")
    libro = obtener_libros_id(id_libro)

    if libro is None:
        print("No existe un libro con ese ID.")
        return

    fecha_limite = leer_fecha("Ingrese la fecha límite del préstamo (YYYY-MM-DD): ", 20)
    estado = "Prestado"

    prestamo = Prestamo(
        None,
        id_usuario,
        id_libro,
        datetime.now(),
        fecha_limite,
        None,
        estado
    )

    if confirmar_accion("¿Desea guardar este préstamo?"):
        crear_prestamo(prestamo)
        print("Préstamo creado exitosamente.")
    else:
        print("Operación cancelada.")

## =================================================================

def actualizar_un_prestamo():
    id_prestamo = leer_int("Ingrese el ID del préstamo a actualizar: ")
    prestamo = obtener_prestamo_por_id(id_prestamo)

    if prestamo is None:
        print("No existe un préstamo con ese ID.")
        return
    elif prestamo.estado == "Devuelto":
        print("No se puede actualizar un préstamo que ya ha sido devuelto.")
        return
    print(prestamo)


    id_usuario = leer_int("Ingrese el nuevo ID del usuario: ")
    usuario = obtener_usuario_por_id(id_usuario)

    if usuario is None:
        print("No existe un usuario con ese ID.")
        return

    id_libro = leer_int("Ingrese el nuevo ID del libro: ")
    libro = obtener_libros_id(id_libro)

    if libro is None:
        print("No existe un libro con ese ID.")
        return
    fecha_prestamo = prestamo.fecha_prestamo
    fecha_limite = leer_fecha("Ingrese la nueva fecha límite (YYYY-MM-DD): ")
    fecha_devolucion = leer_fecha("Ingrese la fecha de devolución (YYYY-MM-DD o vacío si no ha devuelto): ", allow_empty=True)
    estado = leer_texto("Ingrese el nuevo estado del préstamo: ", 20)
    
    prestamo_actualizado = Prestamo(
        id_prestamo,
        id_usuario,
        id_libro,
        fecha_prestamo,
        fecha_limite,
        fecha_devolucion,
        estado
    )

    if confirmar_accion("¿Desea actualizar este préstamo?"):
        actualizar_prestamo(prestamo_actualizado)
        print("Préstamo actualizado exitosamente.")
    else:
        print("Operación cancelada.")

## =================================================================

def eliminar_un_prestamo():
    id_prestamo = leer_int("Ingrese el ID del préstamo a eliminar: ")
    prestamo = obtener_prestamo_por_id(id_prestamo)

    if prestamo is None:
        print("No existe un préstamo con ese ID.")
        return

    print(prestamo)

    if confirmar_accion("¿Está seguro de que desea eliminar este préstamo?"):
        eliminar_prestamo(id_prestamo)
        print("Préstamo eliminado exitosamente.")
    else:
        print("Operación cancelada.")
        
## ¿=================================================================

def devolver_un_prestamo():
    id_prestamo = leer_int("Ingrese el ID del préstamo a devolver: ")
    prestamo = obtener_prestamo_por_id(id_prestamo)

    if prestamo is None:
        print("No existe un préstamo con ese ID.")
        return

    print(prestamo)

    if confirmar_accion("¿Está seguro de que desea devolver este préstamo?"):
        devolver_prestamo(id_prestamo)
        print("Préstamo devuelto exitosamente.")
    else:
        print("Operación cancelada.")
        
## =====================================================================

def mostrar_prestamos_vencidos():
    prestamos_vencidos = obtener_prestamos_vencidos()

    if not prestamos_vencidos:
        print("No hay préstamos vencidos.")
        return

    for prestamo in prestamos_vencidos:
        print(prestamo)

## =====================================================================

def mostrar_prestamos_por_usuario():
    id_usuario = leer_int("Ingrese el ID del usuario: ")
    prestamos = obtener_prestamos_por_usuario(id_usuario)

    if not prestamos:
        print("No hay préstamos para este usuario.")
        return

    for prestamo in prestamos:
        print(prestamo)

## =====================================================================


