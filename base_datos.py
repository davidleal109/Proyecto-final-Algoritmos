import sqlite3


class BaseDatos:
    def __init__(self, nombre="acueducto.db"):
        self.conexion = sqlite3.connect(nombre)
        self.crear_tablas()

    def crear_tablas(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ejecuciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nodo_inicial TEXT NOT NULL,
                costo_total INTEGER NOT NULL,
                fecha TEXT DEFAULT CURRENT_TIMESTAMP
            )""")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aristas_mst (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ejecucion_id INTEGER NOT NULL,
                origen TEXT NOT NULL,
                destino TEXT NOT NULL,
                peso INTEGER NOT NULL,
                FOREIGN KEY (ejecucion_id) REFERENCES ejecuciones(id)
            )""")
        self.conexion.commit()

    def guardar_resultado(self, nodo_inicial, aristas, costo_total):
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO ejecuciones (nodo_inicial, costo_total) VALUES (?, ?)",
            (nodo_inicial, costo_total))
        ejecucion_id = cursor.lastrowid
        for origen, destino, peso in aristas:
            cursor.execute(
                "INSERT INTO aristas_mst (ejecucion_id, origen, destino, peso) "
                "VALUES (?, ?, ?, ?)", (ejecucion_id, origen, destino, peso))
        self.conexion.commit()
        return ejecucion_id

    def consultar_resultados(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT e.id, e.nodo_inicial, a.origen, a.destino, a.peso, e.costo_total
            FROM ejecuciones e JOIN aristas_mst a ON a.ejecucion_id = e.id
            ORDER BY e.id, a.id""")
        return cursor.fetchall()

    def cerrar(self):
        self.conexion.close()
