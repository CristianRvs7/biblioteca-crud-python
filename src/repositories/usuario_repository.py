from database.connection import obtener_conexion
from models.usuario import Usuario


## DEFINICION DE FUNCIONES ##

## =============================================================================================

def obtener_usuarios():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios ORDER BY id_usuario ASC")
            resultados = cursor.fetchall()

    usuarios = []

    for fila in resultados:
        usuario = Usuario(
            id_usuario=fila[0],
            nombres_usuario=fila[1],
            apellidos_usuario=fila[2],
            docidentificacion=fila[3],
            correo_usuario=fila[4],
            contacto_usuario=fila[5],
            fecha_registro=fila[6]
        )

        usuarios.append(usuario)

    return usuarios

## =============================================================================================

def obtener_usuario_por_id(id_usuario):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return None
        usuario = Usuario(*fila)
    return usuario



## =============================================================================================

def crear_usuario(usuario):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuarios (
                    nombres_usuario, apellidos_usuario, docidentificacion, correo_usuario, contacto_usuario
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    usuario.nombres_usuario,
                    usuario.apellidos_usuario,
                    usuario.docidentificacion,
                    usuario.correo_usuario,
                    usuario.contacto_usuario,
                )
            )
            conexion.commit()

## ================================================================================================

def actualizar_usuario(usuario):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE usuarios
                SET nombres_usuario = %s,
                    apellidos_usuario = %s,
                    docidentificacion = %s,
                    correo_usuario = %s,
                    contacto_usuario = %s
                WHERE id_usuario = %s
                """,
                (
                    usuario.nombres_usuario,
                    usuario.apellidos_usuario,
                    usuario.docidentificacion,
                    usuario.correo_usuario,
                    usuario.contacto_usuario,
                    usuario.id_usuario
                )
            )
            conexion.commit()

## =================================================================================================

def eliminar_usuario(id_usuario):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM usuarios WHERE id_usuario = %s",
                (id_usuario,)
            )
            if cursor.rowcount == 0:
                print("No existe ese usuario")
            else:
                conexion.commit()