import random

def objective_function(solution):
    # Define tu función objetivo aquí (debe retornar un valor que se busca maximizar o minimizar)
    # En este ejemplo, simplemente calculamos la suma de los elementos de la solución
    return sum(solution)

def perturb_solution(solution):
    neighbor = solution.copy()
    index = random.randint(0, len(neighbor) - 1)
    neighbor[index] = 1 - neighbor[index]
    return neighbor

def get_best_solution(neighbors, tabu_list):
    best_solution = neighbors[0]
    best_value = objective_function(best_solution)
    for neighbor in neighbors:
        value = objective_function(neighbor)
        if value > best_value and neighbor not in tabu_list:
            best_value = value
            best_solution = neighbor
    return best_solution, best_value

def buscar_tabu(initial_solution, num_iterations, num_neighbors):
    current_solution = initial_solution
    best_solution = current_solution
    tabu_size = 10
    tabu_list = []

    for _ in range(num_iterations):
        neighborhood = generate_neighbors(current_solution, num_neighbors, tabu_list)
        current_solution, improvement = get_best_solution(neighborhood, tabu_list)

        if improvement > 0:
            best_solution = current_solution

        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution

def generate_neighbors(solution, num_neighbors, tabu_list):
    neighbors = []

    while len(neighbors) < num_neighbors:
        neighbor = perturb_solution(solution)
        if neighbor not in tabu_list and neighbor not in neighbors:
            neighbors.append(neighbor)

    return neighbors

# Ejemplo de solución inicial (puedes personalizarlo)
initial_solution = [0, 1, 0, 1, 0, 1]

# Número de iteraciones y número de vecinos
num_iterations = 100
num_neighbors = 10

best_solution = buscar_tabu(initial_solution, num_iterations, num_neighbors)
print("Mejor solucion encontrada:", best_solution)
print("Valor de la funcion objetivo:", objective_function(best_solution))


