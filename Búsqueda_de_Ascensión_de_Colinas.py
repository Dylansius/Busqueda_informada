import random

def hill_climbing(func, initial_guess, max_iterations):
    current_solution = initial_guess
    for _ in range(max_iterations):
        neighbors = [current_solution + random.uniform(-0.1, 0.1) for _ in range(10)]
        neighbor_values = [func(neighbor) for neighbor in neighbors]
        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]
        if func(best_neighbor) <= func(current_solution):
            break
        current_solution = best_neighbor
    return current_solution

# Ejemplo de uso:
def objective_function(x):
    return -x**2

initial_guess = 2.0
solution = hill_climbing(objective_function, initial_guess, 100)
print("Maximo local encontrado:", solution)

