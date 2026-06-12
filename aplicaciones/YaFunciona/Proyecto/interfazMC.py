import tkinter as tk
from tkinter import ttk

class Min_Cuad_metodo:
    def __init__(self, on_close_callback):
        self.root = tk.Tk()
        self.on_close_callback = on_close_callback

        self.root.title("Recta de Mínimos Cuadrados")
        self.root.geometry("500x500")

        self.puntos_label = ttk.Label(self.root, text="Ingrese el número de puntos:")
        self.puntos_label.pack()

        self.puntos_entry = ttk.Entry(self.root)
        self.puntos_entry.pack()

        self.confirmar_button = ttk.Button(self.root, text="Ingresar datos", command=self.crear_campos)
        self.confirmar_button.pack()

        self.campos_frame = ttk.Frame(self.root)
        self.campos_frame.pack()

        self.resultado_label = ttk.Label(self.root, text="")
        self.resultado_label.pack()

        self.error_label = ttk.Label(self.root, text="")
        self.error_label.pack()

        # Botón para regresar, inicialmente no visible
        self.regresar_button = ttk.Button(self.root, text="Regresar", command=self.regresar)
        self.regresar_button.pack()
        self.regresar_button.pack_forget()

        self.x_entries = []
        self.y_entries = []
        self.calcular_button = None

    def RectaMinSq(self, datos):
        X = sum([p[0] for p in datos])
        Y = sum([p[1] for p in datos])
        XX = sum([(p[0])**2 for p in datos])
        XY = sum([p[0]*p[1] for p in datos])
        m = len(datos)

        denominator = m * XX - X**2
        if denominator != 0:
            a0 = (Y * XX - X * XY) / denominator
            a1 = (m * XY - X * Y) / denominator
        else:
            raise ZeroDivisionError("No se puede dividir por cero. Verifique los datos ingresados.")

        def P(x):
            return a0 + a1 * x

        return P, a0, a1

    def ErrorSq(self, f, datos):
        E = sum([(p[1] - f(p[0]))**2 for p in datos])
        return E

    def crear_campos(self):
        try:
            n_puntos = int(self.puntos_entry.get())
        except ValueError:
            self.resultado_label.config(text="Ingrese un número válido de puntos.")
            return

        for widget in self.campos_frame.winfo_children():
            widget.destroy()

        self.x_entries = []
        self.y_entries = []

        for i in range(n_puntos):
            label_x = ttk.Label(self.campos_frame, text=f"Ingrese x_{i+1}:")
            label_x.grid(row=i, column=0)
            entry_x = ttk.Entry(self.campos_frame)
            entry_x.grid(row=i, column=1)
            self.x_entries.append(entry_x)

            label_y = ttk.Label(self.campos_frame, text=f"Ingrese y_{i+1}:")
            label_y.grid(row=i, column=2)
            entry_y = ttk.Entry(self.campos_frame)
            entry_y.grid(row=i, column=3)
            self.y_entries.append(entry_y)

        self.x_eval_label = ttk.Label(self.campos_frame, text="Ingrese el valor de x para evaluar la recta:")
        self.x_eval_label.grid(row=n_puntos, column=0)
        self.x_eval_entry = ttk.Entry(self.campos_frame)
        self.x_eval_entry.grid(row=n_puntos, column=1)

        if self.calcular_button is None:
            self.calcular_button = ttk.Button(self.root, text="Calcular", command=self.calcular)
            self.calcular_button.pack()

    def ingresar_datos(self):
        datos = []
        for entry_x, entry_y in zip(self.x_entries, self.y_entries):
            try:
                x = float(entry_x.get())
                y = float(entry_y.get())
                datos.append((x, y))
            except ValueError:
                pass
        return datos

    def calcular(self):
        datos = self.ingresar_datos()
        if datos:
            try:
                f, a0, a1 = self.RectaMinSq(datos)
                x = float(self.x_eval_entry.get())
            except ValueError:
                self.resultado_label.config(text="Ingrese un valor válido para x.")
                return

            m = a1
            b = a0

            if b < 0:
                self.resultado_label.config(text=f"Recta de ajuste: y = {m:.4f}x {b:.4f}\nEvaluar en x = {x}: {round(f(x), 6)}",font=("Times New Roman", 17))
            else:
                self.resultado_label.config(text=f"Recta de ajuste: y = {m:.4f}x + {b:.4f}\nEvaluar en x = {x}: {round(f(x), 6)}",font=("Times New Roman", 17))

            error = self.ErrorSq(f, datos)
            self.error_label.config(text=f"Error cuadrático: {round(error, 6)}",font=("Times New Roman", 17))
            
            # Mostrar el botón de regresar
            self.regresar_button.pack()
        else:
            self.resultado_label.config(text="No se ingresaron datos.")
            self.error_label.config(text="")

    def regresar(self):
        self.root.destroy()
        self.on_close_callback()

