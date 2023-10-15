import heapq

def buscar_voraz_primero_mejor(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(heuristica(inicio), inicio)]
    visitados = set()

    while cola_prioridad:
        _, nodo = heapq.heappop(cola_prioridad)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return visitados

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (heuristica(vecino), vecino))

# Ejemplo de grafo no dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

# Función heurística (puede personalizarse)
def heuristica(nodo):
    # En este ejemplo, simplemente devolvemos la longitud de la lista de vecinos del nodo
    return len(grafo[nodo])

camino = buscar_voraz_primero_mejor(grafo, inicio, objetivo, heuristica)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontro un camino.")
