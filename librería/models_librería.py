class Material:
    def __init__(self, id_material, titulo, año, disponible=True):
        self.id_material = id_material
        self.titulo = titulo
        self.anio = año
        self.disponible = disponible


class Libro(Material):
    def __init__(self, id_material, titulo, año, autor, isbn, genero):
        super().__init__(id_material, titulo, año)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero


class Revista(Material):
    def __init__(self, id_material, titulo, año, edicion, periodicidad):
        super().__init__(id_material, titulo, año)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, id_material, titulo, año, tipo_archivo, url, tamaño):
        super().__init__(id_material, titulo, año)
        self.tipo_archivo = tipo_archivo
        self.url = url
        self.tamaño = tamaño

class Persona:
    def __init__(self, id_persona, nombre):
        self.id_persona = id_persona
        self.nombre = nombre

class Usuario(Persona):
    def __init__(self, id_persona, nombre, limite):
        super().__init__(id_persona, nombre)
        self.limite_prestamos = limite
        self.lista_activa = []

    def puede_pedir(self):
        return len(self.lista_activa) < self.limite_prestamos

class Bibliotecario(Persona):
    def __init__(self, id_persona, nombre):
        super().__init__(id_persona, nombre)

    def gestionar_prestamo(self, prestamo):
        if prestamo.material.disponible:
            prestamo.material.disponible = False
            prestamo.usuario.lista_activa.append(prestamo)
            return True
        return False

    def transferir_material(self, material, sucursal_destino):
        sucursal_destino.catalogo.append(material)

class Sucursal:
    def __init__(self, id_sucursal, nombre):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.catalogo = []

    def agregar_material(self, material):
        self.catalogo.append(material)

class Prestamo:
    def __init__(self, id_prestamo, fecha_inicio, fecha_fin, usuario, material):
        self.id_prestamo = id_prestamo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False
    def calcular_multa(self, dias_retraso):
        self.monto = dias_retraso * 5
        return self.monto
    def bloquear_usuario(self, usuario):
        usuario.limite_prestamos = 0

class Catalogo:
    def __init__(self):
        self.sucursales = []
    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)
    def buscar_por_autor(self, autor):
        resultados = []
        for suc in self.sucursales:
            for mat in suc.catalogo:
                if isinstance(mat, Libro) and mat.autor == autor:
                    resultados.append(mat)
        return resultados
    def buscar_en_todas(self, titulo):
        resultados = []
        for suc in self.sucursales:
            for mat in suc.catalogo:
                if titulo in mat.titulo:
                    resultados.append(mat)
        return resultados