import math
import random

def objective_function(solution):
    # Define tu función objetivo aquí (debe retornar un valor que se busca maximizar o minimizar)
    # En este ejemplo, simplemente calculamos la suma de los elementos de la solución
    return sum(solution)

def generate_neighbor(solution):
    neighbor = solution.copy()
    index = random.randint(0, len(neighbor) - 1)
    neighbor[index] = 1 - neighbor[index]
    return neighbor

def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    best_solution = current_solution
    temperature = initial_temperature

    for _ in range(num_iterations):
        neighbor = generate_neighbor(current_solution)
        current_value = objective_function(current_solution)
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value or random.random() < math.exp((neighbor_value - current_value) / temperature):
            current_solution = neighbor

        if neighbor_value > objective_function(best_solution):
            best_solution = neighbor

        temperature *= cooling_rate

    return best_solution

# Ejemplo de solución inicial (puedes personalizarlo)
initial_solution = [0, 1, 0, 1, 0, 1]

# Parámetros del algoritmo
initial_temperature = 100.0
cooling_rate = 0.99
num_iterations = 1000

best_solution = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)
print("Mejor solucion encontrada:", best_solution)
print("Valor de la funcion objetivo:", objective_function(best_solution))


