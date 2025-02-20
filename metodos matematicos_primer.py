import math
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import re
from tabulate import tabulate

def extraer_x(funcion):
    """ 
    Extrae el valor de x en la función cos(x) o cos(kπ).
    Acepta `π`, `pi` o valores numéricos directos.
    """
    patron_pi = r'cos\(([-]?\d*\.?\d*)\s*\*?\s*(?:π|pi)\)'
    patron_numero = r'cos\(([-]?\d*\.?\d*)\)'

    funcion = funcion.lower().replace(" ", "")
    coincidencia_pi = re.search(patron_pi, funcion)
    coincidencia_num = re.search(patron_numero, funcion)

    if coincidencia_pi:
        return float(coincidencia_pi.group(1)) * math.pi  # Convertir a radianes
    elif coincidencia_num:
        return float(coincidencia_num.group(1))  # Ya está en radianes
    else:
        raise ValueError("Formato incorrecto. Ingrese en la forma cos(kπ), cos(kpi) o cos(x)")

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
        
        resultados.append((n + 1, valorAproximado, errorVerdadero, errorAproximado))
        
        if errorAproximado != "N/A" and errorAproximado < tolerancia:
            break

        valorAproximadoanterior = valorAproximado
        n += 1

    return resultados

def mostrar_resultados(tabla):
    ventana = tk.Toplevel()
    ventana.title("Resultados")
    ventana.geometry("600x400")
    
    texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20)
    texto.insert(tk.INSERT, tabla)
    texto.config(state=tk.DISABLED)
    texto.pack(expand=True, fill='both')

def calcular():
    try:
        funcion = simpledialog.askstring("Entrada", "Ingrese la función:")
        if funcion is None:
            return
        
        x = extraer_x(funcion)  
        resultados = cos_maclaurin(x)
        
        tabla = tabulate(resultados, headers=["Términos", "Resultado", "E_t (%)", "E_a (%)"], tablefmt="grid", floatfmt=".10f")
        print(tabla)
        mostrar_resultados(tabla)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Calculadora de Serie de Maclaurin")
root.geometry("300x100")  # Tamaño reducido para no estorbar
tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

root.mainloop()

calcular()
