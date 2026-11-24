from grafo import crear_grafo_acueducto
from prim import prim
from base_datos import BaseDatos

def ejecutar(grafo, inicio, bd):
    print("\n" + "=" * 55)
    print(f"PRIM COMENZANDO EN LA VEREDA {inicio}")
    print("=" * 55)
    aristas, costo = prim(grafo.adyacencia, inicio, mostrar=True)

    print(f"\nAristas del MST (inicio {inicio}):")
    for origen, destino, peso in aristas:
        print(f"  {origen} --{peso}-- {destino}")
    suma = " + ".join(str(p) for _, _, p in aristas)
    print(f"Costo total = {suma} = {costo} km")
    print(f"Número de aristas = {len(aristas)}")

    bd.guardar_resultado(inicio, aristas, costo)
    return aristas, costo

def main():
    grafo = crear_grafo_acueducto()
    bd = BaseDatos("acueducto.db")

    print("GRAFO UTILIZADO lista de adyacencia: peso, vecino:")
    grafo.mostrar()

    aristas_a, costo_a = ejecutar(grafo, "A", bd)
    aristas_f, costo_f = ejecutar(grafo, "F", bd)

    print("\n" + "=" * 55)
    print("COMPARACIÓN A vs F")
    print("=" * 55)
    mismo_arbol = {frozenset((o, d)) for o, d, _ in aristas_a} == \
                  {frozenset((o, d)) for o, d, _ in aristas_f}
    print(f"Costo desde A: {costo_a}km Costo desde F: {costo_f}km")
    print(f"Cambia el costo? {'No' if costo_a == costo_f else 'Sí'}")
    print(f"Cambia el árbol? {'No' if mismo_arbol else 'Sí'}")

    print("\nDATOS GUARDADOS (id, inicio, origen, destino, peso, costo):")
    for fila in bd.consultar_resultados():
        print("", fila)
    bd.cerrar()

if __name__ == "__main__":
    main()
