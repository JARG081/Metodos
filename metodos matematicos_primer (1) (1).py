import math
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tabulate import tabulate

def cos_maclaurin(x, tolerancia=0.0000005):
    """Calcula la aproximación de cos(x) con la serie de Maclaurin y los errores."""
    valorAproximado = 1  
    valorAproximadoanterior = valorAproximado  
    errorAproximado = None
    n = 0  

    resultados = []
    while True:
        if n > 0:
            termino = (-1)**n * x**(2*n) / math.factorial(2*n)
            valorAproximado += termino  
        
        errorVerdadero = abs((math.cos(x) - valorAproximado) / math.cos(x)) * 100
        errorAproximado = abs((valorAproximado - valorAproximadoanterior) / valorAproximado) * 100 if n > 0 else "N/A"
        
        resultados.append((n + 1, round(valorAproximado, 8), errorVerdadero, errorAproximado))

        if errorAproximado != "N/A" and errorAproximado < tolerancia:
            break

        valorAproximadoanterior = valorAproximado
        n += 1

    return resultados

def mostrar_resultados(tabla):
    """Muestra los resultados en una ventana emergente."""
    ventana = tk.Toplevel(root)
    ventana.title("Resultados")
    ventana.geometry("600x400")
    
    texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20)
    texto.insert(tk.INSERT, tabla)
    texto.config(state=tk.DISABLED)
    texto.pack(expand=True, fill='both')

def calcular():
    """Obtiene el ángulo desde la interfaz, lo multiplica por π y lo usa en la serie de Maclaurin."""
    try:
        angulo = entrada_angulo.get().strip()
        if not angulo:
            messagebox.showwarning("Aviso", "Ingrese un ángulo válido.")
            return

        angulo = float(angulo)  # Convertir a número
        x = angulo * math.pi  # Multiplicar por π para obtener radianes

        resultados = cos_maclaurin(x)
        
        tabla = tabulate(resultados, headers=["Términos", "Resultado", "E_t (%)", "E_a (%)"], 
                         tablefmt="grid", floatfmt=(".0f", ".8f", ".8f", ".8f"))

        print(tabla)
        mostrar_resultados(tabla)

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para el ángulo.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Serie de Maclaurin")
root.geometry("300x150")

tk.Label(root, text="Ingrese el ángulo:").pack(pady=5)
entrada_angulo = tk.Entry(root, width=10)
entrada_angulo.pack(pady=5)

tk.Button(root, text="Calcular", command=calcular).pack(pady=10)

root.mainloop()
