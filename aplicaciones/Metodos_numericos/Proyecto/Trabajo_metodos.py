import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from puntoFijo import *
from diferenciaDivididas import *
from Lagrange import *
from newton_raphson_metodos_numericos import *
from newton import *
from simpson1tercio import *
from simpson3octavos import *
from trapecio import *
from interfazMC import *


def centrar_ventana(root, width=800, height=600):
    # Obtiene las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcula las coordenadas x, y para colocar la ventana en el centro
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Configura la geometría de la ventana
    root.geometry(f"{width}x{height}+{x}+{y}")

class Portada:
    def __init__(self, master):
        self.master = master
        self.master.title("Portada")
        centrar_ventana(self.master)  # Centra la ventana

        self.label1 = tk.Label(master, text="Bienvenido a SINAP", font=("Times New Roman", 27))
        self.label1.pack(pady=20)
        
        self.label2 = tk.Label(master, text="Universidad Autonoma de Mexico\nEscuela de Estudios Superiores Acatlan\n\n\nProyecto de Metodos Numericos\n\n\nArteaga Reyes Aldair\n Flores Gómez Javier Alberto\n Gabriel Cruz Alondra Paloma \n Moreno Lugo Hava Josette \n San Pedro Avila Pablo", wraplength=300,font=("Times New Roman", 17))
        self.label2.pack()

        # Cargamos las imágenes
        self.image1 = Image.open("a.png")
        self.image2 = Image.open("b.png")

        # Redimensionamos las imágenes
        self.image1 = self.image1.resize((150, 150), Image.LANCZOS)
        self.image2 = self.image2.resize((150, 150), Image.LANCZOS)


        # Convertimos las imágenes en formato que Tkinter pueda mostrar
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.photo2 = ImageTk.PhotoImage(self.image2)

        # Creamos etiquetas para mostrar las imágenes
        self.label1 = ttk.Label(master, image=self.photo1)
        self.label1.place(x=10, y=10)  # Colocar en la esquina superior izquierda

        self.label2 = ttk.Label(master, image=self.photo2)
        self.label2.place(x=630, y=10)  # Colocar en la esquina superior derecha
        
        self.button_next = tk.Button(master, text="Siguiente", command=self.mostrar_siguiente)
        self.button_next.pack(pady=20)
    
    def mostrar_siguiente(self):
        self.master.withdraw()
        siguiente_ventana = tk.Toplevel()
        siguiente_ventana.title("Portada")
        centrar_ventana(siguiente_ventana)  # Centra la ventana

        self.label3 = tk.Label(siguiente_ventana, text="Introduccion", font=("Helvetica", 30))
        self.label3.pack(pady=10)
        
        self.label4 = tk.Label(siguiente_ventana, text="Este programa ha sido diseñado con el propósito de proporcionar a los participantes una comprensión profunda y práctica de las técnicas fundamentales utilizadas en la aproximación y resolución de problemas matemáticos y científicos mediante el uso de algoritmos computacionales. Nuestro programa abarca una amplia gama de temas, desde la resolución de sistemas de ecuaciones lineales hasta la interpolación de datos y la integración numérica. Uno de los aspectos distintivos de nuestro programa es su enfoque en la aplicación práctica de los métodos numéricos en situaciones del mundo real. A través de un sistema el cual permite usar varios tipos de métodos así como la introducción a cada uno de ellos, esto permite tener una amplia gama de soluciones a diversos problemas. En resumen, nuestro programa de métodos numéricos ofrece una combinación única de teoría y práctica que ayudarán a resolver problemas computacionales complejos en campos como la ingeniería, la física, la economía y la ciencia de datos.", wraplength=700, font=("Arial", 15))
        self.label4.pack()

        
        self.button_next = tk.Button(siguiente_ventana, text="Siguiente", command=self.cerrar_portada)
        self.button_next.pack(pady=40)
        
    def cerrar_portada(self):
        self.master.destroy()
        siguiente_panel = Opciones()

class Opciones:
    def __init__(self):
        self.pestaña_opciones = tk.Tk()  
        self.pestaña_opciones.title("Temas")
        centrar_ventana(self.pestaña_opciones, width=800, height=600)  # Centra la ventana y establece el tamaño

        self.left_panel = tk.Frame(self.pestaña_opciones, width=600, height=400, bg="lightgray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.right_panel = tk.Frame(self.pestaña_opciones, width=200, height=400, bg="lightblue")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.current_widgets = []

        self.welcome_label = tk.Label(self.right_panel, text="Bienvenido", font=("Helvetica", 30))
        self.welcome_label.pack(pady=50)

        self.buttons_info = [
            {"label": "Sistemas de ecuaciones no lineales", "command": self.show_data_1, "text": "texto_1"},
            {"label": "Interpolación y aproximación polinomial", "command": self.show_data_2, "text": "Texto_2"},
            {"label": "Derivación e integración numérica", "command": self.show_data_3, "text": "Texto_3"},
            {"label": "Salir", "command": self.fin_app}
        ]

        self.options_btns = []
        for button_info in self.buttons_info:
            btn = tk.Button(self.left_panel, text=button_info["label"], command=button_info["command"], width=30, height=3, font=("Arial", 10))
            btn.pack(pady=20,fill="none", expand=False)
            self.options_btns.append(btn)


    def clear_right_panel(self):
        for widget in self.right_panel.winfo_children():
            widget.destroy()

    def show_widgets(self, tema_label, tema_text, abrir_tema_func):
        self.clear_right_panel()
        label = tk.Label(self.right_panel, text=tema_label, font=("Arial", 14))
        label.pack(pady=10)
        label_tema = tk.Label(self.right_panel, text=tema_text, font=("Arial", 14), wraplength=500)  # Ajusta el valor de wraplength según tu preferencia
        label_tema.pack(pady=10)
        submit_btn = tk.Button(self.right_panel, text="Entrar", command=abrir_tema_func)
        submit_btn.pack(pady=10)

    def show_data_1(self):
        self.show_widgets("Sistemas de ecuaciones no lineales", "Cuando pensamos en resolver ecuaciones, a menudo imaginamos simples operaciones como sumar o multiplicar. Pero cuando las ecuaciones se vuelven más complejas y no pueden expresarse como simples líneas rectas, entramos en el mundo de los sistemas de ecuaciones no lineales. Estos sistemas pueden incluir ecuaciones con formas curvas, exponenciales o trigonométricas, haciendo que su solución sea un desafío emocionante. A través de métodos como el punto fijo o Newton-Raphson, los matemáticos y científicos pueden aproximarse a las soluciones de estos sistemas, abriendo la puerta a una variedad de aplicaciones en la ciencia, la ingeniería y más allá.", self.abrir_tema_1)

    def show_data_2(self):
        self.show_widgets("Interpolación y aproximación polinomial", "Imagina que tienes un conjunto de datos dispersos y necesitas estimar valores entre ellos. Aquí es donde entra en juego la interpolación y la aproximación polinomial. Estas técnicas te permiten crear curvas suaves que se ajusten a tus datos existentes, lo que facilita la predicción de valores intermedios. Con métodos como el método de Lagrange o las diferencias divididas de Newton, puedes construir polinomios que pasen exactamente por tus puntos de datos o que se ajusten de manera óptima a ellos, proporcionando una herramienta poderosa para la modelización y la predicción en una variedad de campos.", self.abrir_tema_2)

    def show_data_3(self):
        self.show_widgets("Derivación e integración numérica", "¿Qué pasa si necesitas calcular la derivada o la integral de una función complicada pero no puedes hacerlo con métodos tradicionales? Ahí es donde entra la derivación e integración numérica. Estas técnicas te permiten aproximar derivadas e integrales utilizando métodos computacionales, como el método de los mínimos cuadrados, el método del trapecio o los métodos de Simpson. Aunque no siempre son tan precisos como los métodos analíticos, son extremadamente útiles cuando la complejidad de las funciones hace que los métodos tradicionales sean impracticables, abriendo un mundo de posibilidades en la simulación, la física computacional y más.", self.abrir_tema_3)

    def fin_app(self):
        self.pestaña_opciones.destroy()

    def abrir_tema_1(self):
        gui = ins_tema1()
        self.pestaña_opciones.destroy()

    def abrir_tema_2(self):
        gui = ins_tema2()
        self.pestaña_opciones.destroy()

    def abrir_tema_3(self):
        gui = ins_tema3()
        self.pestaña_opciones.destroy()

class ins_tema1:
    def __init__(self):
        self.pestaña_tema1 = tk.Tk()  
        self.pestaña_tema1.title("Sistemas de ecuaciones no lineales")
        centrar_ventana(self.pestaña_tema1, width=800, height=600)  # Centra la ventana y establece el tamaño

        self.left_panel = tk.Frame(self.pestaña_tema1, width=600, height=400, bg="lightgray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.right_panel = tk.Frame(self.pestaña_tema1, width=200, height=400, bg="lightblue")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.current_widgets = []

        self.welcome_label = tk.Label(self.right_panel, text="Metodos de Sistemas de ecuaciones no lineales", font=("Helvetica", 18))
        self.welcome_label.pack(pady=50)

        self.buttons_info = [
            {"label": "Punto Fijo", "command": self.show_data_1, "text": "Texto para el tema 1"},
            {"label": "Newton-Rapson", "command": self.show_data_2, "text": "Texto para el tema 2"}, 
            {"label": "Regresar", "command": self.regresar_app}
        ]

        self.options_btns = []
        for button_info in self.buttons_info:
            btn = tk.Button(self.left_panel, text=button_info["label"], command=button_info["command"], width=30, height=3, font=("Arial", 10))
            btn.pack(pady=20,fill="none", expand=False)
            self.options_btns.append(btn)

    def clear_right_panel(self):
        for widget in self.right_panel.winfo_children():
            widget.destroy()

    def show_widgets(self, tema_label, tema_text, abrir_tema_func):
        self.clear_right_panel()
        label = tk.Label(self.right_panel, text=tema_label, font=("Arial", 14))
        label.pack(pady=10)
        label_tema = tk.Label(self.right_panel, text=tema_text, font=("Arial", 14), wraplength=500)  # Ajusta el valor de wraplength según tu preferencia
        label_tema.pack(pady=10)
        submit_btn = tk.Button(self.right_panel, text="Entrar", command=abrir_tema_func)
        submit_btn.pack(pady=10)

    def show_data_1(self):
        self.show_widgets("Punto Fijo", "Imagina que estás tratando de balancear una vara en tu mano. Para mantenerla quieta, necesitas encontrar ese punto en el que la gravedad y la fuerza que aplicas se equilibran. En matemáticas, el método del punto fijo busca ese punto donde una función deja de cambiar significativamente, como cuando la vara se estabiliza en tu mano. Es útil para resolver ecuaciones que no se pueden resolver directamente, y funciona encontrando un valor que hace que la función se estabilice o alcance un punto fijo.", self.abrir_tema_1)

    def show_data_2(self):
        self.show_widgets("Newton-Rapson", "¿Alguna vez has seguido las migajas de pan para encontrar tu camino de regreso? El método de Newton-Raphson es un poco como eso, pero en el mundo de las ecuaciones. Cuando tienes una ecuación complicada que no puedes resolver de forma directa, este método te guía en la dirección correcta para encontrar la solución. Funciona tomando un punto inicial y ajustándolo iterativamente para acercarse más y más a la solución deseada, como seguir las migas de pan hasta llegar a casa.", self.abrir_tema_2)

    def regresar_app(self):
        siguiente_panel = Opciones()
        self.pestaña_tema1.destroy()

    def abrir_tema_1(self):
        self.pestaña_tema1.withdraw()
        gui = PuntoFijoApp( self.reabrir_pestaña_tema1)

    def abrir_tema_2(self): 
        self.pestaña_tema1.withdraw()
        gui = mostrar_panel( self.reabrir_pestaña_tema1)

    def reabrir_pestaña_tema1(self):
        self.pestaña_tema1.deiconify()

class ins_tema2:
    def __init__(self):
        self.pestaña_tema2 = tk.Tk()  
        self.pestaña_tema2.title("Interpolación y aproximación polinomial")
        centrar_ventana(self.pestaña_tema2, width=800, height=600)  # Centra la ventana y establece el tamaño

        self.left_panel = tk.Frame(self.pestaña_tema2, width=600, height=400, bg="lightgray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.right_panel = tk.Frame(self.pestaña_tema2, width=200, height=400, bg="lightblue")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.current_widgets = []

        self.welcome_label = tk.Label(self.right_panel, text="Metodos de Interpolación y aproximación polinomial", font=("Helvetica", 17))
        self.welcome_label.pack(pady=50)

        self.buttons_info = [
            {"label": "Lagrange", "command": self.show_data_1, "text": "Texto para el tema 1"},
            {"label": "Diferencias Divididas", "command": self.show_data_2, "text": "Texto para el tema 2"}, 
            {"label": "Newton-Adelante/Atras", "command": self.show_data_3, "text": "Texto para el tema 3"}, 
            {"label": "Minimos Cuadrados", "command": self.show_data_4, "text": "Texto para el tema 4"}, 
            {"label": "Regresar", "command": self.regresar_app}
        ]

        self.options_btns = []
        for button_info in self.buttons_info:
            btn = tk.Button(self.left_panel, text=button_info["label"], command=button_info["command"], width=30, height=3, font=("Arial", 10))
            btn.pack(pady=20,fill="none", expand=False)
            self.options_btns.append(btn)

    def clear_right_panel(self):
        for widget in self.right_panel.winfo_children():
            widget.destroy()

    def show_widgets(self, tema_label, tema_text, abrir_tema_func):
        self.clear_right_panel()
        label = tk.Label(self.right_panel, text=tema_label, font=("Arial", 14))
        label.pack(pady=10)
        label_tema = tk.Label(self.right_panel, text=tema_text, font=("Arial", 14), wraplength=500)  # Ajusta el valor de wraplength según tu preferencia
        label_tema.pack(pady=10)
        submit_btn = tk.Button(self.right_panel, text="Entrar", command=abrir_tema_func)
        submit_btn.pack(pady=10)

    def show_data_1(self):
        self.show_widgets("Lagrange", " Cuando intentas conectar puntos dispersos en un gráfico con una línea suave, el método de Lagrange es tu herramienta. Imagina que tienes un conjunto de puntos en un gráfico y necesitas una función que los conecte de manera suave, como trazar una curva entre puntos en un mapa. Este método utiliza polinomios para encontrar esa función, asegurándose de que pase exactamente por todos los puntos dados. Es como encontrar el mejor camino entre puntos de referencia en un mapa para que sea lo más suave posible.", self.abrir_tema_1)

    def show_data_2(self):
        self.show_widgets("Diferencias Divididas", "Cuando estás tratando de medir cómo cambian las cosas en el tiempo o el espacio, las diferencias divididas te ayudan a descomponer esos cambios en pasos más pequeños y manejables. Es como desglosar una gran distancia en pasos más cortos para entender mejor el movimiento. Este método se utiliza en la interpolación polinomial para estimar cómo cambia una función entre puntos dados, lo que permite crear una aproximación suave de la función original.", self.abrir_tema_2)

    def show_data_3(self):
        self.show_widgets("Newton-Adelante", " Estos métodos son como ver hacia adelante o hacia atrás en una película para entender cómo se desarrolla la trama. Newton hacia adelante estima la derivada de una función mirando hacia adelante desde un punto dado, mientras que Newton hacia atrás hace lo mismo, pero mirando hacia atrás. Ambos métodos son útiles para calcular derivadas de manera aproximada cuando no se tiene acceso a una fórmula explícita.", self.abrir_tema_3)

    def show_data_4(self):
        self.show_widgets("Minimos Cuadrados", "¿Alguna vez has intentado dibujar una línea recta que pase por la mayoría de los puntos dispersos en un gráfico? Los mínimos cuadrados te ayudan a hacer exactamente eso. Este método busca la mejor línea de ajuste para un conjunto de datos dispersos minimizando la suma de los cuadrados de las diferencias entre los puntos y la línea. Es como encontrar esa línea promedio que mejor se adapta a tus datos, incluso si algunos puntos están un poco fuera de lugar.", self.abrir_tema_4)
  
    def regresar_app(self):
        siguiente_panel = Opciones()
        self.pestaña_tema2.destroy()

    def abrir_tema_1(self):
        self.pestaña_tema2.withdraw()
        gui =LagrangeMetodo( self.reabrir_pestaña_tema2)

    def abrir_tema_2(self): 
        self.pestaña_tema2.withdraw()
        gui =DiferenciasDivididasGUI( self.reabrir_pestaña_tema2)

    def abrir_tema_3(self): 
        self.pestaña_tema2.withdraw()
        gui =MetodoNewton( self.reabrir_pestaña_tema2) 

    def abrir_tema_4(self): 
        self.pestaña_tema2.withdraw()
        gui =Min_Cuad_metodo( self.reabrir_pestaña_tema2)

    def reabrir_pestaña_tema2(self):
        self.pestaña_tema2.deiconify()


class ins_tema3:
    def __init__(self):
        self.pestaña_tema3 = tk.Tk()  
        self.pestaña_tema3.title("Derivación e integración numérica")
        centrar_ventana(self.pestaña_tema3, width=800, height=600)  # Centra la ventana y establece el tamaño

        self.left_panel = tk.Frame(self.pestaña_tema3, width=600, height=400, bg="lightgray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.right_panel = tk.Frame(self.pestaña_tema3, width=200, height=400, bg="lightblue")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.current_widgets = []

        self.welcome_label = tk.Label(self.right_panel, text="Metodos de Derivación e integración numérica", font=("Helvetica", 17))
        self.welcome_label.pack(pady=50)

        self.buttons_info = [
            {"label": "Metodo Trapecio", "command": self.show_data_1, "text": "Texto para el tema 1"},
            {"label": "Metodo Simpson 1/3", "command": self.show_data_2, "text": "Texto para el tema 2"}, 
            {"label": "Metodo Simpson 3/8", "command": self.show_data_3, "text": "Texto para el tema 3"},  
            {"label": "Regresar", "command": self.regresar_app}
        ]

        self.options_btns = []
        for button_info in self.buttons_info:
            btn = tk.Button(self.left_panel, text=button_info["label"], command=button_info["command"], width=30, height=3, font=("Arial", 10))
            btn.pack(pady=20,fill="none", expand=False)
            self.options_btns.append(btn)

    def clear_right_panel(self):
        for widget in self.right_panel.winfo_children():
            widget.destroy()

    def show_widgets(self, tema_label, tema_text, abrir_tema_func):
        self.clear_right_panel()
        label = tk.Label(self.right_panel, text=tema_label, font=("Arial", 14))
        label.pack(pady=10)
        label_tema = tk.Label(self.right_panel, text=tema_text, font=("Arial", 14), wraplength=500)
        label_tema.pack(pady=10)
        submit_btn = tk.Button(self.right_panel, text="Enviar", command=abrir_tema_func)
        submit_btn.pack(pady=10)

    def show_data_1(self):
        self.show_widgets("Metodo Trapecio", "Cuando intentas calcular el área bajo una curva que no es fácilmente integrable, el método del trapecio es una herramienta útil. Imagina que tienes una función complicada y quieres encontrar el área debajo de ella. Este método divide el área en pequeños trapecios, utilizando segmentos rectilíneos para conectar los puntos de la función. Luego, suma las áreas de estos trapecios para obtener una aproximación del área total. Cuanto más pequeños sean los trapecios, más precisa será la aproximación.", self.abrir_tema_1)

    def show_data_2(self):
        self.show_widgets("Metodo Simpson 1/3", "Este método es una mejora del método del trapecio, diseñado para proporcionar una mejor aproximación del área bajo una curva. En lugar de usar trapecios, divide el área en segmentos de parábolas, utilizando tres puntos consecutivos para definir cada parábola. Esto crea una aproximación más precisa porque las parábolas se ajustan mejor a la forma de la curva que los trapecios. Al sumar las áreas de estas parábolas, obtienes una mejor estimación del área total bajo la curva.", self.abrir_tema_2)

    def show_data_3(self):
        self.show_widgets("Metodo Simpson 3/8", "Es una extensión del método de Simpson 1/3 y ofrece una mayor precisión en la aproximación del área bajo la curva. En lugar de usar parábolas, divide el área en segmentos aún más pequeños, utilizando polinomios de tercer grado para conectar cuatro puntos consecutivos. Esto proporciona una aproximación aún más precisa del área total, ya que los polinomios de tercer grado pueden adaptarse mejor a la forma de la curva que las parábolas. Sumando las áreas de estos segmentos, obtienes una estimación muy cercana al área real bajo la curva.", self.abrir_tema_3)

    def regresar_app(self):
        siguiente_panel = Opciones()
        self.pestaña_tema3.destroy()

    def abrir_tema_1(self):
        self.pestaña_tema3.withdraw()
        gui =MetodoTrapecioApp( self.reabrir_pestaña_tema3)

    def abrir_tema_2(self):
        self.pestaña_tema3.withdraw()
        gui =MetodoSimpson1_3App( self.reabrir_pestaña_tema3) 

    def abrir_tema_3(self):
        self.pestaña_tema3.withdraw()
        gui =MetodoSimpson3_8App( self.reabrir_pestaña_tema3) 

    def reabrir_pestaña_tema3(self):
        self.pestaña_tema3.deiconify()

root = tk.Tk()
app = Portada(root)
centrar_ventana(root)  # Centra la ventana principal
root.mainloop()