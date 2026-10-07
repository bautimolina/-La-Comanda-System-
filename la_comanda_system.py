from producto import Bebida, Comestible, Postre
from mesa import Mesa




coca = Bebida("Coca Cola", 2000, 1, 500, False)

hamburguesa = Comestible(
    "Hamburguesa",
    5000,
    1,
    False,
    False
)

flan = Postre(
    "Flan",
    2500,
    1,
    "Frío"
)




mesa1 = Mesa(5)

mesa1.asignar_mozo("Juan")


mesa1.crear_pedido(1)

mesa1.pedido.agregar_producto(coca)
mesa1.pedido.agregar_producto(hamburguesa)
mesa1.pedido.agregar_producto(flan)

mesa1.pedido.mostrar_pedido()

mesa1.pedido.eliminar_producto("Flan")

mesa1.pedido.mostrar_pedido()

mesa1.cerrar_mesa()