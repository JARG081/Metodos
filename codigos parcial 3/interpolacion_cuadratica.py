def interpolacion_cuadratica(x, fx, xi):
    print("Interpolación cuadrática con puntos:")
    for i in range(3):
        print(f"  x{i} = {x[i]}, f(x{i}) = {fx[i]}")

    # Paso 1: calcular b0
    b0 = fx[0]
    print(f"\nPaso 1: b₀ = f(x₀) = {b0}")

    # Paso 2: calcular b1
    b1 = (fx[1] - fx[0]) / (x[1] - x[0])
    print(f"Paso 2: b₁ = (f(x₁) - f(x₀)) / (x₁ - x₀) = ({fx[1]} - {fx[0]}) / ({x[1]} - {x[0]}) = {b1:.7f}")

    # Paso 3: calcular b2
    term1 = (fx[2] - fx[1]) / (x[2] - x[1])
    term2 = (fx[1] - fx[0]) / (x[1] - x[0])
    b2 = (term1 - term2) / (x[2] - x[0])
    print(f"Paso 3:")
    print(f"  Primero, (f(x₂) - f(x₁)) / (x₂ - x₁) = ({fx[2]} - {fx[1]}) / ({x[2]} - {x[1]}) = {term1:.7f}")
    print(f"  Luego, (f(x₁) - f(x₀)) / (x₁ - x₀) = ({fx[1]} - {fx[0]}) / ({x[1]} - {x[0]}) = {term2:.7f}")
    print(f"  Finalmente, b₂ = ({term1:.7f} - {term2:.7f}) / ({x[2]} - {x[0]}) = {b2:.7f}")

    # Paso 4: construir polinomio en forma f(x) = a0 + a1·x + a2·x²
    a0 = b0 - b1 * x[0] + b2 * x[0] * x[1]
    a1 = b1 - b2 * (x[0] + x[1])
    a2 = b2

    print("\nPolinomio resultante en forma desarrollada:")
    print(f"  f(x) = {a0:.7f} + {a1:.7f}·x + {a2:.7f}·x²")

    # Paso 5: Evaluar el polinomio en xi
    yi = a0 + a1 * xi + a2 * xi**2
    print(f"\nEvaluando en x = {xi}:")
    print(f"  f({xi}) = {a0:.7f} + {a1:.7f}·{xi} + {a2:.7f}·{xi}² = {yi:.7f}")

    return yi

# Ejemplo de uso
if __name__ == "__main__":
    x = [1, 4, 6]
    fx = [0, 1.386294, 1.791759]
    xi = 2
    interpolacion_cuadratica(x, fx, xi)
