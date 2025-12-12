
class Novedad:
    def __init__(self, precio, autor, editorial, anio_edicion, preferencias, clasificacion, tema):
        super().__init__(precio, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        self.clasificacion = nueva
        print(f"Nueva clasificación: {nueva}")
