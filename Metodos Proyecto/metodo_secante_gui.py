import tkinter as tk
import math
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import sin, cos, exp, log, tan, pi, e

class MetodoSecanteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Método de la Secante")
        self.root.geometry("1000x700")
        
        # Variables para almacenar los datos de entrada
        self.funcion_var = tk.StringVar(value="(pi)*(x**2)*((9-x)/3)-30")
        self.x0_var = tk.StringVar(value="0")
        self.x1_var = tk.StringVar(value="1")
        self.tol_var = tk.StringVar(value="0.1")
        self.max_iter_var = tk.StringVar(value="100")
        
        # Crear widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Frame para los datos de entrada
        input_frame = ttk.LabelFrame(self.root, text="Parámetros de Entrada", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Función
        ttk.Label(input_frame, text="Función f(x):").grid(row=0, column=0, sticky=tk.W)
        funcion_entry = ttk.Entry(input_frame, textvariable=self.funcion_var, width=40)
        funcion_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(input_frame, text="Ej: x*exp(-x) - cos(x)").grid(row=0, column=2, sticky=tk.W)
        
        # Valores iniciales
        ttk.Label(input_frame, text="x₋₁:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.x0_var, width=15).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(input_frame, text="x₀:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.x1_var, width=15).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Tolerancia y máximo de iteraciones
        ttk.Label(input_frame, text="Tolerancia (%):").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.tol_var, width=15).grid(row=3, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(input_frame, text="Máx. iteraciones:").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.max_iter_var, width=15).grid(row=4, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Botón para ejecutar
        ttk.Button(input_frame, text="Calcular", command=self.ejecutar_secante).grid(row=5, column=0, columnspan=3, pady=10)
        
        # Frame para resultados
        result_frame = ttk.LabelFrame(self.root, text="Resultados", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tabla de iteraciones
        self.tree = ttk.Treeview(result_frame, columns=("Iter", "xᵢ", "f(xᵢ)", "Error Normalizado %", "Error Relativo %"), show="headings")
        self.tree.heading("Iter", text="Iteración")
        self.tree.heading("xᵢ", text="xᵢ")
        self.tree.heading("f(xᵢ)", text="f(xᵢ)")
        self.tree.heading("Error Normalizado %", text="Error Normalizado %")
        self.tree.heading("Error Relativo %", text="Error Relativo %")
        self.tree.column("Iter", width=70, anchor=tk.CENTER)
        self.tree.column("xᵢ", width=150, anchor=tk.CENTER)
        self.tree.column("f(xᵢ)", width=150, anchor=tk.CENTER)
        self.tree.column("Error Normalizado %", width=100, anchor=tk.CENTER)
        self.tree.column("Error Relativo %", width=100, anchor=tk.CENTER)
        
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Frame para gráficos
        graph_frame = ttk.LabelFrame(self.root, text="Gráficos", padding=10)
        graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear figura para los gráficos
        self.fig, (self.ax1) = plt.subplots(1, figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def ejecutar_secante(self):
        try:
            # Obtener valores de entrada
            funcion_str = self.funcion_var.get()
            x0 = float(self.x0_var.get())
            x1 = float(self.x1_var.get())
            tol = float(self.tol_var.get())
            max_iter = int(self.max_iter_var.get())
            valorR = 2.02690572831  # Valor de referencia para error relativo

            # Definir la función
            f = lambda x: eval(funcion_str, {'__builtins__': None}, 
                         {'x': x, 'sin': sin, 'cos': cos, 'tan': tan,
                          'exp': exp, 'pi': math.pi})

            # Limpiar tabla y gráficos anteriores
            for item in self.tree.get_children():
                self.tree.delete(item)
                self.ax1.clear()

            # Preparar listas para graficar
            iteraciones = []
            valores_xi = []

            # Variables para mostrar correctamente errores de la iteración anterior
            prev_x = None
            prev_fx = None
            prev_error_porcentual = None
            prev_error_relativo = None

            for i in range(max_iter):
                f_x0 = f(x0)
                f_x1 = f(x1)

                if f_x1 - f_x0 == 0:
                    messagebox.showerror("Error", "División por cero en el método de la secante")
                    return

                x2 = x1 - ((f_x1 * (x0 - x1)) / (f_x0 - f_x1))
                fx2 = f(x2)

                error_porcentual = abs((x2 - x1) / x2) * 100 if x2 != 0 else float('inf')
                error_relativo = abs((x2 - valorR) / x2) * 100 if x2 != 0 else float('inf')

                # Mostrar resultados anteriores con errores actuales
                if prev_x is not None:
                    self.tree.insert("", tk.END, values=(i, f"{prev_x:.8f}", f"{prev_fx:.8f}",
                                         f"{prev_error_porcentual:.6f}%", f"{prev_error_relativo:.6f}%"))
                else:
                    # Primera iteración, errores no aplican
                    self.tree.insert("", tk.END, values=(i, f"{x0:.8f}", f"{f_x0:.8f}", "No aplica", "No aplica"))

                # Guardar valores actuales como "previos" para la siguiente fila
                prev_x = x1
                prev_fx = fx2
                prev_error_porcentual = error_porcentual
                prev_error_relativo = error_relativo

                # Guardar para graficar
                iteraciones.append(i+1)
                valores_xi.append(x1)

                # Verificar tolerancia
                if error_porcentual < tol:
                    # Mostrar última fila pendiente
                    self.tree.insert("", tk.END, values=(i+1, f"{x1:.8f}", f"{fx2:.8f}",
                                                     f"{error_porcentual:.6f}%", f"{error_relativo:.6f}%"))
                    messagebox.showinfo("Convergencia", 
                                   f"Convergencia alcanzada en {i+1} iteraciones.\n"
                                   f"Raíz aproximada: {x2:.8f}\n"
                                   f"Error final: {error_porcentual:.6f}%")
                    break

                # Actualizar para la próxima iteración
                x0, x1 = x1, x2

            # Graficar evolución de xᵢ
            self.ax1.plot(iteraciones, valores_xi, 'bo-')
            self.ax1.set_title('Evolución de xᵢ')
            self.ax1.set_xlabel('Iteración')
            self.ax1.set_ylabel('Valor de xᵢ')
            self.ax1.grid(True)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar los datos: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MetodoSecanteApp(root)
    root.mainloop()