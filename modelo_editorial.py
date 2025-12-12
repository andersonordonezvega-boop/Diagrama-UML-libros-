class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Editorial: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}")