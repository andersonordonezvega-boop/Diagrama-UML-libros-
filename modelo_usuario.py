class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self, sugerencia):
        print(f"{self.nombre} envió una sugerencia: {sugerencia}")

    def leer(self, articulo):
        print(f"{self.nombre} está leyendo {articulo}")

    def comprar(self, producto):
        print(f"{self.nombre} compró el producto {producto}")

    def vender(self, producto):
        print(f"{self.nombre} vendió el producto {producto}")

    def realizar_reclamacion(self, reclamo):
        print(f"{self.nombre} realizó una reclamación: {reclamo}")

       




