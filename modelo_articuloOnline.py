class ArticuloOnline:
    def __init__(self, precio, autor, editorial, anio_edicion, preferencias, tema):
        super().__init__(precio, autor, editorial, anio_edicion, preferencias)
        self.tema = tema

    def publicar(self):
        print(f"Artículo online sobre {self.tema} publicado.")
