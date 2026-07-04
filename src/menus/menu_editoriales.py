from repositories.editorial_repository import (obtener_editoriales, obtener_editorial_por_id, crear_editorial, actualizar_editorial, eliminar_editorial)
from models.editorial import Editorial
from utils.validaciones import leer_texto, leer_int, confirmar_accion

def menu_editoriales(): 
    while True:
        print("""
\n========= EDITORIALES =========\n
              
1. Listar editoriales

2. Buscar editorial por ID

3. Crear editorial

4. Actualizar editorial

5. Eliminar editorial

              
0. Volver al menú principal
""")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_editoriales()
        elif opcion == "2":
            buscar_editorial_por_id()
        elif opcion == "3":
            ingresar_editorial()
        elif opcion == "4":
            actualizar_una_editorial()
        elif opcion == "5":
            eliminar_una_editorial()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

def mostrar_editoriales():
    editoriales = obtener_editoriales()
    for editorial in editoriales:
        print(editorial)

## ========================================================================================

def buscar_editorial_por_id():
    id_editorial = leer_int("Ingrese el ID de la editorial: ")
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        print("No existe una editorial con ese ID.")
        return
    print(editorial)
        
## ======================================================================================== 

def ingresar_editorial():
    nombre_editorial = leer_texto("Ingrese el nombre de la editorial: ", 100)
    editorial = Editorial(None, nombre_editorial)
    if confirmar_accion("¿Desea guardar esta editorial?"):
        crear_editorial(editorial)
        print("Editorial creada exitosamente.")
    else:
        print("Operación cancelada.")

## ========================================================================================

def actualizar_una_editorial():
    id_editorial = leer_int("Ingrese el ID de la editorial a actualizar: ")
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        print("No existe una editorial con ese ID.")
        return
    nombre = leer_texto(f"Ingrese el nuevo nombre de la editorial (actual: {editorial.nombre_editorial}): ", 100)
    editorial.nombre_editorial = nombre
    actualizar_editorial(editorial)
    print("Editorial actualizada exitosamente.")

## ========================================================================================

def eliminar_una_editorial():
    id_editorial = leer_int("Ingrese el ID de la editorial a eliminar: ")
    editorial = obtener_editorial_por_id(id_editorial)
    if editorial is None:
        print("No existe una editorial con ese ID.")
        return
    if not confirmar_accion("¿Estás seguro de que deseas eliminar esta editorial?"):
        print("Operación cancelada.")
        return
    eliminar_editorial(id_editorial)
    print("Editorial eliminada exitosamente.")