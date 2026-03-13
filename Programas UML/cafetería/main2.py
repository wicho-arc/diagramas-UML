from cafetería import *

print("REGISTRO DE PRODUCTOS DE CAFETERIA")

b1 = Bebida(1, "Cafe Americano", 30, "Mediano", "CALIENTE")
b2 = Bebida(2, "Latte", 45, "Grande", "CALIENTE")
b3 = Bebida(3, "Capuccino", 40, "Mediano", "CALIENTE")
b4 = Bebida(4, "Frappuccino", 55, "Grande", "FRIA")
b5 = Bebida(5, "Te Chai", 35, "Mediano", "CALIENTE")
p1 = Postre(6, "Brownie", 30, False, False)
p2 = Postre(7, "Galleta Chocolate", 20, False, False)
p3 = Postre(8, "Cheesecake", 50, False, False)
p4 = Postre(9, "Pastel Zanahoria", 45, False, False)
p5 = Postre(10, "Pan Vegano", 40, True, False)


print(b1.nombre, "-", b1.precio_base)
print(b2.nombre, "-", b2.precio_base)
print(b3.nombre, "-", b3.precio_base)
print(b4.nombre, "-", b4.precio_base)
print(b5.nombre, "-", b5.precio_base)
print(p1.nombre, "-", p1.precio_base)
print(p2.nombre, "-", p2.precio_base)
print(p3.nombre, "-", p3.precio_base)
print(p4.nombre, "-", p4.precio_base)
print(p5.nombre, "-", p5.precio_base)

print("\nPRUEBA DE MODIFICADORES")

b1.agregar_extra("Leche de almendra")
b1.agregar_extra("Sin azucar")

print("Precio final cafe:", b1.calcular_precio_final())

print("\nPRUEBA DE PEDIDO")

pedido1 = Pedido(101)
pedido1.agregar_producto(b1)
pedido1.agregar_producto(p1)
pedido1.agregar_producto(p2)

print("Total del pedido:", pedido1.calcular_total())

print("\nPRUEBA DE CLIENTE")

cliente1 = Cliente(1, "Carlos", "carlos@email.com")
cliente1.realizar_pedido(pedido1)

print("Pedidos en historial:", len(cliente1.historial_pedidos))

print("\nPRUEBA DE INVENTARIO")

inventario = Inventario()
inventario.agregar_ingrediente("Cafe", 10)
inventario.agregar_ingrediente("Leche", 5)
inventario.agregar_ingrediente("Chocolate", 3)
print(inventario.ingredientes)

print("\nPRUEBA DE EMPLEADO")

empleado1 = Empleado(2, "Ana", "ana@email.com", "EMP01", "BARISTA")
empleado1.cambiar_estado_pedido(pedido1, "PREPARANDO")
print("Estado del pedido:", pedido1.estado)
