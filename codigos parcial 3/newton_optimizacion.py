import sympy as sp

def newton_optimizacion(expr_str, x0, tol=1e-5, max_iter=100):
    x = sp.symbols('x')
    f = sp.sympify(expr_str)
    df = sp.diff(f, x)
    ddf = sp.diff(df, x)

    f_func = sp.lambdify(x, f, 'math')
    df_func = sp.lambdify(x, df, 'math')
    ddf_func = sp.lambdify(x, ddf, 'math')

    iteracion = 0
    error = float('inf')

    print("="*100)
    print("Método de Newton para Optimización")
    print(f"Función: f(x) = {expr_str}")
    print(f"Derivada: f'(x) = {df}")
    print(f"Segunda derivada: f''(x) = {ddf}")
    print("="*100)

    # Encabezado de la tabla (se imprimirá después de los procedimientos)
    tabla_resultados = []
    
    while error > tol and iteracion < max_iter:
        fx = f_func(x0)
        dfx = df_func(x0)
        ddfx = ddf_func(x0)

        if ddfx == 0:
            print("Derivada segunda es cero. No se puede continuar.")
            break

        x1 = x0 - dfx / ddfx
        error = abs((x1 - x0) / x1)

        # Guardar para tabla después
        tabla_resultados.append((iteracion, x0, fx, dfx, ddfx, error))

        # Mostrar paso a paso antes de la tabla
        print(f"\n>> Iteración {iteracion}")
        print(f"    1. x_{iteracion} = {x0:.6f}")
        print(f"    2. Evaluar f(x_{iteracion}) = {fx:.6f}")
        print(f"    3. Evaluar f'(x_{iteracion}) = {dfx:.6f}")
        print(f"    4. Evaluar f''(x_{iteracion}) = {ddfx:.6f}")
        print("    5. Aplicar fórmula de Newton:")
        print(f"       x_{iteracion + 1} = x_{iteracion} - f'(x)/f''(x)")
        print(f"                     = {x0:.6f} - ({dfx:.6f}) / ({ddfx:.6f})")
        print(f"                     = {x1:.6f}")
        print(f"    6. Calcular error relativo:")
        print(f"       Error = |x_{iteracion + 1} - x_{iteracion}| / |x_{iteracion + 1}|")
        print(f"             = |{x1:.6f} - {x0:.6f}| / |{x1:.6f}| = {error:.6e}")

        x0 = x1
        iteracion += 1

    # Imprimir tabla resumen después de mostrar los pasos
    print("\n" + "="*100)
    print(f"{'Iteración':<10}{'x':>10}{'f(x)':>15}{'f\'(x)':>15}{'f\'\'(x)':>15}{'Error':>15}")
    print("="*100)
    for it, xval, fxval, dfxval, ddfxval, err in tabla_resultados:
        print(f"{it:<10}{xval:>10.6f}{fxval:>15.6f}{dfxval:>15.6f}{ddfxval:>15.6f}{err:>15.6e}")

    print("\n" + "="*100)
    print(f">>> Punto óptimo encontrado: x = {x0:.6f}, f(x) = {f_func(x0):.6f}")
    print("="*100)

if __name__ == "__main__":
    # Usar sin(x), no sen(x)
    #sin(),cos(),tan(),acos(),
    newton_optimizacion("2*sin(x)-(x**2)/10", x0=2.5)
