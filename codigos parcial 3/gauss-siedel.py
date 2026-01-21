def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=100):
    n = len(A)
    x = [0.0 for _ in range(n)] if x0 is None else x0.copy()
    error = float('inf')
    iteracion = 0

    # Guardar resultados para la tabla
    tabla_resultados = []

    print("="*100)
    print("Método de Gauss-Seidel para resolver sistemas de ecuaciones")
    print("="*100)

    while error > tol and iteracion < max_iter:
        x_new = x.copy()
        print(f"\n>> Iteración {iteracion}:")
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))  # anteriores ya actualizados
            sum2 = sum(A[i][j] * x[j] for j in range(i+1, n))  # posteriores sin actualizar
            xi_old = x[i]
            xi_new = (b[i] - sum1 - sum2) / A[i][i]
            x_new[i] = xi_new

            print(f"x{i} = (b[{i}] - sum1 - sum2) / A[{i}][{i}]")
            print(f"    = ({b[i]} - {sum1:.6f} - {sum2:.6f}) / {A[i][i]}")
            print(f"    = {xi_new:.6f}")

        error = max(abs((x_new[i] - x[i]) / x_new[i]) if x_new[i] != 0 else 0 for i in range(n))

        print(f"\nValores actualizados de x en iteración {iteracion}:")
        for i in range(n):
            print(f"  x{i} = {x_new[i]:.6f}")
        print(f">> Error relativo máximo: {error:.6e}")
        print("-"*100)

        # Guardar valores para la tabla
        tabla_resultados.append((iteracion, x_new.copy(), error))

        x = x_new
        iteracion += 1

    # Tabla final
    print("\n" + "="*100)
    encabezado = f"{'Iteración':<10}" + "".join([f"x{i:<15}" for i in range(n)]) + "Error"
    print(encabezado)
    print("="*100)
    for it, x_vals, err in tabla_resultados:
        fila = f"{it:<10}" + "".join([f"{val:<15.6f}" for val in x_vals]) + f"{err:.6e}"
        print(fila)

    # Solución final
    print("\n" + "="*100)
    print(">>> Solución aproximada encontrada:")
    for i in range(n):
        print(f"\tx{i} = {x[i]:.6f}")
    print("="*100)


# Ejemplo de uso
if __name__ == "__main__":
    A = [
        [3, -0.1, -0.2],
        [0.1, 7, -0.3],
        [0.31, -0.2, 10]
    ]
    b = [7.85, -19.3, 71.4]
    gauss_seidel(A, b)
