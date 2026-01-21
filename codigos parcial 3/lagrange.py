def lagrange_interpolacion(x, y, xi):
    n = len(x)
    yi = 0

    print("="*100)
    print(f"Interpolación de Lagrange para x = {xi}")
    print("="*100)

    for i in range(n):
        Li = 1
        pasos = []  # Para mostrar la fórmula paso a paso
        for j in range(n):
            if i != j:
                numerador = xi - x[j]
                denominador = x[i] - x[j]
                Li *= numerador / denominador
                pasos.append(f"({xi} - {x[j]}) / ({x[i]} - {x[j]})")
        producto_yL = y[i] * Li
        yi += producto_yL

        print(f"\n>> L_{i}(x):")
        print("    Fórmula: " + " * ".join(pasos))
        print(f"    Resultado numérico de L_{i}(x): {Li:.6f}")
        print(f"    y[{i}] * L_{i}(x) = {y[i]} * {Li:.6f} = {producto_yL:.6f}")

    print("\n" + "="*100)
    print(f">>> Resultado final: f({xi}) ≈ {yi:.6f}")
    print("="*100)
    return yi

# Ejemplo de uso
if __name__ == "__main__":
    x = [1,2,3,5]                   # valores de x_n
    y = [3, 6, 19,99]     # valores de f(x_n)
    xi = 4                          # punto a interpolar
    lagrange_interpolacion(x, y, xi)

####    IMPORTANTE, el grado de la interpolacion n tiene que ser menor a la cantidad de valores en los vectores X,Y
####    Si interpola grado 2 son 3 valores|||||||||||||| si interpola grado 3 son 4 valores