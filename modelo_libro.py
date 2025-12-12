class Libro:
    def __init__(self, precio, autor, editorial, anio_edicion, preferencias, genero):
        super().__init__(precio, autor, editorial, anio_edicion, preferencias)
        self.genero = genero