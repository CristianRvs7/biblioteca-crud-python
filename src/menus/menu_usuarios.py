from models.usuario import Usuario
from repositories.usuario_repository import (obtener_usuarios, obtener_usuario_por_id, crear_usuario, actualizar_usuario, eliminar_usuario)
from utils.validaciones import leer_int, leer_texto, confirmar_accion, leer_correo
import datetime

def menu_usuarios():
    while True:
        print("""
\n========== USUARIOS ==========\n

1. Listar usuarios

2. Buscar usuario por ID

3. Crear usuario

4. Actualizar usuario

5. Eliminar usuario


0. Volver al menú principal
              """)
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            buscar_usuario_por_id()
        elif opcion == "3":
            ingresar_usuario()
        elif opcion == "4":
            actualizar_un_usuario()
        elif opcion == "5":
            eliminar_un_usuario()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

## ========================================================================================

def mostrar_usuarios():
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)
        
## =========================================================================================

def buscar_usuario_por_id():
    id_usuario = leer_int("Ingrese el ID del usuario: ")
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        print("No existe un usuario con ese ID.")
        return
    print(usuario)
    
## ========================================================================================

def ingresar_usuario():
    nombre_usuario = leer_texto("Ingrese el nombre del usuario: ", 100)
    apellido_usuario = leer_texto("Ingrese el apellido del usuario: ", 100)
    docidentificacion = leer_texto("Ingrese el documento de identificación del usuario: ", 20)
    correo_usuario = leer_correo("Ingrese el correo electrónico del usuario: ")
    contacto_usuario = leer_texto("Ingrese el contacto del usuario: ", 20)

    usuario = Usuario(None, nombre_usuario, apellido_usuario, docidentificacion, correo_usuario, contacto_usuario, datetime.datetime.now())

    if confirmar_accion("¿Desea guardar este usuario?"):
        crear_usuario(usuario)
        print("Usuario creado exitosamente.")
    else:
        print("Operación cancelada.")

## ========================================================================================

def actualizar_un_usuario():
    id_usuario = leer_int("Ingrese el ID del usuario a actualizar: ")
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        print("No existe un usuario con ese ID.")
        return
    
    print(usuario)
    
    nombres_usuario = leer_texto(f"Ingrese el nuevo nombre del usuario (actual: {usuario.nombres_usuario}): ", 100)
    apellidos_usuario = leer_texto(f"Ingrese el nuevo apellido del usuario (actual: {usuario.apellidos_usuario}): ", 100)
    docidentificacion = leer_texto(f"Ingrese el nuevo documento de identificación del usuario (actual: {usuario.docidentificacion}): ", 20)
    correo_usuario = leer_correo(f"Ingrese el nuevo correo electrónico del usuario (actual: {usuario.correo_usuario}): ")
    contacto_usuario = leer_texto(f"Ingrese el nuevo contacto del usuario (actual: {usuario.contacto_usuario}): ", 20)
    fecha_registro = usuario.fecha_registro

    usuario_actualizado = Usuario(id_usuario, nombres_usuario, apellidos_usuario, docidentificacion, correo_usuario, contacto_usuario, fecha_registro)

    if confirmar_accion("¿Desea actualizar este usuario?"):
        actualizar_usuario(usuario_actualizado)
        print("Usuario actualizado exitosamente.")
    else:
        print("Operación cancelada.")
        
## ========================================================================================

def eliminar_un_usuario():
    id_usuario = leer_int("Ingrese el ID del usuario a eliminar: ")
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        print("No existe un usuario con ese ID.")
        return

    if confirmar_accion(f"¿Está seguro de que desea eliminar al usuario {usuario.nombres_usuario} {usuario.apellidos_usuario}?"):
        eliminar_usuario(id_usuario)
        print("Usuario eliminado exitosamente.")
    else:
        print("Operación cancelada.")

## ========================================================================================
