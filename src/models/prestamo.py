from datetime import datetime, date

class Prestamo:
    def __init__(
        self,
        id_prestamo: int,
        id_usuario: int,
        id_libro: int,
        fecha_prestamo: datetime,
        fecha_limite: date,
        fecha_devolucion: datetime,
        estado: str,
        nombre_usuario = None,
        titulo_libro = None
    ):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_limite
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
        self.nombre_usuario = nombre_usuario
        self.titulo_libro = titulo_libro

    def __str__(self):
        return f"""
ID préstamo: {self.id_prestamo}
Usuario ID: {self.id_usuario}
Libro ID: {self.id_libro}
Fecha préstamo: {self.fecha_prestamo}
Fecha límite: {self.fecha_limite}
Fecha devolución: {self.fecha_devolucion}
Estado: {self.estado}
""" 