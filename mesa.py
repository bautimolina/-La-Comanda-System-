#Esta clase está a cargo de Sahonero Geremías
from pedido import Pedido
class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.pedido = None
        self.mozo = None

    def asignar_mozo(self, mozo):
        self.mozo = mozo
        print(f"Mozo {mozo} asignado a la mesa {self.numero}.")

    def crear_pedido(self, id_pedido):
        self.pedido = Pedido(id_pedido, self.numero)
        print(f"Pedido #{id_pedido} creado para la mesa {self.numero}.")

    def cerrar_mesa(self):
        if self.pedido is None:
            print("No hay ningún pedido en esta mesa.")
            return

        print(f"Mesa {self.numero} cerrada.")
        print(f"Total a pagar: ${self.pedido.calcular_total()}")

        self.pedido = None