from modelo_servidor import Servidor
from modelo_procesador import Procesador
from modelo_recolector import Recolector
from modelo_indexador import Indexador
from modelo_usuario import Usuario
from modelo_libro import Libro
from modelo_revista import Revista
from modelo_articulos_de_segunda_mano import ArticuloSegundaMano
from modelo_novedad import Novedad
from modelo_articuloOnline import ArticuloOnline
from modelo_editorial import Editorial
from modelo_hilo import Hilo

def crear_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cuenta = input("Número de cuenta: ")
    direccion = input("Dirección: ")
    login = input("Login: ")
    password = input("Password: ")
    return Usuario(nombre, apellido, cuenta, direccion, login, password)

def crear_editorial():
    nombre = input("Nombre de la Editorial: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    return Editorial(nombre, direccion, telefono)

def crear_libro(editorial):
    precio_str = input("Precio: ")
    try:
        precio = float(precio_str)
    except ValueError:
        precio = 0.00
    autor = input("Autor: ")
    anio_edicion = input("Año de Edición: ")
    preferencias_str = input("Preferencias (separadas por coma): ")
    preferencias = [p.strip() for p in preferencias_str.split(',')]
    genero = input("Género: ")
    return Libro(precio, autor, editorial, anio_edicion, preferencias, genero)

def crear_articulo_segunda_mano(vendedor_nombre):
    clasificacion = input("Clasificación (ej. Usado): ")
    tema = input("Tema: ")
    return ArticuloSegundaMano(clasificacion, tema, vendedor_nombre)

def mostrar_usuario(usuario):
    print(f"Nombre: {usuario.nombre} {usuario.apellido}")
    print(f"Login: {usuario.login}")

def mostrar_libro(libro):
    libro.ver_catalogo()
    print(f"Género: {libro.genero}")

def mostrar_articulo_segunda_mano(articulo_sm):
    articulo_sm.mostrar()

def menu_principal():
    usuario_actual = None
    editorial_actual = None
    libro_ejemplo = None
    articulo_segunda_mano_ejemplo = None

    procesador_sistema = Procesador()
    servidor_web = Servidor()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear Usuario")
        print("2. Crear Editorial")
        print("3. Crear Libro")
        print("4. Crear Artículo de Segunda Mano")
        print("5. Ver Usuario")
        print("6. Ver Libro")
        print("7. Ver Artículo de Segunda Mano")
        print("8. Simular Compra de Libro")
        print("9. Simular Venta de Segunda Mano")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            usuario_actual = crear_usuario()
        elif opcion == "2":
            editorial_actual = crear_editorial()
        elif opcion == "3":
            if editorial_actual:
                libro_ejemplo = crear_libro(editorial_actual)
            else:
                print("ERROR: Cree una Editorial primero.")
        elif opcion == "4":
            if usuario_actual:
                articulo_segunda_mano_ejemplo = crear_articulo_segunda_mano(usuario_actual.nombre)
            else:
                print("ERROR: Cree un Usuario primero.")
        elif opcion == "5":
            if usuario_actual: mostrar_usuario(usuario_actual)
            else: print("No hay usuario creado.")
        elif opcion == "6":
            if libro_ejemplo: mostrar_libro(libro_ejemplo)
            else: print("No hay libro creado.")
        elif opcion == "7":
            if articulo_segunda_mano_ejemplo: mostrar_articulo_segunda_mano(articulo_segunda_mano_ejemplo)
            else: print("No hay artículo de segunda mano creado.")
        elif opcion == "8":
            if usuario_actual and libro_ejemplo:
                usuario_actual.comprar(libro_ejemplo)
                libro_ejemplo.comprar()
                procesador_sistema.realizar_cobro()
                servidor_web.envia_datos_compra()
                print("Compra simulada.")
            else:
                print("ERROR: Necesita Usuario y Libro creados.")
        elif opcion == "9":
            if usuario_actual and articulo_segunda_mano_ejemplo:
                usuario_actual.vender(articulo_segunda_mano_ejemplo)
                procesador_sistema.mandar_datos_venta()
                servidor_web.envia_datos_venta()
                print("Venta de segunda mano simulada.")
            else:
                print("ERROR: Necesita Usuario y Artículo de Segunda Mano creados.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()