from datetime import date
from persistencia import BaseDatosMuseo
from datos_demo import cargar_datos_si_esta_vacio
from servicios import (
    registrar_prestamo,
    devolver_obra,
    mover_obra,
    agregar_obra_exposicion
)
from consultas import (
    mostrar_obras,
    obras_disponibles,
    obras_por_artista,
    prestamos_activos,
    obras_en_exposicion,
    prestamos_por_visitante,
    resumen
)


def primera_apertura():
    print("=== 1. ABRIR BASE DE DATOS ===")
    bd = BaseDatosMuseo()
    root = bd.abrir()

    nuevos = cargar_datos_si_esta_vacio(root)
    if nuevos:
        print("Se crearon y guardaron los datos iniciales.")
    else:
        print("Los datos ya existían en ZODB.")

    # Lógica de negocio
    print("\n=== 2. OPERACIONES DE NEGOCIO ===")
    print(agregar_obra_exposicion(root, "E001", "O001"))
    print(registrar_prestamo(
        root,
        "P001",
        date(2026, 9, 25),
        date(2026, 10, 25),
        "Museo Nacional",
        "O002",
        "V001"
    ))
    print(mover_obra(root, "O003", "S002"))

    # Guardar cambios en ZODB
    bd.guardar()
    print("\ntransaction.commit() ejecutado correctamente.")

    # Consultas
    mostrar_obras(root)
    obras_disponibles(root)
    obras_por_artista(root, "Frida Kahlo")
    prestamos_activos(root)
    obras_en_exposicion(root)
    prestamos_por_visitante(root, "Museo Nacional")
    resumen(root)

    print("\n=== 3. CERRAR APLICACIÓN ===")
    bd.cerrar()
    print("Base de datos cerrada.")


def segunda_apertura():
    print("\n=== 4. VOLVER A ABRIR LA APLICACIÓN ===")
    bd = BaseDatosMuseo()
    root = bd.abrir()

    print("Objetos recuperados después de cerrar y abrir:")
    mostrar_obras(root)
    prestamos_activos(root)
    resumen(root)

    print("\nLa información continúa disponible en ZODB.")

    # Ejemplo de modificación persistente
    print("\n=== 5. MODIFICAR ESTADO DE UN OBJETO ===")
    if "P001" in root.prestamos and root.prestamos["P001"].esta_vigente():
        print(devolver_obra(root, "P001"))
        bd.guardar()
        print("Cambio guardado con transaction.commit().")
    else:
        print("El préstamo P001 ya había sido devuelto.")

    mostrar_obras(root)
    prestamos_activos(root)

    bd.cerrar()


if __name__ == "__main__":
    primera_apertura()
    segunda_apertura()
