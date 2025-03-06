import math
import tkinter as tk
from tkinter import messagebox, scrolledtext

def falsa_posicion(func, a, b, tol=0.1, max_iter=100):
    iteraciones = []
    
    if func(a) * func(b) >= 0:
        messagebox.showerror("Error", "La función debe tener signos opuestos en a y b.")
        return None, iteraciones

    c_anterior = None  # Almacena el valor anterior de c

    for i in range(max_iter):
        c = b -(( func(b)*(a-b)) / (func(a) - func(b)))

        if c_anterior is None:
            error = 0  # Primera iteración, error es 0
        else:
            error = abs((c - c_anterior) / c) * 100  # Cálculo correcto del error

        iteraciones.append((i + 1, c, error))
        if abs(func(c)) < 1e-6:  # Un umbral pequeño para considerar la raíz encontrada
            break

        if error < tol and i > 0:  # Se detiene si el error es menor a la tolerancia después de la primera iteración
            break

        if func(c) * func(a) < 0:
            b = c
        elif func(c) * func(b) < 0:
            a = c
        else:
            break  # Detener si no hay cambio

        c_anterior = c  # Se actualiza correctamente el valor de c para la siguiente iteración

    return c, iteraciones

def ecuacion(g, c, v, t):
    return lambda m: (g * m / c) * (1 - math.exp(- (c / m) * t)) - v

def mostrar_resultados(iteraciones):
    ventana = tk.Toplevel()
    ventana.title("Resultados del Método de Falsa Posición")
    ventana.geometry("500x400")

    text_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=60, height=20)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    resultado = "Iteración | Xr        | Error (%)\n"
    resultado += "-" * 40 + "\n"
    resultado += "\n".join(f"{it[0]:<10} | {it[1]:.6f} | {it[2]:.6f}%" for it in iteraciones)
    
    text_area.insert(tk.END, resultado)
    text_area.config(state=tk.DISABLED)

def ejecutar_falsa_posicion():
    try:
        g = float(entrada_g.get() or 9.8)
        c = float(entrada_c.get() or 15)
        v = float(entrada_v.get() or 35)
        t = float(entrada_t.get() or 9)
        m_inferior = float(entrada_m_inf.get())
        m_superior = float(entrada_m_sup.get())

        func = ecuacion(g, c, v, t)
        raiz, iteraciones = falsa_posicion(func, m_inferior, m_superior, tol=0.1)

        if raiz is not None:
            mostrar_resultados(iteraciones)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Interfaz gráfica principal
root = tk.Tk()
root.title("Método de Falsa Posición")
root.geometry("400x350")

tk.Label(root, text="g (default 9.8):").pack()
entrada_g = tk.Entry(root)
entrada_g.pack()

tk.Label(root, text="c (default 15):").pack()
entrada_c = tk.Entry(root)
entrada_c.pack()

tk.Label(root, text="v (default 35):").pack()
entrada_v = tk.Entry(root)
entrada_v.pack()

tk.Label(root, text="t (default 9):").pack()
entrada_t = tk.Entry(root)
entrada_t.pack()

tk.Label(root, text="Límite inferior para m:").pack()
entrada_m_inf = tk.Entry(root)
entrada_m_inf.pack()

tk.Label(root, text="Límite superior para m:").pack()
entrada_m_sup = tk.Entry(root)
entrada_m_sup.pack()

boton_calcular = tk.Button(root, text="Calcular Raíz", command=ejecutar_falsa_posicion)
boton_calcular.pack(pady=10)

root.mainloop()  # Mantiene la interfaz gráfica activa
