from repositories.autor_repository import (obtener_autores, obtener_autor_por_id, crear_autor, actualizar_autor, eliminar_autor)
from models.autor import Autor
from utils.validaciones import leer_int, leer_texto, confirmar_accion


def menu_autores():
    while True:
        print("""
\n========= AUTORES =========\n

1. Listar autores

2. Buscar autor por ID

3. Crear autor

4. Actualizar autor

5. Eliminar autor


0. Volver al menú principal
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_autores()
        elif opcion == "2":
            buscar_autor_por_id()
        elif opcion == "3":
            ingresar_autor()
        elif opcion == "4":
            actualizar_un_autor()
        elif opcion == "5":
            eliminar_un_autor()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

## =======================================================================================

def mostrar_autores():
    autores = obtener_autores()

    for autor in autores:
        print(autor)

## =======================================================================================

def buscar_autor_por_id():
    id_autor = leer_int("Ingrese el ID del autor: ")

    autor = obtener_autor_por_id(id_autor)

    if autor is None:
        print("No existe un autor con ese ID.")
        return

    print(autor)

## =========================================================================================

def ingresar_autor():
    nombre_autor = leer_texto("Ingrese el nombre del autor: ", 100)
    apellido_autor = leer_texto("Ingrese el apellido del autor: ", 100)

    autor = Autor(
        id_autor=None,
        nombre_autor=nombre_autor,
        apellido_autor=apellido_autor
    )

    if confirmar_accion("¿Desea guardar este autor?"):
        crear_autor(autor)
        print("Autor creado correctamente.")
    else:
        print("Operación cancelada.")

## ========================================================================================

def actualizar_un_autor():
    id_autor = leer_int("Ingrese el ID del autor a actualizar: ")

    autor_existente = obtener_autor_por_id(id_autor)

    if autor_existente is None:
        print("No existe un autor con ese ID.")
        return

    nombre_autor = leer_texto(
        f"Ingrese el nuevo nombre (actual: {autor_existente.nombre_autor}): ",
        100
    )
    apellido_autor = leer_texto(
        f"Ingrese el nuevo apellido (actual: {autor_existente.apellido_autor}): ",
        100
    )

    autor_actualizado = Autor(
        id_autor=id_autor,
        nombre_autor=nombre_autor,
        apellido_autor=apellido_autor
    )

    if confirmar_accion("¿Desea actualizar este autor?"):
        actualizar_autor(autor_actualizado)
        print("Autor actualizado correctamente.")
    else:
        print("Operación cancelada.")

## ======================================================================================

def eliminar_un_autor():
    id_autor = leer_int("Ingrese el ID del autor a eliminar: ")

    autor_existente = obtener_autor_por_id(id_autor)

    if autor_existente is None:
        print("No existe un autor con ese ID.")
        return

    if confirmar_accion("¿Desea eliminar este autor?"):
        eliminar_autor(id_autor)
        print("Autor eliminado correctamente.")
    else:
        print("Operación cancelada.")