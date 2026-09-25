import ZODB
import ZODB.FileStorage
import transaction


class BaseDatosMuseo:
    def __init__(self, archivo="museo.fs"):
        self.archivo = archivo
        self.storage = None
        self.db = None
        self.connection = None
        self.root = None

    def abrir(self):
        self.storage = ZODB.FileStorage.FileStorage(self.archivo)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        # Estructuras persistentes principales
        if "artistas" not in self.root:
            self.root.artistas = {}
        if "colecciones" not in self.root:
            self.root.colecciones = {}
        if "salas" not in self.root:
            self.root.salas = {}
        if "visitantes" not in self.root:
            self.root.visitantes = {}
        if "obras" not in self.root:
            self.root.obras = {}
        if "exposiciones" not in self.root:
            self.root.exposiciones = {}
        if "prestamos" not in self.root:
            self.root.prestamos = {}

        transaction.commit()
        return self.root

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        if self.connection:
            self.connection.close()
        if self.db:
            self.db.close()
        if self.storage:
            self.storage.close()
