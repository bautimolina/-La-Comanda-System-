#Esta clase está a cargo de Gambino Octavio

class Pedido:
    def __init__(self, id, mesa):
        self.id = id
        self.mesa = mesa
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} agregado al pedido.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"{nombre} eliminado del pedido.")
                return

        print(f"No se encontró el producto {nombre}.")

    def mostrar_pedido(self):
        print(f"\nPedido #{self.id} - Mesa {self.mesa}")
        print("-------------------------")

        if len(self.productos) == 0:
            print("El pedido está vacío.")
            return

        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")

        print("-------------------------")
        print(f"Total: ${self.calcular_total()}")

    def calcular_total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio

        return total