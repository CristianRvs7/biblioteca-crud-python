class Categoria:
    def __init__(self, id_categoria : int, nombre_categoria : str):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria
    
    def __str__(self):
        return f"""
ID: {self.id_categoria}
Categoria: {self.nombre_categoria}
               """