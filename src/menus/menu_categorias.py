from models.categoria import Categoria
from utils.validaciones import(leer_int, leer_texto, confirmar_accion)
from repositories.categoria_repository import(obtener_categoria, obtener_categoria_id, actualizar_categoria, crear_categoria, eliminar_categoria)


def menu_categoria():
    while True:
        print("""
          \n=============== Categorias ==============\n

1. Listar categorias

2. Buscar categoria por ID

3. Actualizar categoria

4. Crear categoria

5. Eliminar categoria


0. Volver al menu principal
          """)
    
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            mostrar_categorias()
        elif opcion == "2":
            buscar_categoria_por_id()
        elif opcion == "3":
            actualizar_una_categoria()
        elif opcion == "4":
            crear_una_categoria()
        elif opcion == "5":
            eliminar_una_categoria()
        elif opcion == "0":
            break
        else:
            print("Operacion invalida.")

## ===============================================================================================

def mostrar_categorias():
    categorias = obtener_categoria()
    
    for categoria in categorias:
        print(categoria)

## ===============================================================================================

def buscar_categoria_por_id():
    id_categoria = leer_int("Ingrese el id a buscar: ")
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        print("No hay categoria con esa ID")
        return
    
    print(categoria)
    
## ================================================================================================

def actualizar_una_categoria():
    id_categoria = leer_int("Ingrese el id a buscar: ")
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        print("No hay categoria con esa ID")
        return
    nombre = leer_texto(f"Ingrese el nuevo nombre de la categoria (Actual:{categoria.nombre_categoria}) ")
    categoria.nombre_categoria = nombre
    actualizar_categoria(categoria)
    print("Categoria actualizada correctamente.")

## =================================================================================================

def crear_una_categoria():
    nombre_categ = leer_texto("Ingrese el nombre de la categoria: ", 50)
    categoria = Categoria(None, nombre_categ)
    if confirmar_accion("¿Desea guardar esta categoria?"):
        crear_categoria(categoria)
        print("Categoria creada exitosamente.")
    else:
        print("Operación cancelada.")
        
## ==================================================================================================

def eliminar_una_categoria():
    id_categoria = leer_int("Ingrese el ID de la categoria a eliminar: ")
    categoria = obtener_categoria_id(id_categoria)
    if categoria is None:
        print("No existe una categoria con ese ID.")
        return
    if not confirmar_accion("¿Estás seguro de que deseas eliminar esta categoria?"):
        print("Operación cancelada.")
        return
    eliminar_categoria(id_categoria)
    print("Categoria eliminada exitosamente.")