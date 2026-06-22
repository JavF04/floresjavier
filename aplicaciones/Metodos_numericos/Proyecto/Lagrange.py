import tkinter as tk
from tkinter import messagebox
import sympy as sp

class LagrangeMetodo:
    def __init__(self, on_close_callback):
        self.root = tk.Tk()
        self.on_close_callback = on_close_callback
        self.root.title("Interpolación de Lagrange")

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        self.frame_resultado = tk.Frame(self.root)
        self.frame_resultado.pack(pady=10)

        self.frame_tabla = tk.Frame(self.root)
        self.frame_tabla.pack(pady=10)

        self.label_num_puntos = tk.Label(self.frame_entrada, text="Introduce el número de puntos:")
        self.label_num_puntos.grid(row=0, column=0)
        self.entry_num_puntos = tk.Entry(self.frame_entrada)
        self.entry_num_puntos.grid(row=0, column=1)

        self.button_generar = tk.Button(self.frame_entrada, text="Generar campos de entrada", command=self.generar_campos)
        self.button_generar.grid(row=0, column=2)

        self.resultado_text = None
        
        self.btn_regresar = tk.Button(self.frame_resultado, text="Regresar", command=self.regresar)
        self.btn_regresar.grid(row=1, column=0, columnspan=3)

    def LagrangePol(self, datos):
        x = sp.symbols('x')
        n = len(datos)
        L = [1] * n
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    L[i] *= (x - datos[j][0]) / (datos[i][0] - datos[j][0])
        
        P = sum(L[i] * datos[i][1] for i in range(n))
        P_simplified = sp.simplify(P)
        return P_simplified, P_simplified.evalf()

    def calcular_polynomial(self):
        try:
            datos = []
            n = int(self.entry_num_puntos.get())
            for i in range(n):
                x = float(self.entries_x[i].get())
                y = float(self.entries_y[i].get())
                datos.append((x, y))
            
            x_eval = float(self.entry_x_eval.get())
            
            polinomio, result = self.LagrangePol(datos)
            result_eval = polinomio.subs('x', x_eval)
            
            if self.resultado_text is not None:
                self.resultado_text.destroy()

            self.resultado_text = tk.Text(self.frame_resultado, height=10, width=50)
            self.resultado_text.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
            self.resultado_text.insert(tk.END, f"Polinomio de Lagrange (simplificado):\n{sp.pretty(polinomio)}\n")
            self.resultado_text.insert(tk.END, f"\nEvaluación en x = {x_eval}: {result_eval:.12f}")
            
            self.mostrar_tabla(datos, x_eval, result_eval)
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def mostrar_tabla(self, datos, x_eval, result):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        
        headings = ["Punto", "x", "y"]
        for i, heading in enumerate(headings):
            label = tk.Label(self.frame_tabla, text=heading, font=('Arial', 12, 'bold'))
            label.grid(row=0, column=i)
        
        for i, (x, y) in enumerate(datos):
            label_punto = tk.Label(self.frame_tabla, text=f"Punto {i+1}", font=('Arial', 12))
            label_punto.grid(row=i+1, column=0)
            label_x = tk.Label(self.frame_tabla, text=x, font=('Arial', 12))
            label_x.grid(row=i+1, column=1)
            label_y = tk.Label(self.frame_tabla, text=y, font=('Arial', 12))
            label_y.grid(row=i+1, column=2)
        
        label_result = tk.Label(self.frame_tabla, text=f"Evaluación en x = {x_eval}: {result:.12f}", font=('Arial', 12, 'bold'))
        label_result.grid(row=len(datos)+1, columnspan=3)

    def generar_campos(self):
        self.entries_x = []
        self.entries_y = []
        try:
            n = int(self.entry_num_puntos.get())
            for widget in self.frame_entrada.winfo_children()[2:]:
                widget.destroy()
            
            for i in range(n):
                label_x = tk.Label(self.frame_entrada, text=f"Introduce x{i}:")
                label_x.grid(row=i+1, column=0)
                entry_x = tk.Entry(self.frame_entrada)
                entry_x.grid(row=i+1, column=1)
                self.entries_x.append(entry_x)
                
                label_y = tk.Label(self.frame_entrada, text=f"Introduce y{i}:")
                label_y.grid(row=i+1, column=2)
                entry_y = tk.Entry(self.frame_entrada)
                entry_y.grid(row=i+1, column=3)
                self.entries_y.append(entry_y)
            
            label_x_eval = tk.Label(self.frame_entrada, text="Introduce el valor de x para evaluar el polinomio:")
            label_x_eval.grid(row=n+1, column=0)
            self.entry_x_eval = tk.Entry(self.frame_entrada)
            self.entry_x_eval.grid(row=n+1, column=1)
            
            button_calcular = tk.Button(self.frame_entrada, text="Calcular", command=self.calcular_polynomial)
            button_calcular.grid(row=n+2, columnspan=4)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero válido para el número de puntos.")

    def regresar(self):
        self.root.destroy()
        self.on_close_callback()


