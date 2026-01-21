import sympy as sp

def runge_kutta(expr_str, x0, y0, h, xn, orden=4):
    x, y = sp.symbols('x y')
    f_expr = sp.sympify(expr_str)
    f = sp.lambdify((x, y), f_expr, 'math')

    x_actual = x0
    y_actual = y0
    tabla_resultados = []
    ea_anterior = None
    y_anterior = None

    print("=" * 100)
    print(f"Resolviendo con Runge-Kutta de orden {orden}, desde x = {x0} hasta x = {xn}")
    print(f"f(x, y) = {expr_str}")
    print(f"h = {h}, y({x0}) = {y0}")
    print("=" * 100)

    paso = 0
    while round(x_actual, 10) <= round(xn, 10):
        paso += 1
        print(f"\n================== Iteración {paso} ==================")
        print(f"x_actual = {x_actual:.6f}, y_actual = {y_actual:.6f}")

        k1 = k2 = k3 = k4 = 0
        y_siguiente = y_actual

        if orden == 2:
            print("\nCalculando k1:")
            print(f"k1 = h * f(x_actual, y_actual)")
            print(f"k1 = {h} * f({x_actual:.6f}, {y_actual:.6f})")
            k1 = h * f(x_actual, y_actual)
            print(f"k1 = {k1:.6f}")

            print("\nCalculando k2:")
            print(f"k2 = h * f(x_actual + h, y_actual + k1)")
            print(f"k2 = {h} * f({x_actual:.6f} + {h}, {y_actual:.6f} + {k1:.6f})")
            print(f"k2 = {h} * f({x_actual + h:.6f}, {y_actual + k1:.6f})")
            k2 = h * f(x_actual + h, y_actual + k1)
            print(f"k2 = {k2:.6f}")

            print("\nCalculando y_siguiente:")
            print(f"y_siguiente = y_actual + (k1 + k2) / 2")
            print(f"y_siguiente = {y_actual:.6f} + ({k1:.6f} + {k2:.6f}) / 2")
            y_siguiente = y_actual + (k1 + k2) / 2
            print(f"y_siguiente = {y_siguiente:.6f}")

        elif orden == 3:
            print("\nCalculando k1:")
            print(f"k1 = h * f(x_actual, y_actual)")
            print(f"k1 = {h} * f({x_actual:.6f}, {y_actual:.6f})")
            k1 = h * f(x_actual, y_actual)
            print(f"k1 = {k1:.6f}")

            print("\nCalculando k2:")
            print(f"k2 = h * f(x_actual + h / 2, y_actual + k1 / 2)")
            print(f"k2 = {h} * f({x_actual:.6f} + {h} / 2, {y_actual:.6f} + {k1:.6f} / 2)")
            print(f"k2 = {h} * f({x_actual + h / 2:.6f}, {y_actual + k1 / 2:.6f})")
            k2 = h * f(x_actual + h / 2, y_actual + k1 / 2)
            print(f"k2 = {k2:.6f}")

            print("\nCalculando k3:")
            print(f"k3 = h * f(x_actual + h, y_actual - k1 + 2 * k2)")
            print(f"k3 = {h} * f({x_actual:.6f} + {h}, {y_actual:.6f} - {k1:.6f} + 2 * {k2:.6f})")
            print(f"k3 = {h} * f({x_actual + h:.6f}, {y_actual - k1 + 2 * k2:.6f})")
            k3 = h * f(x_actual + h, y_actual - k1 + 2 * k2)
            print(f"k3 = {k3:.6f}")

            print("\nCalculando y_siguiente:")
            print(f"y_siguiente = y_actual + (k1 + 4 * k2 + k3) / 6")
            print(f"y_siguiente = {y_actual:.6f} + ({k1:.6f} + 4 * {k2:.6f} + {k3:.6f}) / 6")
            y_siguiente = y_actual + (k1 + 4 * k2 + k3) / 6
            print(f"y_siguiente = {y_siguiente:.6f}")


        elif orden == 4:
            print("\nCalculando k1:")
            print(f"k1 = h * f(x_actual, y_actual)")
            print(f"k1 = {h} * f({x_actual:.6f}, {y_actual:.6f})")
            k1 = h * f(x_actual, y_actual)
            print(f"k1 = {k1:.6f}")

            print("\nCalculando k2:")
            print(f"k2 = h * f(x_actual + h / 2, y_actual + k1 / 2)")
            print(f"k2 = {h} * f({x_actual:.6f} + {h} / 2, {y_actual:.6f} + {k1:.6f} / 2)")
            print(f"k2 = {h} * f({x_actual + h / 2:.6f}, {y_actual + k1 / 2:.6f})")
            k2 = h * f(x_actual + h / 2, y_actual + k1 / 2)
            print(f"k2 = {k2:.6f}")


            print("\nCalculando k3:")
            print(f"k3 = h * f(x_actual + h / 2, y_actual + k2 / 2)")
            print(f"k3 = {h} * f({x_actual:.6f} + {h} / 2, {y_actual:.6f} + {k2:.6f} / 2)")
            print(f"k3 = {h} * f({x_actual + h / 2:.6f}, {y_actual + k2 / 2:.6f})")
            k3 = h * f(x_actual + h / 2, y_actual + k2 / 2)
            print(f"k3 = {k3:.6f}")

            print("\nCalculando k4:")
            print(f"k4 = h * f(x_actual + h, y_actual + k3)")
            print(f"k4 = {h} * f({x_actual:.6f} + {h}, {y_actual:.6f} + {k3:.6f})")
            print(f"k4 = {h} * f({x_actual + h:.6f}, {y_actual + k3:.6f})")
            k4 = h * f(x_actual + h, y_actual + k3)
            print(f"k4 = {k4:.6f}")

            print("\nCalculando y_siguiente:")
            print(f"y_siguiente = y_actual + (k1 + 2*k2 + 2*k3 + k4) / 6")
            print(f"y_siguiente = {y_actual:.6f} + ({k1:.6f} + 2*{k2:.6f} + 2*{k3:.6f} + {k4:.6f}) / 6")
            y_siguiente = y_actual + (k1 + 2*k2 + 2*k3 + k4) / 6
            print(f"y_siguiente = {y_siguiente:.6f}")

        else:
            raise ValueError("Orden debe ser 2, 3 o 4.")

        ea = 0 if ea_anterior is None else abs((y_siguiente - ea_anterior) / y_siguiente) * 100
        ea_anterior = y_siguiente

        # Guardamos los resultados antes de actualizar las variables
        tabla_resultados.append([
            x_actual, y_actual, k1, k2, k3, k4, y_siguiente, ea
        ])

        # Verificamos si el siguiente paso superaría xn
        if round(x_actual + h, 10) > round(xn, 10):
            break

        # Actualizamos las variables para el siguiente paso
        y_actual = y_siguiente
        x_actual += h

    print("\n" + "=" * 100)
    print("Tabla de resultados:")
    print("{:<8} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "xi", "yi", "k1", "k2", "k3", "k4", "yi+1", "Ea(%)"
    ))
    for fila in tabla_resultados:
        # Adjust slicing based on order to avoid printing k3/k4 if not calculated
        if orden == 2:
             print("{:<8.4f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(*fila[:2], fila[2], fila[3], 0.0, 0.0, fila[6], fila[7]))
        elif orden == 3:
             print("{:<8.4f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(*fila[:2], fila[2], fila[3], fila[4], 0.0, fila[6], fila[7]))
        elif orden == 4:
             print("{:<8.4f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(*fila))


    # El resultado final es el último yi calculado
    print("\n>>> Resultado final: y({:.4f}) ≈ {:.6f}".format(x_actual, y_actual))


# Ejemplo de uso:
runge_kutta("4*exp(0.8*x) - 0.5*y", x0=0, y0=2, h=0.5, xn=0.5, orden=4)
#sin(x),cos(x),tan(x),sec(x),csc(x),cot(x),sqrt(x),exp(x),log(x),log10(x),Abs(x),cosh(x),senh(x)