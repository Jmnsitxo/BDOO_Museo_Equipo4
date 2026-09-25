from datetime import date
from modelos import Artista, Coleccion, Sala, Visitante, Obra, Exposicion


def cargar_datos_si_esta_vacio(root):
    if len(root.obras) > 0:
        return False

    # Artistas
    a1 = Artista("A001", "Frida Kahlo", "Mexicana", 1907)
    a2 = Artista("A002", "Diego Rivera", "Mexicana", 1886)
    a3 = Artista("A003", "Vincent van Gogh", "Neerlandesa", 1853)

    root.artistas[a1.id_artista] = a1
    root.artistas[a2.id_artista] = a2
    root.artistas[a3.id_artista] = a3

    # Colecciones
    c1 = Coleccion("C001", "Arte Mexicano", "Obras de artistas mexicanos.")
    c2 = Coleccion("C002", "Arte Europeo", "Obras de artistas europeos.")

    root.colecciones[c1.id_coleccion] = c1
    root.colecciones[c2.id_coleccion] = c2

    # Salas
    s1 = Sala("S001", "Sala Principal", 5, "Planta baja")
    s2 = Sala("S002", "Sala Histórica", 4, "Primer piso")

    root.salas[s1.id_sala] = s1
    root.salas[s2.id_sala] = s2

    # Visitantes / entidades receptoras
    v1 = Visitante("V001", "Museo Nacional", "Museo Nacional", "contacto@museo.mx")
    v2 = Visitante("V002", "Galería Central", "Galería Central", "galeria@central.mx")

    root.visitantes[v1.id_visitante] = v1
    root.visitantes[v2.id_visitante] = v2

    # Obras
    o1 = Obra(
        "O001", "Las dos Fridas", 1939, "Pintura",
        "Óleo sobre lienzo.", artista=a1, coleccion=c1, sala=s1
    )
    o2 = Obra(
        "O002", "El cargador de flores", 1935, "Pintura",
        "Obra de Diego Rivera.", artista=a2, coleccion=c1, sala=s1
    )
    o3 = Obra(
        "O003", "La noche estrellada", 1889, "Pintura",
        "Paisaje nocturno.", artista=a3, coleccion=c2, sala=s2
    )

    root.obras[o1.id_obra] = o1
    root.obras[o2.id_obra] = o2
    root.obras[o3.id_obra] = o3

    # Exposición
    e1 = Exposicion(
        "E001",
        "Maestros de la pintura",
        date(2026, 9, 1),
        date(2026, 12, 15),
        s1
    )
    root.exposiciones[e1.id_exposicion] = e1
    s1.agregar_exposicion(e1)

    return True
