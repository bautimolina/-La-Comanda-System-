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
    def __init__(self, nombre, precio, porciones, capacidad, alcohol):
        super().__init__(nombre, precio, porciones)

        self.capacidad = capacidad
        self.alcohol = alcohol


class Comestible(Producto):
     def __init__(self, nombre, precio, porciones, apto_celiaco, vegetariano):
        super().__init__(nombre, precio, porciones)

        self.apto_celiaco = apto_celiaco
        self.vegetariano = vegetariano


class Postre(Producto):
    pass