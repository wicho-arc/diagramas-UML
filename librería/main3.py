from models_librería import *

print("REGISTRO DE MATERIALES (10 OBJETOS)")

l1 = Libro(1, "Python Basico", 2020, "Juan Perez", "111", "Programacion")
l2 = Libro(2, "POO Avanzado", 2021, "Ana Lopez", "222", "Tecnologia")
l3 = Libro(3, "Redes", 2019, "Luis Diaz", "333", "Tecnologia")
l4 = Libro(4, "Bases de Datos", 2018, "Maria Ruiz", "444", "Tecnologia")
l5 = Libro(5, "IA", 2022, "Carlos Vega", "555", "Tecnologia")

r1 = Revista(6, "Tech Hoy", 2023, 10, "Mensual")
r2 = Revista(7, "Ciencia", 2023, 5, "Mensual")
r3 = Revista(8, "Gaming", 2022, 8, "Mensual")

d1 = MaterialDigital(9, "Curso Python", 2023, "PDF", "url1", 50)
d2 = MaterialDigital(10, "Curso IA", 2023, "PDF", "url2", 60)

print(l1.titulo)
print(l2.titulo)
print(l3.titulo)
print(l4.titulo)
print(l5.titulo)
print(r1.titulo)
print(r2.titulo)
print(r3.titulo)
print(d1.titulo)
print(d2.titulo)


print("\nPRUEBA DE PRESTAMO")

usuario = Usuario(1, "Carlos", 3)
bibliotecario = Bibliotecario(2, "Ana")

prestamo = Prestamo(1, "2024-01-01", "2024-01-10", usuario, l1)

if bibliotecario.gestionar_prestamo(prestamo):
    print("Prestamo realizado")
else:
    print("No disponible")


print("\nPRUEBA DE PENALIZACION")

penal = Penalizacion(0, "Retraso")

print("Multa:", penal.calcular_multa(3))

penal.bloquear_usuario(usuario)

print("Limite usuario:", usuario.limite_prestamos)


print("\nPRUEBA DE CATALOGO")

s1 = Sucursal(1, "Centro")
s1.agregar_material(l1)
s1.agregar_material(l2)

catalogo = Catalogo()
catalogo.agregar_sucursal(s1)

res = catalogo.buscar_por_autor("Juan Perez")

for r in res:
    print("Encontrado:", r.titulo)

