import pandas as pd
import sympy as sp
import tkinter as tk

class MetodoNewton(tk.Tk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Método de Newton")
        self.on_close_callback = on_close_callback

        self.label_puntos = tk.Label(self, text="Cantidad de puntos:")
        self.label_puntos.grid(row=0, column=0)
        self.puntos_entry = tk.Entry(self)
        self.puntos_entry.grid(row=0, column=1)

        self.ingresar_valores_button = tk.Button(self, text="Ingresar valores", command=self.ingresar_valores)
        self.ingresar_valores_button.grid(row=0, column=2)

    def ingresar_valores(self):
        try:
            self.puntos = int(self.puntos_entry.get())
            self.entries = []

            for i in range(self.puntos):
                label_x = tk.Label(self, text=f"x_{i}:")
                label_x.grid(row=i+1, column=0)
                entry_x = tk.Entry(self)
                entry_x.grid(row=i+1, column=1)
                self.entries.append(entry_x)

                label_fx = tk.Label(self, text=f"f(x_{i}):")
                label_fx.grid(row=i+1, column=2)
                entry_fx = tk.Entry(self)
                entry_fx.grid(row=i+1, column=3)
                self.entries.append(entry_fx)

            self.mostrar_tabla_button = tk.Button(self, text="Mostrar tabla", command=self.mostrar_tabla)
            self.mostrar_tabla_button.grid(row=self.puntos+1, columnspan=4)
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor, introduce un número entero válido para la cantidad de puntos.")

    def mostrar_tabla(self):
        try:
            tabulacion = {'x_i': [], 'f[x_i]': []}
            for i in range(self.puntos):
                tabulacion['x_i'].append(float(self.entries[i*2].get()))
                tabulacion['f[x_i]'].append(float(self.entries[i*2+1].get()))

            obj = MetodoNewtonBackend(tabulacion)
            tabla_resultado = obj.crear_tabla()
            polinomio_adelante = obj.crear_polinomio_adelante()
            polinomio_atras = obj.crear_polinomio_atras()

            self.resultado_label = tk.Label(self, text="Resultados:")
            self.resultado_label.grid(row=self.puntos+2, columnspan=4)

            self.resultado_text = tk.Text(self, height=20, width=85)
            self.resultado_text.insert(tk.END, f"Tabla de diferencias:\n{tabla_resultado}\n\n")
            self.resultado_text.insert(tk.END, f"Polinomio de Newton hacia adelante:\n{polinomio_adelante}\n\n")
            self.resultado_text.insert(tk.END, f"Polinomio de Newton hacia atrás:\n{polinomio_atras}\n\n")
            self.resultado_text.grid(row=self.puntos+3, columnspan=5)

            self.regresar_button = tk.Button(self, text="Regresar", command=self.regresar)
            self.regresar_button.grid(row=self.puntos+4, columnspan=4)
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos para x y f(x).")

    def regresar(self):
        self.destroy()
        self.on_close_callback()

class MetodoNewtonBackend:
    def __init__(self, tabulacion):
        self.df = pd.DataFrame(tabulacion)
        self.ecuacion = ""
        self.var = {}

    def nombre_df(self, i):
        texto = "f[x_i,"
        i_aux = i
        while i > 0:
            texto = texto + f"x_i+{i_aux-i+1}"
            if i == 1:
                texto = texto + "]"
                break
            texto = texto + ","
            i -= 1
        return texto

    def crear_tabla(self):
        list_aux = []
        k_aux = 0
        for i in range(1, len(self.df['x_i'])):
            for j in range(0, len(self.df.iloc[:, i-1])-1-k_aux):
                list_aux.append((self.df.iloc[j+1, i] - self.df.iloc[j, i])/(self.df.iloc[j+i, 0] - self.df.iloc[j, 0]))
            for k in range(0, i):
                list_aux.append("---")
                k_aux = k+1
            self.df.insert(len(self.df.columns), self.nombre_df(i), list_aux)
            list_aux.clear()
        return str(self.df)

    def crear_polinomio_adelante(self):
        self.ecuacion = ""
        self.var = {}
        for i in range(0, len(self.df['x_i'])):
            self.var[sp.Symbol(f'c_{i}')] = sp.Symbol(f'c_{i}')
            if i == 0:
                self.ecuacion = self.ecuacion + str(sp.Symbol(f'c_{i}'))
            else:
                self.ecuacion = self.ecuacion + "+" + str(sp.Symbol(f'c_{i}'))
            for j in range(0, i):
                self.ecuacion = self.ecuacion + f"*(x-{self.df['x_i'][j]})"

        for i in range(1, len(self.var)+1):
            self.var[sp.Symbol(f'c_{i-1}')] = round(float(self.df.iloc[0, i]), 6)
        ecuacion_sol = sp.sympify(self.ecuacion).subs(self.var)
        return ecuacion_sol

    def crear_polinomio_atras(self):
        self.ecuacion = ""
        self.var = {}
        index = len(self.df['x_i'])
        for i in range(index, 0, -1):
            self.var[sp.Symbol(f'c_{index-i}')] = sp.Symbol(f'c_{index-i}')
            if i == index:
                self.ecuacion = self.ecuacion + str(sp.Symbol(f'c_{index-i}'))
            else:
                self.ecuacion = self.ecuacion + "+" + str(sp.Symbol(f'c_{index-i}'))
            for j in range(index-1, i-1, -1):
                self.ecuacion = self.ecuacion + f"*(x-{self.df['x_i'][j]})"

        for i in range(1, len(self.var)+1):
            self.var[sp.Symbol(f'c_{i-1}')] = round(float(self.df.iloc[index-i, i]), 6)
        ecuacion_sol = sp.sympify(self.ecuacion).subs(self.var)
        return ecuacion_sol

def on_close_callback():
    print("Ventana cerrada.")

if __name__ == "__main__":
    app = MetodoNewton(on_close_callback)
    app.mainloop()
