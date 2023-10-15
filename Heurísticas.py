def heuristic_sqrt(n):
    x = n
    while True:
        y = (x + n / x) / 2
        if abs(y - x) < 0.00001:
            return y
        x = y

resultado = heuristic_sqrt(25)
print("Aproximacion de la raiz cuadrada:", resultado)

