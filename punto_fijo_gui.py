import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def punto_fijo_method(func_str, x0, tol, max_iter):
    x = sp.Symbol('x')
    try:
        # Definimos un entorno seguro con funciones comunes
        local_dict = {
            "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
            "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,
            "pi": sp.pi, "e": sp.E
        }
        g_expr = sp.sympify(func_str, locals=local_dict)
        g = sp.lambdify(x, g_expr, modules=["numpy"])
    except Exception as e:
        messagebox.showerror("Error", f"Función inválida: {e}")
        return

    data = []
    for i in range(1, max_iter + 1):
        try:
            x1 = g(x0)
        except Exception as e:
            messagebox.showerror("Error", f"Error al evaluar la función en x={x0}: {e}")
            return
        error_norm = abs(x1 - x0)
        error_rel = abs(error_norm / x1) if x1 != 0 else 0
        data.append((i, x0, x1, error_norm, error_rel))
        if error_norm < tol:
            break
        x0 = x1

    show_table(data)
    plot_graph(data)

def show_table(data):
    for row in tree.get_children():
        tree.delete(row)
    for d in data:
        tree.insert("", "end", values=(d[0], f"{d[1]:.6f}", f"{d[2]:.6f}", f"{d[3]:.6f}", f"{d[4]:.6f}"))

    if data:
        label_result.config(text=f"Iteraciones: {data[-1][0]}   Valor final: {data[-1][2]:.6f}   Error: {data[-1][3]:.6f}")

def plot_graph(data):
    iterations = [d[0] for d in data]
    values = [d[2] for d in data]

    plt.figure()
    plt.plot(iterations, values, marker='o', color='purple')
    plt.title("Convergencia del Método de Punto Fijo")
    plt.xlabel("Iteraciones")
    plt.ylabel("Aproximación")
    plt.grid(True)
    plt.show()

def calcular():
    try:
        func_str = entry_func.get()
        x0 = float(entry_x0.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
        punto_fijo_method(func_str, x0, tol, max_iter)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Método de Punto Fijo")
root.geometry("800x600")
root.configure(bg="#ecf0f1")

# Sección de entrada
frame_input = tk.Frame(root, bg="#ecf0f1")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Función g(x):", bg="#ecf0f1").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_func = tk.Entry(frame_input, width=50)
entry_func.insert(0, "x - ((exp(-x/200))*cos(sqrt(2000-((x/10)**2))*0.05) - 0.01)")
entry_func.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Valor inicial x0:", bg="#ecf0f1").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_x0 = tk.Entry(frame_input, width=50)
entry_x0.insert(0, "1")
entry_x0.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tolerancia:", bg="#ecf0f1").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_tol = tk.Entry(frame_input, width=50)
entry_tol.insert(0, "0.01")
entry_tol.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Máx Iteraciones:", bg="#ecf0f1").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_iter = tk.Entry(frame_input, width=50)
entry_iter.insert(0, "3000")
entry_iter.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Calcular", command=calcular, bg="#2980b9", fg="white", width=20).grid(row=4, column=0, columnspan=2, pady=10)

# Sección de tabla
frame_table = tk.Frame(root, bg="#ecf0f1")
frame_table.pack(pady=10)

columns = ("Iteración", "x0", "x1", "Error Norm.", "Error Rel.")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)
tree.pack()
label_result = tk.Label(frame_table, text="", bg="#ecf0f1", font=("Arial", 12, "bold"))
label_result.pack(pady=10)


root.mainloop()