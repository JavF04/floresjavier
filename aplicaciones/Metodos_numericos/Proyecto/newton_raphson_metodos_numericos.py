import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np

def newton_raphson(funciones, variables, valores_iniciales, tolerancia=1e-6, max_iter=100):
    def jacobiano(funciones, variables, valores):
        jacobiano = np.zeros((len(funciones), len(variables)))
        for i, funcion in enumerate(funciones):
            for j, variable in enumerate(variables):
                jacobiano[i, j] = eval(f"lambda {', '.join(variables)}: {sp.sympify(funcion).diff(variable)}")(*valores)
        return jacobiano

    def evaluar_funciones(funciones, variables, valores):
        return np.array([eval(f"lambda {', '.join(variables)}: {sp.sympify(funcion)}")(*valores) for funcion in funciones])

    valores = np.array(valores_iniciales)
    iteraciones = []
    for iteracion in range(max_iter):
        jacob = jacobiano(funciones, variables, valores)
        f = evaluar_funciones(funciones, variables, valores)
        delta = np.linalg.solve(jacob, -f)
        valores += delta
        iteraciones.append(valores.copy())
        if np.all(np.abs(delta) < tolerancia):
            break
    return valores, iteraciones

def mostrar_panel(on_close_callback):
    panel = tk.Tk()
    panel.title("Método Newton-Raphson")

    tk.Label(panel, text="Número de funciones:").grid(row=0, column=0)
    num_funciones_entry = tk.Entry(panel)
    num_funciones_entry.grid(row=0, column=1)

    tk.Label(panel, text="Número de variables:").grid(row=1, column=0)
    num_variables_entry = tk.Entry(panel)
    num_variables_entry.grid(row=1, column=1)

    def ingresar_valores():
        try:
            num_funciones = int(num_funciones_entry.get())
            num_variables = int(num_variables_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")
            return

        for widget in panel.winfo_children()[4:]:
            widget.destroy()

        tk.Label(panel, text="Funciones:").grid(row=2, column=0)
        funciones_entries = []
        for i in range(num_funciones):
            entry = tk.Entry(panel)
            entry.grid(row=3 + i, column=0, columnspan=2)
            funciones_entries.append(entry)

        tk.Label(panel, text="Variables:").grid(row=3 + num_funciones, column=0)
        variables_entries = []
        for i in range(num_variables):
            entry = tk.Entry(panel)
            entry.grid(row=4 + num_funciones + i, column=0, columnspan=2)
            variables_entries.append(entry)

        tk.Label(panel, text="Valores iniciales:").grid(row=4 + num_funciones + num_variables, column=0)
        valores_iniciales_entries = []
        for i in range(num_variables):
            entry = tk.Entry(panel)
            entry.grid(row=5 + num_funciones + num_variables + i, column=0, columnspan=2)
            valores_iniciales_entries.append(entry)

        def mostrar_tabla():
            funciones = [sp.sympify(entry.get()) for entry in funciones_entries]
            variables = [entry.get() for entry in variables_entries]
            try:
                valores_iniciales = [float(entry.get()) for entry in valores_iniciales_entries]
            except ValueError:
                messagebox.showerror("Error", "Ingrese valores iniciales válidos.")
                return

            resultado, iteraciones = newton_raphson(funciones, variables, valores_iniciales)
            
            tk.Label(panel, text="Resultados:").grid(row=5 + num_funciones + num_variables * 2, column=0)
            resultado_text = tk.Text(panel, height=10, width=50)
            resultado_text.grid(row=6 + num_funciones + num_variables * 2, column=0, columnspan=2)
            resultado_text.insert(tk.END, "Iteraciones:\n")
            for iteracion in iteraciones:
                resultado_text.insert(tk.END, f"{iteracion}\n")
            resultado_text.insert(tk.END, f"\nResultado final: {resultado}")

            def regresar():
                panel.destroy()
                on_close_callback()

            tk.Button(panel, text="Regresar", command=regresar).grid(row=7 + num_funciones + num_variables * 2, column=0, columnspan=2)

        tk.Button(panel, text="Mostrar tabla", command=mostrar_tabla).grid(row=5 + num_funciones + num_variables * 2, column=0, columnspan=2)

    tk.Button(panel, text="Ingresar valores", command=ingresar_valores).grid(row=2, column=1)

    
