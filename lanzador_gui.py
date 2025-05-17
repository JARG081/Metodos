import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys


def cargar_scripts():
    """Carga automáticamente los scripts _gui.py en el directorio"""
    scripts = []
    try:
        # Lista todos los archivos .py que contengan 'gui' en el nombre (sin distinguir mayúsculas)
        archivos = [f for f in os.listdir() 
                   if f.lower().endswith('.py') 
                   and 'gui' in f.lower()
                   and f != os.path.basename(__file__)]
        
        # Si no encuentra con 'gui', busca alternativas
        if not archivos:
            archivos = [f for f in os.listdir() 
                       if f.lower().endswith('.py')
                       and f != os.path.basename(__file__)
                       and ('metodo' in f.lower() or 'newton' in f.lower() or 'bisection' in f.lower())]
        
        return archivos
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron listar archivos: {e}")
        return []

# Cargar scripts
script_files = cargar_scripts()

# Si no encuentra nada, usa lista manual
if not script_files:
    script_files = [
        'biseccion_gui.py',
        'falsa_posicion_gui.py',
        'punto_fijo_gui.py',
        'newton_raphson_gui.py',
        'metodo_secante_gui.py'
    ]
    messagebox.showinfo("Información", "Usando lista manual de scripts")

# Resto del código igual...
proceso_activo = None

def ejecutar_script(nombre_script):
    global proceso_activo
    if proceso_activo and proceso_activo.poll() is None:
        messagebox.showwarning("Advertencia", "Ya hay un script ejecutándose. Ciérralo antes de abrir otro.")
        return

    try:
        proceso_activo = subprocess.Popen([sys.executable, nombre_script])
        proceso_activo.wait()  # Espera a que el script termine
        if proceso_activo.returncode != 0:
            messagebox.showerror("Error", f"El script {nombre_script} terminó con errores.")
        else:
            messagebox.showinfo("Éxito", f"{nombre_script} se ejecutó correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar {nombre_script}:\n{e}")

# Crear la interfaz
root = tk.Tk()
root.title("Lanzador de Métodos Numéricos")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Seleccione un método", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

frame_botones = tk.Frame(root, bg="#f0f0f0")
frame_botones.pack()

# Verificar si hay scripts para mostrar
if not script_files:
    tk.Label(frame_botones, text="No se encontraron scripts", fg="red").pack()
else:
    for i, script in enumerate(script_files):
        nombre_boton = os.path.splitext(script)[0].replace("_", " ").title()
        boton = tk.Button(
            frame_botones,
            text=nombre_boton,
            width=20,
            height=2,
            bg="#3498db",
            fg="white",
            command=lambda s=script: ejecutar_script(s)
        )
        boton.grid(row=i // 2, column=i % 2, padx=10, pady=5)

root.mainloop()