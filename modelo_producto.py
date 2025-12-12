class Producto:
    def __init__(self, precio, autor, editorial, anio_edicion, preferencias):
        self.precio = precio
        self.autor = autor
        self.editorial = editorial
        self.anio_edicion = anio_edicion
        self.preferencias = preferencias

    def vender(self):
        print("El producto ha sido vendido.")

    def comprar(self):
        print("El producto ha sido comprado.")

    def ver_catalogo(self):
        print(f"Autor: {self.autor}, Editorial: {self.editorial}, Precio: {self.precio}")
