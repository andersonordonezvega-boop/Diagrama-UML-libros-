class Revista:
    def __init__(self, precio, autor, editorial, anio_edicion, preferencias, categoria):
        super().__init__(precio, autor, editorial, anio_edicion, preferencias)
        self.categoria = categoria
