#Librerias.
from tkinter import *
from tkinter import ttk
# Código todas las funciones y constantes matemáticas predefinidas que ofrece el módulo
import math


def TemaObscuro(*args):
    estilos.configure('mainframe.Frame', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('Label2.TLabel', background="#010924", foreground="white")

    estilos_botones_numeros.configure('botones_numeros.TButton', background="#483D8B", foreground="white")
    estilos_botones_numeros.map('botones_numeros.TButton', background=[('active', '#020A90')])

    estilos_botones_borrar.configure('botones_borrar.TButton', background="#191970", foreground="white")
    estilos_botones_borrar.map('botones_borrar.TButton', background=[('active', '#020A90')])

    estilos_botones_restantes.configure('botones_restantes.TButton', background="#191970", foreground="white")
    estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#020A90')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure('botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map('botones_numeros.TButton', background=[('active', '#B9B9B9')])
    
    estilos_botones_borrar.configure('botones_borrar.TButton', background="#CECECE", foreground="black")
    estilos_botones_borrar.map('botones_borrar.TButton', background=[('active', '#858585')])

    estilos_botones_restantes.configure('botones_restantes.TButton', background="#CECECE", foreground="black")
    estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#858585')])
    
def ingresarValores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' :
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' :
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
            
        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char
    print(event)

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        
        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raizCuadrada():

    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def borrarTodo(*args):
    entrada1.set('')
    entrada2.set('')

def calcular_potencia():

    try:
        # Obtener la base y el exponente de las entradas
        base = float(entrada2.get())  # Convertir el texto de entrada1 a número
        exponente = float(entrada1.get())  # Convertir el texto de entrada2 a número
        
        # Calcular la potencia
        resultado_potencia = base ** exponente
        
        # Mostrar el resultado en la etiqueta de resultado
        entrada2.set(f"Resultado: {resultado_potencia}")
    except ValueError:
        # Manejar errores si las entradas no son números válidos
        entrada2.set("Error: Ingresa números válidos")

def funcion_x():
    valor_x = entrada2.get()
    # Suponiendo que hay un label para mostrar el valor
    entrada2.config(text=f"El valor de x es: {valor_x}")

def resolver_ecuacion_primer_grado():
    ecuacion = entrada2.get()  # Obtener la ecuación ingresada por el usuario

    # Utilizar expresiones regulares para extraer los coeficientes
    match = re.match(r"(-?\d*)x\s*([+-]\s*\d+)", ecuacion)
    if match:
        a = float(match.group(1) or 1)  # Si no hay coeficiente para x, asumimos a=1
        b = float(match.group(2))
        if a == 0:
            entrada2.set("Error: No se puede dividir por cero")
        else:
            x = -b / a
            entrada2.set(f"x = {x}")
    else:
        entrada2.set("Error: Formato de ecuación inválido")

def ingresarValore2(tecla2):
    if tecla2 == 'sin' or tecla2 == 'cos' or tecla2 == 'asin' or tecla2 == 'acos' or tecla2 == 'tan' or tecla2 == 'ctan' or tecla2 == 'atan' or tecla2 == 'actan' or tecla2 == 'log' or tecla2 == 'exp' or tecla2 == 'sinh' or tecla2 == 'cos' or tecla2 == 'sqrt' or tecla2 == 'cbrt' or tecla2 == 'tanh' or tecla2 == 'ctanh' or tecla2 == 'asinh' or tecla2 == 'acosh' or tecla2 == 'atanh' or tecla2 == 'actanh' or tecla2 == 'cosh ':
            # Concatenar 'sin(' y ')' para indicar la función seno
            entrada2.set(entrada2.get() + tecla2 + '(')
    if tecla2 == 'sin':
            entrada1.set(entrada2.get())
    elif tecla2 == 'cos':
        entrada1.set(entrada2.get())
 
root = Tk()
root.title("Calculadora")
#Coordenadas de donde saldra la interfaz grafica.
root.geometry("+350+100")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")   
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)

#Estilos labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

#Donde se colocaran los resultados
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=8, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=8, sticky=(W, N, E, S))

#Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('botones_numeros.TButton', font="arial 15", width=5, background="#00CED1", relief="flat")

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="arial 15", width=5, relief="flat", background="#008B8B")

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('botones_restantes.TButton', font="arial 15", width=5, relief="flat", background="#20B2AA")

#Aqui se crean los botones del 0 al 9.
Button0 = ttk.Button(mainframe, text="0", style="botones_numeros.TButton", command=lambda: ingresarValores('0'))
Button1 = ttk.Button(mainframe, text="1", style="botones_numeros.TButton", command=lambda: ingresarValores('1'))
Button2 = ttk.Button(mainframe, text="2", style="botones_numeros.TButton", command=lambda: ingresarValores('2'))
Button3 = ttk.Button(mainframe, text="3", style="botones_numeros.TButton", command=lambda: ingresarValores('3'))
Button4 = ttk.Button(mainframe, text="4", style="botones_numeros.TButton", command=lambda: ingresarValores('4'))
Button5 = ttk.Button(mainframe, text="5", style="botones_numeros.TButton", command=lambda: ingresarValores('5'))
Button6 = ttk.Button(mainframe, text="6", style="botones_numeros.TButton", command=lambda: ingresarValores('6'))
Button7 = ttk.Button(mainframe, text="7", style="botones_numeros.TButton", command=lambda: ingresarValores('7'))
Button8 = ttk.Button(mainframe, text="8", style="botones_numeros.TButton", command=lambda: ingresarValores('8'))
Button9 = ttk.Button(mainframe, text="9", style="botones_numeros.TButton", command=lambda: ingresarValores('9'))

#Aqui se crean los botones de Borrar, Borrrar_todo, parentesis y punto.
Button_borrar = ttk.Button(mainframe, text=chr(9003), style="botones_borrar.TButton", command=lambda: borrar())
Button_borrar_todo = ttk.Button(mainframe, text="C", style="botones_borrar.TButton", command=lambda: borrarTodo())
Button_parentesis1 = ttk.Button(mainframe, text="(", style="botones_restantes.TButton", command=lambda: ingresarValores('('))
Button_parentesis2 = ttk.Button(mainframe, text=")", style="botones_restantes.TButton", command=lambda: ingresarValores(')'))
Button_punto = ttk.Button(mainframe, text=".", style="botones_restantes.TButton", command=lambda: ingresarValores('.'))

#Aqui se crean los botones de operaciones.
Button_division = ttk.Button(mainframe, text=chr(247), style="botones_restantes.TButton", command=lambda: ingresarValores('/'))
Button_multiplicacion = ttk.Button(mainframe, text="x", style="botones_restantes.TButton", command=lambda: ingresarValores('*'))
Button_resta = ttk.Button(mainframe, text="-", style="botones_restantes.TButton", command=lambda: ingresarValores('-'))
Button_suma = ttk.Button(mainframe, text="+", style="botones_restantes.TButton", command=lambda: ingresarValores('+'))
Button_pi = ttk.Button(mainframe, text="pi", style="botones_restantes.TButton", command=lambda: ingresarValores('3.1416'))
Button_sin = ttk.Button(mainframe, text="sin", style="botones_restantes.TButton", command=lambda:ingresarValore2 ('sin'))
Button_cos = ttk.Button(mainframe, text="cos", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('cos'))
Button_tan = ttk.Button(mainframe, text="tan", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('tan'))
Button_ctan = ttk.Button(mainframe, text="ctan", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('ctan'))
Button_log = ttk.Button(mainframe, text="log", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('log'))
Button_exp = ttk.Button(mainframe, text="exp", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('exp'))
Button_sqrt = ttk.Button(mainframe, text="sqrt", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('sqrt'))
Button_cbrt = ttk.Button(mainframe, text="cbrt", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('cbrt'))
Button_asin = ttk.Button(mainframe, text="asin", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('asin'))
Button_acos = ttk.Button(mainframe, text="acos", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('acos'))
Button_atan = ttk.Button(mainframe, text="atan", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('atan'))
Button_actan = ttk.Button(mainframe, text="actan", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('actan'))
Button_sinh = ttk.Button(mainframe, text="sinh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('sinh'))
Button_cosh = ttk.Button(mainframe, text="cosh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('cosh'))
Button_tanh = ttk.Button(mainframe, text="tanh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('tanh'))
Button_ctanh = ttk.Button(mainframe, text="ctanh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('ctanh'))
Button_asinh = ttk.Button(mainframe, text="asinh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('asinh'))
Button_acosh = ttk.Button(mainframe, text="acosh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('acosh'))
Button_atanh = ttk.Button(mainframe, text="atanh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('atanh'))
Button_actanh = ttk.Button(mainframe, text="actanh", style="botones_restantes.TButton", command=lambda: ingresarValore2 ('actanh'))
Button_resolver = ttk.Button(mainframe, text="1er Grado",style="botones_restantes.TButton", command=lambda: resolver_ecuacion_primer_grado())

Button_e = ttk.Button()
Button_igual = ttk.Button(mainframe, text="=", style="botones_restantes.TButton", command=lambda: ingresarValores('='))
Button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="botones_restantes.TButton", command=lambda: raizCuadrada())
Button_x = ttk.Button(mainframe, text="x", style="botones_restantes.TButton", command=lambda: funcion_x())
Button_y = ttk.Button(mainframe, text="y", style="botones_restantes.TButton")
Button_potencia = ttk.Button(mainframe, text="POT", style="botones_restantes.TButton", command=lambda: calcular_potencia())

#colocar botones en pantalla.
Button_pi.grid(column=0, row=2, sticky=(W, N, E, S))
Button_parentesis1.grid(column=1, row=2, sticky=(W, N, E, S))
Button_parentesis2.grid(column=2, row=2, sticky=(W, N, E, S))
Button_potencia.grid(column=3, row=2, sticky=(W, N, E, S))
Button_borrar_todo.grid(column=4, row=2, columnspan=2, sticky=(W, N, E, S))
Button_borrar.grid(column=6, row=2, columnspan=2, sticky=(W, N, E, S))

Button7.grid(column=0, row=3, sticky=(W, N, E, S))
Button8.grid(column=1, row=3, sticky=(W, N, E, S))
Button9.grid(column=2, row=3, sticky=(W, N, E, S))
Button_sin.grid(column=3, row=3, sticky=(W, N, E, S))
Button_cos.grid(column=4, row=3, sticky=(W, N, E, S))
Button_asin.grid(column=5, row=3, sticky=(W,N,E,S))
Button_acos.grid(column=6, row=3, sticky=(W,N,E,S))
Button_division.grid(column=7, row=3, sticky=(W, N, E, S))

Button4.grid(column=0, row=4, sticky=(W, N, E, S))
Button5.grid(column=1, row=4, sticky=(W, N, E, S))
Button6.grid(column=2, row=4, sticky=(W, N, E, S))
Button_tan.grid(column=3, row=4, sticky=(W, N, E, S))
Button_ctan.grid(column=4, row=4, sticky=(W, N, E, S))
Button_atan.grid(column=5, row=4, sticky=(W, N, E, S))
Button_actan.grid(column=6, row=4, sticky=(W, N, E, S))
Button_multiplicacion.grid(column=7, row=4, sticky=(W, N, E, S))

Button1.grid(column=0, row=5, sticky=(W, N, E, S))
Button2.grid(column=1, row=5, sticky=(W, N, E, S))
Button3.grid(column=2, row=5, sticky=(W, N, E, S))
Button_log.grid(column=3, row=5, sticky=(W, N, E, S))
Button_exp.grid(column=4, row=5, sticky=(W, N, E, S))
Button_sinh.grid(column=5, row=5, sticky=(W, N, E, S))
Button_cosh.grid(column=6, row=5, sticky=(W, N, E, S))
Button_suma.grid(column=7, row=5, sticky=(W, N, E, S))

Button_resolver.grid(column=0, row=6, sticky=(W, N, E, S))
Button0.grid(column=1, row=6, sticky=(W, N, E, S)) #Con sticky agrega para anclar de lado a lado el 0.
Button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
Button_sqrt.grid(column=3, row=6, sticky=(W, N, E, S))
Button_cbrt.grid(column=4, row=6, sticky=(W, N, E, S))
Button_tanh.grid(column=5, row=6, sticky=(W, N, E, S))
Button_ctanh.grid(column=6, row=6, sticky=(W, N, E, S))
Button_resta.grid(column=7, row=6, sticky=(W, N, E, S))

Button_x.grid(column=0, row=7, sticky=(W, N, E, S))
Button_y.grid(column=1, row=7, sticky=(W, N, E, S))
Button_raiz_cuadrada.grid(column=2, row=7, sticky=(W, N, E, S))
Button_asinh.grid(column=3, row=7, sticky=(W, N, E, S))
Button_acosh.grid(column=4, row=7, sticky=(W, N, E, S))
Button_atanh.grid(column=5, row=7, sticky=(W, N, E, S))
Button_actanh.grid(column=6, row=7, sticky=(W, N, E, S)) 
Button_igual.grid(column=7, row=7, sticky=(W, N, E, S))


for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-o>', TemaObscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', ingresarValoresTeclado)
#Para borrar desde teclado
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-q>', borrarTodo)

root, mainloop()
