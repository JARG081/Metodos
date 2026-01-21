def interpolacion_lineal(x, fx, xi):
    print("Interpolación lineal con puntos:")
    print(f"  x₀ = {x[0]}, f(x₀) = {fx[0]}")
    print(f"  x₁ = {x[1]}, f(x₁) = {fx[1]}")

    # Paso 1: calcular la pendiente
    m = (fx[1] - fx[0]) / (x[1] - x[0])
    print(f"\nPaso 1: Calcular la pendiente (b₁)")
    print(f"  b₁ = (f(x₁) - f(x₀)) / (x₁ - x₀) = ({fx[1]} - {fx[0]}) / ({x[1]} - {x[0]}) = {m:.7f}")

    # Paso 2: calcular b₀ = f(x₀)
    b0 = fx[0]
    print(f"Paso 2: b₀ = f(x₀) = {b0}")

    # Paso 3: expresión del polinomio
    print("\nPolinomio resultante:")
    print(f"  f(x) = {b0:.7f} + {m:.7f}·(x - {x[0]})")

    # Paso 4: Evaluar en xi
    yi = b0 + m * (xi - x[0])
    print(f"\nEvaluando en x = {xi}:")
    print(f"  f({xi}) = {b0:.7f} + {m:.7f}·({xi} - {x[0]}) = {yi:.7f}")

    return yi

# Ejemplo de uso
if __name__ == "__main__":
    x = [1, 4]
    fx = [0, 1.386294]
    xi = 2
    interpolacion_lineal(x, fx, xi)
