import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import matplotlib.pyplot as plt

def falsa_posicion_method(func_str, a, b, tol, max_iter):
    x = sp.Symbol('x')
    try:
        f = sp.lambdify(x, sp.sympify(func_str, locals={"exp": sp.exp, "cos": sp.cos, "sin": sp.sin, "tan": sp.tan, "sqrt": sp.sqrt}), modules=["numpy"])
    except Exception as e:
        messagebox.showerror("Error", f"Función inválida: {e}")
        return

    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        messagebox.showerror("Error", "f(a) y f(b) deben tener signos opuestos.")
        return

    data = []
    for i in range(1, max_iter + 1):
        x0 = b - (fb * (a - b)) / (fa - fb)
        fx0 = f(x0)
        error_norm = abs(b - a)
        error_rel = abs((b - a) / x0) if x0 != 0 else 0
        data.append((i, a, b, x0, fx0, error_norm, error_rel))

        if fx0 == 0 or error_norm < tol:
            break

        if fa * fx0 < 0:
            b = x0
            fb = fx0
        else:
            a = x0
            fa = fx0

    show_table(data)
    plot_graph(data)

def show_table(data):
    for row in tree.get_children():
        tree.delete(row)
    for d in data:
        tree.insert("", "end", values=(d[0], f"{d[1]:.6f}", f"{d[2]:.6f}", f"{d[3]:.6f}", f"{d[4]:.6f}", f"{d[5]:.6f}", f"{d[6]:.6f}"))
    if data:
        label_result.config(text=f"Iteraciones: {data[-1][0]}   Valor final: {data[-1][2]:.6f}  Error: {data[-1][3]:.6f}")
def plot_graph(data):
    iterations = [d[0] for d in data]
    values = [d[3] for d in data]

    plt.figure()
    plt.plot(iterations, values, marker='o', color='red')
    plt.title("Convergencia del Método de Falsa Posición")
    plt.xlabel("Iteraciones")
    plt.ylabel("Aproximación de la raíz")
    plt.grid(True)
    plt.show()

def calcular():
    try:
        func_str = entry_func.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
        falsa_posicion_method(func_str, a, b, tol, max_iter)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Método de Falsa Posición")
root.geometry("750x600")
root.configure(bg="#ecf0f1")

# Sección de entrada
frame_input = tk.Frame(root, bg="#ecf0f1")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Función f(x):", bg="#ecf0f1").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_func = tk.Entry(frame_input, width=50)
entry_func.insert(0, "x**3 + 4*x**2 - 10")
entry_func.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Límite inferior a:", bg="#ecf0f1").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_a = tk.Entry(frame_input, width=50)
entry_a.insert(0, "1")
entry_a.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Límite superior b:", bg="#ecf0f1").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_b = tk.Entry(frame_input, width=50)
entry_b.insert(0, "2")
entry_b.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tolerancia:", bg="#ecf0f1").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_tol = tk.Entry(frame_input, width=50)
entry_tol.insert(0, "0.01")
entry_tol.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Máx Iteraciones:", bg="#ecf0f1").grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_iter = tk.Entry(frame_input, width=50)
entry_iter.insert(0, "100")
entry_iter.grid(row=4, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Calcular", command=calcular, bg="#c0392b", fg="white", width=20).grid(row=5, column=0, columnspan=2, pady=10)

# Sección de tabla
frame_table = tk.Frame(root, bg="#ecf0f1")
frame_table.pack(pady=10)

columns = ("Iteración", "a", "b", "x0", "f(x0)", "Error Norm.", "Error Rel.")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)
tree.pack()
label_result = tk.Label(frame_table, text="", bg="#ecf0f1", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()