import math
import pandas as pd
import tkinter as tk
from tkinter import ttk

def f(m, g, c, v, t):
    return (g * m / c) * (1 - math.exp(- (c / m) * t)) - v

def mostrar_resultados(tabla, raiz):
    ventana = tk.Tk()
    ventana.title("Resultados - Método de Falsa Posición")
    
    frame = ttk.Frame(ventana, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    label = ttk.Label(frame, text=f"Raíz encontrada: {raiz:.6f}", font=("Arial", 12, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=5)
    
    tree = ttk.Treeview(frame, columns=("Iteración", "Xr", "Error (%)"), show='headings')
    tree.heading("Iteración", text="Iteración")
    tree.heading("Xr", text="Xr")
    tree.heading("Error (%)", text="Error (%)")
    
    for i in range(len(tabla)):
        tree.insert("", "end", values=tuple(tabla.iloc[i]))
    
    tree.grid(row=1, column=0)
    
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
    
    ventana.mainloop()

def falsa_posicion(g, c, v, t, xi, xu, tol=0.1, max_iter=100):
    xr_ant = None
    iteracion = 0
    datos = []
    
    while iteracion < max_iter:
        iteracion += 1
        xr = xu - (f(xu, g, c, v, t) * (xi - xu)) / (f(xi, g, c, v, t) - f(xu, g, c, v, t))
        
        error = abs((xr - xr_ant) / xr) * 100 if xr_ant is not None else None
        
        datos.append([iteracion, xr, f"{error:.6f}%" if error is not None else "N/A"])
        
        if error is not None and error < tol:
            break
        
        if f(xi, g, c, v, t) * f(xr, g, c, v, t) < 0:
            xu = xr
        else:
            xi = xr
        
        xr_ant = xr
    
    tabla_resultados = pd.DataFrame(datos, columns=["Iteración", "Xr", "Error (%)"])
    mostrar_resultados(tabla_resultados, xr)
    return xr

def main():
    g = input(f"Ingrese el valor de g (default 9.8): ")
    g = float(g) if g else 9.8
    
    c = input(f"Ingrese el valor de c (default 15): ")
    c = float(c) if c else 15
    
    v = input(f"Ingrese el valor de v (default 35): ")
    v = float(v) if v else 35
    
    t = input(f"Ingrese el valor de t (default 9): ")
    t = float(t) if t else 9
    
    xi = float(input("Ingrese el límite inferior: "))
    xu = float(input("Ingrese el límite superior: "))
    
    resultado = falsa_posicion(g, c, v, t, xi, xu)
    print(f"\nLa raíz encontrada para m es: {resultado:.6f}")

if __name__ == "__main__":
    main()
