import tkinter as tk
from tkinter import messagebox
import pandas as pd
import sympy as sp

class DiferenciasDivididasGUI:
    def __init__(self, on_close_callback):
        self.root = tk.Tk()    
        self.on_close_callback = on_close_callback
        self.root.title("Interpolación por diferencias divididas")

        self.tabular = {'x': [], 'f(x)': []}
        self.ecuacion = ""

        self.label_puntos = tk.Label(self.root, text="Ingrese la cantidad de puntos:")
        self.label_puntos.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry_puntos = tk.Entry(self.root)
        self.entry_puntos.grid(row=0, column=1, padx=5, pady=5)

        self.btn_ingresar_puntos = tk.Button(self.root, text="Ingresar puntos", command=self.ingresar_puntos)
        self.btn_ingresar_puntos.grid(row=0, column=2, padx=5, pady=5)

    def ingresar_puntos(self):
        try:
            puntos = int(self.entry_puntos.get())
            self.clear_entries()
            self.x_entries = []
            self.fx_entries = []
            for i in range(puntos):
                label_x = tk.Label(self.root, text=f"x_{i}:")
                label_x.grid(row=3+i, column=0, padx=5, pady=2)
                entry_x = tk.Entry(self.root)
                entry_x.grid(row=3+i, column=1, padx=5, pady=2)
                self.x_entries.append(entry_x)

                label_fx = tk.Label(self.root, text=f"f(x_{i}):")
                label_fx.grid(row=3+i, column=2, padx=5, pady=2)
                entry_fx = tk.Entry(self.root)
                entry_fx.grid(row=3+i, column=3, padx=5, pady=2)
                self.fx_entries.append(entry_fx)

            self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.mostrar_resultado)
            self.btn_calcular.grid(row=3+puntos, column=0, columnspan=4, padx=5, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def clear_entries(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

    def mostrar_resultado(self):
        try:
            self.tabular['x'] = [float(entry.get()) for entry in self.x_entries]
            self.tabular['f(x)'] = [float(entry.get()) for entry in self.fx_entries]

            obj = DiferenciasDivididas(self.tabular)
            resultado = obj._metodo()

            resultado_text = tk.Text(self.root, height=10, width=50)
            resultado_text.grid(row=3+len(self.x_entries), column=0, columnspan=4, padx=5, pady=5)
            resultado_text.insert(tk.END, resultado)

            regresar_button = tk.Button(self.root, text="Regresar", command=self.regresar)
            regresar_button.grid(row=4+len(self.x_entries), column=0, columnspan=4, padx=5, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def regresar(self):
        self.root.destroy()
        self.on_close_callback()

class DiferenciasDivididas:
    def __init__(self, tabulacion: dict):
        self.__tabulacion = tabulacion

    def _metodo(self):
        x = self.__tabulacion['x']
        fx = self.__tabulacion['f(x)']
        n = len(x)
        coef = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            coef[i][0] = fx[i]

        for j in range(1, n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

        x_sym = sp.symbols('x')
        polinomio = coef[0][0]
        for j in range(1, n):
            termino = coef[0][j]
            for i in range(j):
                termino *= (x_sym - x[i])
            polinomio += termino

        polinomio = sp.simplify(polinomio)
        resultado = "El polinomio interpolador es:\n" + str(polinomio)
        resultado += "\n\nLos coeficientes de diferencias divididas son:\n"
        for j in range(n):
            resultado += f"c{j}: {coef[0][j]}\n"
        
        return resultado
