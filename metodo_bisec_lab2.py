import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk

def mostrar_resultados(resultados):
    ventana = tk.Tk()
    ventana.title("Resultados del Método de Bisección")
    
    cols = ("Iteración", "Xl", "Xu", "Xr", "f(Xr)", "Error %")
    tree = ttk.Treeview(ventana, columns=cols, show='headings')
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    
    for res in resultados:
        tree.insert("", "end", values=res)
    
    tree.pack(expand=True, fill='both')
    ventana.mainloop()

def biseccion(func, Xl, Xu, tol=1e-6, max_iter=100, max_tol=0.5):
    fXl, fXu = func(Xl), func(Xu)
    
    if fXl == 0:
        print(f"La raíz exacta es {Xl}")
        return Xl
    if fXu == 0:
        print(f"La raíz exacta es {Xu}")
        return Xu
    
    iteracion = 0
    xr_anterior = Xl
    error_porcentual = float("inf")
    resultados = []
    
    while error_porcentual > tol and error_porcentual > max_tol and iteracion < max_iter:
        iteracion += 1
        Xr = (Xl + Xu) / 2
        fXr = func(Xr)
        
        if iteracion > 1:
            error_porcentual = abs((Xr - xr_anterior) / Xr) * 100
        
        resultados.append((iteracion, round(Xl, 4), round(Xu, 4), round(Xr, 4), round(fXr, 4), round(error_porcentual, 4)))
        
        if abs(fXr) < tol:
            mostrar_resultados(resultados)
            return Xr
        
        if fXl * fXr < 0:
            Xu = Xr
            fXu = fXr
        else:
            Xl = Xr
            fXl = fXr
        
        xr_anterior = Xr
    
    mostrar_resultados(resultados)
    return Xr

def pedir_entrada():
    g, m, t, v = 9.81, 68.1, 10, 40
    print("Valores base (presiona Enter para dejar valores predeterminados):")
    g = float(input(f"Gravedad (g) = {g}: ") or g)
    m = float(input(f"Masa (m) = {m}: ") or m)
    t = float(input(f"Tiempo (t) = {t}: ") or t)
    v = float(input(f"Velocidad (v) = {v}: ") or v)
    
    Xl = float(input("Ingresa Xl (límite inferior): "))
    Xu = float(input("Ingresa Xu (límite superior): "))
    
    c = sp.symbols('c')
    funcion = sp.lambdify(c, ((g * m) / c) * (1 - sp.exp(- (c / m) * t)) - v, "numpy")
    
    return funcion, Xl, Xu

if __name__ == "__main__":
    funcion, Xl, Xu = pedir_entrada()
    raiz = biseccion(funcion, Xl, Xu)
    print(f"\nRaíz aproximada: {raiz:.6f}")
