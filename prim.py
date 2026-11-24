import heapq

def aristas_candidatas(grafo, visitados):
    candidatas = []
    for nodo in visitados:
        for peso, vecino in grafo[nodo]:
            if vecino not in visitados:
                candidatas.append((peso, nodo, vecino))
    return sorted(candidatas)

def prim(grafo, inicio, mostrar=False):

    visitados= set()
    mst_aristas = []
    costo_total= 0

    cola = [(0, inicio, inicio)]
    iteracion = 0

    while cola:
        peso, origen, destino = heapq.heappop(cola)

        if destino in visitados:
            continue                     

        if mostrar:
            if origen == destino:
                print(f"\nIteración 0 -> Inicio en{inicio}")
            else:
                iteracion+= 1
                print(f"\nIteración {iteracion}")
                print(f"  Conectados antes : {sorted(visitados)}")
                cands = aristas_candidatas(grafo, visitados)
                print("  Candidatas       : " +
                      ", ".join(f"{o}-{d}({p})" for p, o, d in cands))
                print(f" Arista elegida: {origen}-{destino}con peso {peso} (la menor)")

        visitados.add(destino)

        if origen != destino:             
            mst_aristas.append((origen, destino, peso))
            costo_total += peso

        if mostrar:
            print(f"Conectados después: {sorted(visitados)}")

        for peso_v, vecino in grafo[destino]:
            if vecino not in visitados:
                heapq.heappush(cola, (peso_v, destino, vecino))

    return mst_aristas, costo_total
