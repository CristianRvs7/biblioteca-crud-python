from datetime import datetime

class Usuario:
    def __init__(self, id_usuario : int, nombres_usuario : str, apellidos_usuario : str, docidentificacion : str, correo_usuario : str, contacto_usuario : str, fecha_registro : datetime ):
        
        self.id_usuario = id_usuario
        self.nombres_usuario = nombres_usuario
        self.apellidos_usuario = apellidos_usuario
        self.docidentificacion = docidentificacion
        self.correo_usuario = correo_usuario
        self.contacto_usuario = contacto_usuario
        self.fecha_registro = fecha_registro
        
    def __str__(self):
        return f"""
ID: {self.id_usuario}
Nombre: {self.nombres_usuario} {self.apellidos_usuario}
Documento: {self.docidentificacion}
Correo: {self.correo_usuario}
Contacto: {self.contacto_usuario}
Miembro desde: {self.fecha_registro}
        """