class Editorial:
    def __init__(self, id_editorial, nombre_editorial):
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial

    def __str__(self):
        return f"ID: {self.id_editorial}, Nombre: {self.nombre_editorial}"