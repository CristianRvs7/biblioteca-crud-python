
## DEFINICION DE CLASES ##

class Libro:
    def __init__( self,id_libro: int, isbn: str, titulo: str, id_autor: int, id_categoria: int,
                 id_editorial: int, anio_lanzamiento: int, existencias: int):
        self.id_libro = id_libro
        self.isbn = isbn
        self.titulo = titulo
        self.id_autor = id_autor
        self.id_categoria = id_categoria
        self.id_editorial = id_editorial
        self.anio_lanzamiento = anio_lanzamiento
        self.existencias = existencias

    def __str__(self):
        return f"""
ID: {self.id_libro}
Título: {self.titulo}
ISBN: {self.isbn}
Año: {self.anio_lanzamiento}
Existencias: {self.existencias}
                """