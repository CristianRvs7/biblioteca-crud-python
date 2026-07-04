from repositories.libro_repository import (obtener_libros_detallados, obtener_libros_detallados_por_id, obtener_libros_id, crear_libro, 
                                           actualizar_libro, eliminar_libro, obtener_libros_por_existencias, obtener_libros_agotados, obtener_libros_por_nombre,
                                           obtener_libros_por_autor, obtener_libros_por_editorial)
from models.libro import Libro
from utils.validaciones import (leer_int, leer_isbn, leer_anio, leer_int_no_negativo, confirmar_accion, leer_texto)


def menu_libros():
    while True:
        print("""
\n========= LIBROS =========\n

1. Listar libros

2. Buscar libro por ID

3. Crear libro

4. Actualizar libro

5. Eliminar libro

6. Mostrar libros disponibles

7. Mostrar libros agotados

8. Buscar libro por nombre

9. Buscar libro por autor

10. Buscar libro por editorial


0. Volver al menú principal
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            buscar_libros_por_id()
        elif opcion == "3":
            ingresar_libro()
        elif opcion == "4":
            actualizar_un_libro()
        elif opcion == "5":
            eliminar_un_libro()
        elif opcion == "6":
            mostrar_libros_disponibles()
        elif opcion == "7":
            mostrar_libros_agotados()
        elif opcion == "8":
            buscar_libro_por_nombre()
        elif opcion == "9":
            buscar_libros_por_autor()
        elif opcion == "10":
            buscar_libros_por_editorial()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

## ========================================================================================

def imprimir_libro(libro):
    print(f"""
ID: {libro[0]}
ISBN: {libro[1]}
Título: {libro[2]}
Autor: {libro[3]} {libro[4]}
Categoría: {libro[5]}
Editorial: {libro[6]}
Año: {libro[7]}
Existencias: {libro[8]}
""")
    
## ========================================================================================

def mostrar_libros():
    libros = obtener_libros_detallados()

    for libro in libros:
        imprimir_libro(libro)
        
## =======================================================================================

def buscar_libros_por_id():
    id_libro = leer_int("Ingrese el ID del libro: ")

    libro = obtener_libros_detallados_por_id(id_libro)

    if libro is None:
        print("No existe un libro con ese ID.")
        return
    
    imprimir_libro(libro)
    
## =======================================================================================

def ingresar_libro():
    id_libro = None  # ID Generado automáticamente por la base de datos
    isbn = leer_isbn("Ingrese el ISBN del libro: ")
    titulo = leer_texto("Ingrese el título del libro: ", 150)
    id_autor = leer_int("Ingrese el ID del autor: ")
    id_categoria = leer_int("Ingrese el ID de la categoría: ")
    id_editorial = leer_int("Ingrese el ID de la editorial: ")
    anio_lanzamiento = leer_anio("Ingrese el año de lanzamiento: ")
    existencias = leer_int_no_negativo("Ingrese la cantidad de existencias: ")

    libro = Libro(
        id_libro=id_libro,
        isbn=isbn,
        titulo=titulo,
        id_autor=id_autor,
        id_categoria=id_categoria,
        id_editorial=id_editorial,
        anio_lanzamiento=anio_lanzamiento,
        existencias=existencias
    )

    if confirmar_accion("¿Desea guardar este libro?"):
        crear_libro(libro)
        print("Libro creado correctamente.")
    else:
        print("Operación cancelada.")   
## =========================================================================================

def actualizar_un_libro():
    id_libro = leer_int("Ingrese el ID del libro a actualizar: ")

    libro_existente = obtener_libros_id(id_libro)

    if libro_existente is None:
        print("No existe un libro con ese ID.")
        return

    isbn = leer_isbn(f"Ingrese el nuevo ISBN (actual: {libro_existente.isbn}): ")
    titulo = leer_texto(f"Ingrese el nuevo título (actual: {libro_existente.titulo}): ")
    id_autor = leer_int(f"Ingrese el nuevo ID del autor (actual: {libro_existente.id_autor}): ")
    id_categoria = leer_int(f"Ingrese el nuevo ID de la categoría (actual: {libro_existente.id_categoria}): ")
    id_editorial = leer_int(f"Ingrese el nuevo ID de la editorial (actual: {libro_existente.id_editorial}): ")
    anio_lanzamiento = leer_anio(f"Ingrese el nuevo año de lanzamiento (actual: {libro_existente.anio_lanzamiento}): ")
    existencias = leer_int_no_negativo(f"Ingrese la nueva cantidad de existencias (actual: {libro_existente.existencias}): ")

    libro_actualizado = Libro(
        id_libro=id_libro,
        isbn=isbn,
        titulo=titulo,
        id_autor=id_autor,
        id_categoria=id_categoria,
        id_editorial=id_editorial,
        anio_lanzamiento=anio_lanzamiento,
        existencias=existencias
    )

    if confirmar_accion("¿Está seguro de que desea actualizar este libro?"):
        actualizar_libro(libro_actualizado)
        print("Libro actualizado correctamente.")
    else:
        print("Operación cancelada.")
    
## =========================================================================================

def eliminar_un_libro():
    id_libro = leer_int("Ingrese el ID del libro a eliminar: ")

    libro_existente = obtener_libros_id(id_libro)

    if libro_existente is None:
        print("No existe un libro con ese ID.")
        return

    if confirmar_accion("¿Está seguro de que desea eliminar este libro?"):
        eliminar_libro(id_libro)
        print("Libro eliminado correctamente.")
    else:
        print("Operación cancelada.")
        
## =========================================================================================

def mostrar_libros_disponibles():
    libros_disponibles = obtener_libros_por_existencias()

    if not libros_disponibles:
        print("No hay libros disponibles.")
        return

    for libro in libros_disponibles:
        imprimir_libro(libro)

## ========================================================================================

def mostrar_libros_agotados():
    libros_agotados = obtener_libros_agotados()

    if not libros_agotados:
        print("No hay libros agotados.")
        return

    for libro in libros_agotados:
        imprimir_libro(libro)

## ========================================================================================

def buscar_libro_por_nombre():
    nombre_libro = leer_texto("Ingrese el nombre del libro a buscar: ", 150)

    libros_encontrados = obtener_libros_por_nombre(nombre_libro)

    if not libros_encontrados:
        print("No se encontraron libros con ese nombre.")
        return

    for libros in libros_encontrados:
            imprimir_libro(libros)
        
## ===========================================================================================

def buscar_libros_por_autor():
    nombre_autor_result = leer_texto("Ingrese el nombre del autor:")
    libros_encontrados = obtener_libros_por_autor(nombre_autor_result)
    
    if not libros_encontrados:
        print("No se encontraron libros de ese autor.")
        return

    for libros in libros_encontrados:
        imprimir_libro(libros)

## ============================================================================================

def buscar_libros_por_editorial():
    nombre_editorial = leer_texto("Ingrese nombre de editorial: ")
    libros_encontrados = obtener_libros_por_editorial(nombre_editorial)
    
    if not libros_encontrados:
        print("Esa editorial aun no tiene libros registrados.")
    
    for libros in libros_encontrados:
        imprimir_libro(libros)