def mostrar_obras(root):
    print("\n--- TODAS LAS OBRAS ---")
    for obra in root.obras.values():
        print(obra)


def obras_disponibles(root):
    print("\n--- OBRAS DISPONIBLES ---")
    for obra in root.obras.values():
        if obra.esta_disponible():
            print(obra)


def obras_por_artista(root, nombre_artista):
    print(f"\n--- OBRAS DE {nombre_artista.upper()} ---")
    encontradas = 0
    for obra in root.obras.values():
        if obra.artista and obra.artista.nombre.lower() == nombre_artista.lower():
            print(obra)
            encontradas += 1

    if encontradas == 0:
        print("No se encontraron obras.")


def prestamos_activos(root):
    print("\n--- PRÉSTAMOS ACTIVOS ---")
    encontrados = 0
    for prestamo in root.prestamos.values():
        if prestamo.esta_vigente():
            print(prestamo)
            encontrados += 1

    if encontrados == 0:
        print("No hay préstamos activos.")


def obras_en_exposicion(root):
    print("\n--- OBRAS EN EXPOSICIÓN ---")
    encontradas = 0
    for obra in root.obras.values():
        if obra.estado == "En Exposición":
            print(obra)
            encontradas += 1

    if encontradas == 0:
        print("No hay obras en exposición.")


def prestamos_por_visitante(root, nombre_visitante):
    print(f"\n--- PRÉSTAMOS DE {nombre_visitante.upper()} ---")
    encontrados = 0
    for prestamo in root.prestamos.values():
        if prestamo.visitante.nombre.lower() == nombre_visitante.lower():
            print(prestamo)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron préstamos.")


def resumen(root):
    print("\n========== RESUMEN DEL MUSEO ==========")
    print("Artistas:", len(root.artistas))
    print("Colecciones:", len(root.colecciones))
    print("Salas:", len(root.salas))
    print("Visitantes:", len(root.visitantes))
    print("Obras:", len(root.obras))
    print("Exposiciones:", len(root.exposiciones))
    print("Préstamos:", len(root.prestamos))
    print("=======================================")
