import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

class MetodoSimpson3_8App:
    def __init__(self, on_close_callback):
        self.root = tk.Tk()    
        self.on_close_callback = on_close_callback
        self.root.title("Método de Simpson 3/8")

        self.frame_size_input = ttk.Frame(self.root)
        self.frame_size_input.pack(pady=10)

        self.label_intervalo = tk.Label(self.frame_size_input , text="Intervalo de la integral (separado por comas):")
        self.label_intervalo.grid(row=0, column=0, padx=5, pady=5)
        self.entry_intervalo = tk.Entry(self.frame_size_input )
        self.entry_intervalo.grid(row=0, column=1, padx=5, pady=5)

        self.label_num_puntos = tk.Label(self.frame_size_input , text="Cantidad de puntos de la función:")
        self.label_num_puntos.grid(row=1, column=0, padx=5, pady=5)
        self.entry_num_puntos = tk.Entry(self.frame_size_input )
        self.entry_num_puntos.grid(row=1, column=1, padx=5, pady=5)

        self.ingresar_button = tk.Button(self.frame_size_input , text="Ingresar puntos", command=self.ingresar_puntos)
        self.ingresar_button.grid(row=1, column=2, padx=5, pady=5)

        self.calcular_button = tk.Button(self.frame_size_input , text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=10)
        
        self.frame_result = ttk.Frame(self.root)
        self.frame_result.pack(pady=10)

    def ingresar_puntos(self):
        try:
            self.x_entries = []
            num_puntos = int(self.entry_num_puntos.get())
            if (num_puntos - 4) % 3 != 0 :
                messagebox.showerror("Error", "El número de puntos debe seguir la sucesión 4 + 3n.")
            else:
                for i in range(num_puntos):
                    label = tk.Label(self.frame_input, text=f"f(x_{i}):")
                    label.grid(row=3+i, column=0, padx=5, pady=2)
                    entry = tk.Entry(self.frame_input)
                    entry.grid(row=3+i, column=1, padx=5, pady=2)
                    self.x_entries.append(entry)  
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


    def calcular(self):
        try:
            intervalo = [float(numero) for numero in self.entry_intervalo.get().split(',')]
            num = int(self.entry_num_puntos.get())
            valores = {'x':[], 'f(x)':[]}
            distancia = abs((intervalo[1] - intervalo[0]) / (num - 1))
            
            # Obteniendo los valores de f(xi)
            for i in range(num):
                f_x_i = float(self.x_entries[i].get())
                valores['x'].append(round(intervalo[0] + i * distancia, 4))
                valores['f(x)'].append(f_x_i)

            obj = MetodoSimpson3_8(valores, distancia)
            integral_aprox, tabla = obj.calcular_metodo()
            
            # Crear área de texto para mostrar el resultado
            resultado_text = tk.Text(self.frame_result, height=10, width=50)
            resultado_text.grid(row=4+num, column=0, columnspan=3, padx=5, pady=5)
            resultado_text.insert(tk.END, tabla)
            resultado_text.insert(tk.END, f"\nCon lo que la aproximación de la integral es: {integral_aprox}")

            # Botón para regresar
            regresar_button = tk.Button(self.frame_result, text="Regresar", command=self.regresar)
            regresar_button.grid(row=5+num, column=0, columnspan=3, padx=5, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
    def regresar(self):
        self.root.destroy()
        self.on_close_callback()

class MetodoSimpson3_8():
    def __init__(self, valores: dict, diferencia_entre_puntos: float):
        self.valores = valores
        self.diferencia_entre_puntos = diferencia_entre_puntos

    def calcular_metodo(self):
        integral_aprox = float
        aux_df = pd.DataFrame(self.valores)
        for i in range(1,len(aux_df)-2,3):
            aux_df.loc[i,"c_i"] = round(3, 4)
        for i in range(2,len(aux_df)-1,3):
            aux_df.loc[i,"c_i"] = round(3, 4)
        for i in range(3, len(aux_df)-3,3):
            aux_df.loc[i, "c_i"] = round(2,4)
        aux_df.loc[0, 'c_i'] = round(1, 4)
        aux_df.loc[len(aux_df) - 1, 'c_i'] = round(1, 4)
        aux_df['c_i*f(x)'] = round(aux_df['c_i'] * aux_df['f(x)'], 4)
        integral_aprox = round((self.diferencia_entre_puntos*3/8)*sum(aux_df['c_i*f(x)']), 4)
        tabla = str(aux_df)
        return integral_aprox, tabla

