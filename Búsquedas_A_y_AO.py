import heapq

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1  # Assuming all edges have a weight of 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Ejemplo de grafo no dirigido
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['D']
}

start = 'A'
goal = 'G'

# Función heurística (puede personalizarse)
def heuristic(node, goal):
    # En este ejemplo, simplemente devolvemos la distancia entre el nodo actual y el objetivo
    return abs(ord(node) - ord(goal))

path = a_star_search(graph, start, goal, heuristic)
if path:
    print("Camino encontrado:", path)
else:
    print("No se encontro un camino.")
