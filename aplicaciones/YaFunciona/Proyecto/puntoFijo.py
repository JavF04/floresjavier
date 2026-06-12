import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import sympy as sp
import copy

class PuntoFijo:
    def __init__(self, variables, vector_inicial, tolerancia, iteraciones):
        self.variables = variables
        self.vector_inicial = vector_inicial
        self.tolerancia = tolerancia
        self.despejes = []
        self.iteraciones = iteraciones

    def _metodo_jacobi(self):
        aux_tolerancia = self.tolerancia + 1
        df_aux = pd.DataFrame(columns=self.variables)
        aux_dict = {}
        aux_vector = self.vector_inicial.copy()
        j = 1
        df_aux.loc[0] = list(self.vector_inicial.values())
        while aux_tolerancia >= self.tolerancia and len(df_aux) <= self.iteraciones:
            for i, var in enumerate(self.variables):
                aux_dict[var] = round(self.despejes[i].subs(aux_vector), 4)
            df_aux.loc[j] = list(aux_dict.values())
            aux_vector = aux_dict.copy()
            aux_dict.clear()
            j += 1
        return df_aux

    def _metodo_gauss_seidel(self):
        aux_tolerancia = self.tolerancia + 1
        df_aux = pd.DataFrame(columns=self.variables)
        aux_dict = {}
        aux_vector = self.vector_inicial.copy()
        j = 1
        df_aux.loc[0] = list(self.vector_inicial.values())
        while aux_tolerancia >= self.tolerancia and len(df_aux) <= self.iteraciones:
            for i, var in enumerate(self.variables):
                aux_dict[var] = round(self.despejes[i].subs(aux_vector), 4)
                aux_vector[var] = aux_dict[var]
            df_aux.loc[j] = list(aux_dict.values())
            aux_dict.clear()
            j += 1
        return df_aux

class PuntoFijoApp:
    def __init__(self, on_close_callback):
        self.root = tk.Tk()    
        self.on_close_callback = on_close_callback
        self.root.title("Método del Punto Fijo")
        
        self.var_entries = []
        self.vector_inicial_entries = []
        self.despeje_entries = []

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.result_frame = tk.Frame(self.root)

        self.init_ui()

    def init_ui(self):
        label_puntos = tk.Label(self.main_frame, text="Cantidad de variables:")
        label_puntos.grid(row=0, column=0)
        self.entry_puntos = tk.Entry(self.main_frame)
        self.entry_puntos.grid(row=0, column=1)
        btn_set_puntos = tk.Button(self.main_frame, text="Ingresar valores", command=self.set_puntos)
        btn_set_puntos.grid(row=0, column=2)

    def set_puntos(self):
        try:
            num_puntos = int(self.entry_puntos.get())
            if num_puntos <= 0:
                raise ValueError("La cantidad de variables debe ser mayor a cero.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        for widget in self.main_frame.winfo_children()[3:]:
            widget.destroy()

        for i in range(num_puntos):
            var_label = tk.Label(self.main_frame, text=f"Variable {i + 1}:")
            var_label.grid(row=i+1, column=0)
            var_entry = tk.Entry(self.main_frame)
            var_entry.grid(row=i+1, column=1)
            self.var_entries.append(var_entry)

            vi_label = tk.Label(self.main_frame, text=f"Valor inicial {i + 1}:")
            vi_label.grid(row=i+1, column=2)
            vi_entry = tk.Entry(self.main_frame)
            vi_entry.grid(row=i+1, column=3)
            self.vector_inicial_entries.append(vi_entry)

            despeje_label = tk.Label(self.main_frame, text=f"Despeje {i + 1}:")
            despeje_label.grid(row=i+1, column=4)
            despeje_entry = tk.Entry(self.main_frame)
            despeje_entry.grid(row=i+1, column=5)
            self.despeje_entries.append(despeje_entry)

        label_iteraciones = tk.Label(self.main_frame, text="Número de iteraciones:")
        label_iteraciones.grid(row=num_puntos+1, column=0)
        self.entry_iteraciones = tk.Entry(self.main_frame)
        self.entry_iteraciones.grid(row=num_puntos+1, column=1)

        label_tolerancia = tk.Label(self.main_frame, text="Tolerancia:")
        label_tolerancia.grid(row=num_puntos+1, column=2)
        self.entry_tolerancia = tk.Entry(self.main_frame)
        self.entry_tolerancia.grid(row=num_puntos+1, column=3)

        btn_mostrar_tabla = tk.Button(self.main_frame, text="Mostrar tabla", command=self.mostrar_tabla)
        btn_mostrar_tabla.grid(row=num_puntos+2, column=0, columnspan=6)

    def mostrar_tabla(self):
        try:
            variables = [sp.symbols(var_entry.get()) for var_entry in self.var_entries]
            vector_inicial = {str(var): float(vi_entry.get()) for var, vi_entry in zip(variables, self.vector_inicial_entries)}
            despejes = [sp.sympify(despeje_entry.get()) for despeje_entry in self.despeje_entries]
            iteraciones = int(self.entry_iteraciones.get())
            tolerancia = float(self.entry_tolerancia.get())
        except ValueError as e:
            messagebox.showerror("Error", "Entrada inválida. Asegúrese de ingresar valores correctos.")
            return

        pf = PuntoFijo(variables, vector_inicial, tolerancia, iteraciones)
        pf.despejes = despejes

        result = pf._metodo_jacobi()

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        tv = ttk.Treeview(self.result_frame)
        tv['columns'] = list(result.columns)
        tv['show'] = 'headings'
        for column in tv['columns']:
            tv.heading(column, text=column)

        for row in result.itertuples(index=False):
            tv.insert("", "end", values=row)

        tv.pack(fill="both", expand=True)

        btn_regresar = tk.Button(self.result_frame, text="Regresar", command=self.regresar)
        btn_regresar.pack()

        self.main_frame.pack_forget()
        self.result_frame.pack()

    def regresar(self):
        self.root.destroy()
        self.on_close_callback()


