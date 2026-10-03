#Esta clase está a cargo de Molina Bautista

class Producto:
    def __init__(self, nombre, precio, porciones):
        if precio < 0:
            print("El precio no puede ser negativo.")
            precio = 0

        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones

class Bebida(Producto):
    pass

class Comestible(Producto):
    pass

class Postre(Producto):
    pass