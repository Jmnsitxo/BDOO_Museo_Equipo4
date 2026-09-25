from modelos import Prestamo


def agregar_objeto(root, coleccion, clave, objeto):
    getattr(root, coleccion)[clave] = objeto


def registrar_prestamo(root, id_prestamo, fecha_prestamo, fecha_devolucion,
                       destino, id_obra, id_visitante):
    if id_obra not in root.obras:
        return "No existe la obra."
    if id_visitante not in root.visitantes:
        return "No existe el visitante."

    obra = root.obras[id_obra]
    visitante = root.visitantes[id_visitante]

    if not obra.esta_disponible():
        return "La obra no está disponible."

    prestamo = Prestamo(
        id_prestamo,
        fecha_prestamo,
        fecha_devolucion,
        destino,
        obra,
        visitante
    )

    prestamo.registrar_prestamo()
    root.prestamos[id_prestamo] = prestamo
    return f"Préstamo {id_prestamo} registrado correctamente."


def devolver_obra(root, id_prestamo):
    if id_prestamo not in root.prestamos:
        return "No existe el préstamo."

    prestamo = root.prestamos[id_prestamo]

    if not prestamo.esta_vigente():
        return "El préstamo ya fue finalizado."

    prestamo.finalizar_prestamo()
    return f"Préstamo {id_prestamo} finalizado correctamente."


def mover_obra(root, id_obra, id_sala):
    if id_obra not in root.obras:
        return "No existe la obra."
    if id_sala not in root.salas:
        return "No existe la sala."

    root.obras[id_obra].cambiar_ubicacion(root.salas[id_sala])
    return f"La obra {id_obra} fue movida a {root.salas[id_sala].nombre}."


def agregar_obra_exposicion(root, id_exposicion, id_obra):
    if id_exposicion not in root.exposiciones:
        return "No existe la exposición."
    if id_obra not in root.obras:
        return "No existe la obra."

    exposicion = root.exposiciones[id_exposicion]
    obra = root.obras[id_obra]

    if exposicion.agregar_obra(obra):
        return f"{obra.titulo} agregada a {exposicion.nombre}."
    return "La obra ya pertenece a la exposición."
