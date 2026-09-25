from persistent import Persistent
from persistent.list import PersistentList


class Artista(Persistent):
    def __init__(self, id_artista, nombre, nacionalidad, anio_nacimiento):
        self.id_artista = id_artista
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.anio_nacimiento = anio_nacimiento

    def __str__(self):
        return f"{self.id_artista} - {self.nombre} ({self.nacionalidad})"


class Coleccion(Persistent):
    def __init__(self, id_coleccion, nombre, descripcion):
        self.id_coleccion = id_coleccion
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id_coleccion} - {self.nombre}"


class Sala(Persistent):
    def __init__(self, id_sala, nombre, capacidad, ubicacion):
        self.id_sala = id_sala
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.exposiciones = PersistentList()

    def tiene_capacidad(self):
        return len(self.exposiciones) < self.capacidad

    def agregar_exposicion(self, exposicion):
        if exposicion not in self.exposiciones and self.tiene_capacidad():
            self.exposiciones.append(exposicion)
            return True
        return False

    def __str__(self):
        return f"{self.id_sala} - {self.nombre} | {self.ubicacion}"


class Visitante(Persistent):
    def __init__(self, id_visitante, nombre, institucion, contacto):
        self.id_visitante = id_visitante
        self.nombre = nombre
        self.institucion = institucion
        self.contacto = contacto

    def __str__(self):
        return f"{self.id_visitante} - {self.nombre} | {self.institucion}"


class Obra(Persistent):
    def __init__(
        self, id_obra, titulo, anio, tipo, descripcion,
        estado="Disponible", artista=None, coleccion=None, sala=None
    ):
        self.id_obra = id_obra
        self.titulo = titulo
        self.anio = anio
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = estado
        self.artista = artista
        self.coleccion = coleccion
        self.sala = sala

    def cambiar_ubicacion(self, nueva_sala):
        self.sala = nueva_sala

    def prestar(self):
        if self.estado == "Disponible":
            self.estado = "Prestada"
            return True
        return False

    def devolver(self):
        self.estado = "Disponible"

    def esta_disponible(self):
        return self.estado == "Disponible"

    def __str__(self):
        artista = self.artista.nombre if self.artista else "Sin artista"
        coleccion = self.coleccion.nombre if self.coleccion else "Sin colección"
        sala = self.sala.nombre if self.sala else "Sin sala"
        return (
            f"{self.id_obra} - {self.titulo} ({self.anio}) | "
            f"{artista} | {coleccion} | {sala} | {self.estado}"
        )


class Exposicion(Persistent):
    def __init__(self, id_exposicion, nombre, fecha_inicio, fecha_fin, sala=None):
        self.id_exposicion = id_exposicion
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sala = sala
        self.obras = PersistentList()

    def agregar_obra(self, obra):
        if obra not in self.obras:
            self.obras.append(obra)
            obra.estado = "En Exposición"
            obra.sala = self.sala
            return True
        return False

    def retirar_obra(self, obra):
        if obra in self.obras:
            self.obras.remove(obra)
            obra.estado = "Disponible"
            return True
        return False

    def esta_activa(self, fecha_actual):
        return self.fecha_inicio <= fecha_actual <= self.fecha_fin

    def __str__(self):
        sala = self.sala.nombre if self.sala else "Sin sala"
        return f"{self.id_exposicion} - {self.nombre} | Sala: {sala}"


class Prestamo(Persistent):
    def __init__(
        self, id_prestamo, fecha_prestamo, fecha_devolucion,
        destino, obra, visitante, estado="Activo"
    ):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.destino = destino
        self.estado = estado
        self.obra = obra
        self.visitante = visitante

    def registrar_prestamo(self):
        if self.obra.prestar():
            self.estado = "Activo"
            return True
        return False

    def finalizar_prestamo(self):
        self.estado = "Devuelto"
        self.obra.devolver()

    def esta_vigente(self):
        return self.estado == "Activo"

    def __str__(self):
        return (
            f"{self.id_prestamo} | {self.obra.titulo} | "
            f"{self.visitante.nombre} | {self.destino} | {self.estado}"
        )
