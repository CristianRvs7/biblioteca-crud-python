class Autor:
    def __init__(self, id_autor : int, nombre_autor : str, apellido_autor : str):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
    
    def __str__(self):
        return f"""
ID: {self.id_autor}
Nombre: {self.nombre_autor} {self.apellido_autor}
               """