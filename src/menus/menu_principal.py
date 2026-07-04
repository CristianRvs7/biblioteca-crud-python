from menus.menu_libros import menu_libros
from menus.menu_autores import menu_autores
from menus.menu_editoriales import menu_editoriales
from menus.menu_usuarios import menu_usuarios
from menus.menu_prestamo import menu_prestamos
from menus.menu_categorias import menu_categoria


def iniciar_menu():
    while True:
        print("""
\n========= BIBLIOTECA =========\n

1. Gestionar libros

2. Gestionar autores

3. Gestionar editoriales

4. Gestionar usuarios

5. Gestionar préstamos

6. Gestionar categorias


0. Salir
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_libros()
        elif opcion == "2":
            menu_autores()
        elif opcion == "3":
            menu_editoriales()
        elif opcion == "4":
            menu_usuarios()
        elif opcion == "5":
            menu_prestamos()
        elif opcion == "6":
            menu_categoria()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")