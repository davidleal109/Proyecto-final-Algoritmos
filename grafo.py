class Grafo:
    def __init__(self):
        self.adyacencia ={}

    def agregar_arista(self, origen, destino, peso):
        self.adyacencia.setdefault(origen, []).append((peso, destino))
        self.adyacencia.setdefault(destino, []).append((peso, origen))

    def mostrar(self):
        for nodo in sorted(self.adyacencia):
            print(f"  {nodo}: {sorted(self.adyacencia[nodo])}")

def crear_grafo_acueducto():
    grafo = Grafo()
    tramos = [
        ("A","B", 4), ("A", "C", 2), ("B","C", 1),
        ("B", "D", 5), ("C","D", 8),("C", "E", 10),
        ("D", "E", 2), ("D", "F", 6), ("E","F", 3),
    ]
    for origen, destino, peso in tramos:
        grafo.agregar_arista(origen, destino, peso)
    return grafo
