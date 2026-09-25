# Proyecto BDOO - Museo

Proyecto de Bases de Datos Avanzadas para implementar una Base de Datos Orientada a Objetos de un museo usando Python y ZODB.

## Clases implementadas

- Obra
- Artista
- Coleccion
- Exposicion
- Sala
- Prestamo
- Visitante

## Requisitos

- Python 3.12 o superior
- ZODB

Instalación:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

El programa demuestra:

1. Creación de objetos.
2. Almacenamiento en ZODB.
3. Uso de `transaction.commit()`.
4. Cierre de la base de datos.
5. Reapertura de la base de datos.
6. Recuperación de objetos persistentes.
7. Modificación del estado de objetos.
8. Operaciones de lógica de negocio.
9. Consultas del museo.

## Archivos

- `modelos.py`: clases persistentes del proyecto.
- `persistencia.py`: conexión, guardado y cierre de ZODB.
- `datos_demo.py`: datos iniciales.
- `servicios.py`: lógica de negocio.
- `consultas.py`: consultas del sistema.
- `main.py`: prueba completa de persistencia.
- `.gitignore`: archivos que no deben subirse al repositorio.

## Ramas sugeridas para el equipo

Cada integrante puede trabajar en su propia rama:

```bash
git checkout -b samuel-modelos
git checkout -b nimsi-colecciones
git checkout -b ashley-exposiciones
git checkout -b victor-consultas
```

Después de terminar el trabajo de cada rama:

```bash
git add .
git commit -m "Implementa parte asignada del sistema"
git push -u origin nombre-de-la-rama
```

Finalmente, las ramas pueden integrarse a `main` mediante Pull Request en GitHub.
