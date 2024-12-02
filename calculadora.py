#Librerias.
from tkinter import *
from tkinter import ttk
#Para sacar la raiz cuadrada
import math

def TemaObscuro(*args):
    estilos.configure('mainframe.Frame', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010924", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#010924", foreground="black")

    estilos_botones_numeros.configure('botones_numeros.TButton', background="#00044A", foreground="green")
    estilos_botones_numeros.map('botones_numeros.Tbutton', background=[('#020A90')])

    estilos_botones_borrar.configure('botones_borrar.TButton', background="#010924", foreground="green")
    estilos_botones_borrar.map('botones_borrar.TButton', background=[('active', '#000AB1')])

    estilos_botones_restantes.configure('botones_restantes.TButton', background="#010924", foreground="green")
    estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#000AB1')])

root = Tk()
root.title("Calculadora")
#Coordenadas de donde saldra la interfaz grafica.
root.geometry("+800+200")
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

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=6, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=6, sticky=(W, N, E, S))

#Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('botones_numeros.TButton', font="arial 15", width=5, background="#00CED1", relief="flat")

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="arial 15", width=5, relief="flat", background="#008B8B")

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('botones_restantes.TButton', font="arial 15", width=5, relief="flat", background="#20B2AA")

#Aqui se crean los botones del 0 al 9.
Button0 = ttk.Button(mainframe, text="0", style="botones_numeros.TButton")
Button1 = ttk.Button(mainframe, text="1", style="botones_numeros.TButton")
Button2 = ttk.Button(mainframe, text="2", style="botones_numeros.TButton")
Button3 = ttk.Button(mainframe, text="3", style="botones_numeros.TButton")
Button4 = ttk.Button(mainframe, text="4", style="botones_numeros.TButton")
Button5 = ttk.Button(mainframe, text="5", style="botones_numeros.TButton")
Button6 = ttk.Button(mainframe, text="6", style="botones_numeros.TButton")
Button7 = ttk.Button(mainframe, text="7", style="botones_numeros.TButton")
Button8 = ttk.Button(mainframe, text="8", style="botones_numeros.TButton")
Button9 = ttk.Button(mainframe, text="9", style="botones_numeros.TButton")

#Aqui se crean los botones de Borrar, Borrrar_todo, parentesis y punto.
Button_borrar = ttk.Button(mainframe, text=chr(9003), style="botones_borrar.TButton")
Button_borrar_todo = ttk.Button(mainframe, text="C", style="botones_borrar.TButton")
Button_parentesis1 = ttk.Button(mainframe, text="(", style="botones_restantes.TButton")
Button_parentesis2 = ttk.Button(mainframe, text=")", style="botones_restantes.TButton")
Button_punto = ttk.Button(mainframe, text=".", style="botones_restantes.TButton")

#Aqui se crean los botones de opeaciones.
Button_division = ttk.Button(mainframe, text=chr(247), style="botones_restantes.TButton")
Button_multiplicacion = ttk.Button(mainframe, text="x", style="botones_restantes.TButton")
Button_resta = ttk.Button(mainframe, text="-", style="botones_restantes.TButton")
Button_suma = ttk.Button(mainframe, text="+", style="botones_restantes.TButton")
Button_pi = ttk.Button(mainframe, text="pi", style="botones_restantes.TButton")
Button_sin = ttk.Button(mainframe, text="sin", style="botones_restantes.TButton")
Button_cos = ttk.Button(mainframe, text="cos", style="botones_restantes.TButton")
Button_tan = ttk.Button(mainframe, text="tan", style="botones_restantes.TButton")
Button_ctan = ttk.Button(mainframe, text="ctan", style="botones_restantes.TButton")
Button_log = ttk.Button(mainframe, text="log", style="botones_restantes.TButton")
Button_exp = ttk.Button(mainframe, text="exp", style="botones_restantes.TButton")
Button_sqrt = ttk.Button(mainframe, text="sqrt", style="botones_restantes.TButton")
Button_cbrt = ttk.Button(mainframe, text="cbrt", style="botones_restantes.TButton")
Button_e = ttk.Button(mainframe, text="e", style="botones_restantes.TButton")
Button_igual = ttk.Button(mainframe, text="=", style="botones_restantes.TButton")
Button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="botones_restantes.TButton")
Button_x = ttk.Button(mainframe, text="x", style="botones_restantes.TButton")
Button_y = ttk.Button(mainframe, text="y", style="botones_restantes.TButton")
Button_potencia = ttk.Button(mainframe, text="^", style="botones_restantes.TButton")

#colocar botones en pantalla.
Button_pi.grid(column=0, row=2, sticky=(W, N, E, S))
Button_parentesis1.grid(column=1, row=2, sticky=(W, N, E, S))
Button_parentesis2.grid(column=2, row=2, sticky=(W, N, E, S))
Button_borrar_todo.grid(column=3, row=2, columnspan=2, sticky=(W, N, E, S))

Button_borrar.grid(column=5, row=2, sticky=(W, N, E, S))

Button7.grid(column=0, row=3, sticky=(W, N, E, S))
Button8.grid(column=1, row=3, sticky=(W, N, E, S))
Button9.grid(column=2, row=3, sticky=(W, N, E, S))
Button_sin.grid(column=3, row=3, sticky=(W, N, E, S))
Button_cos.grid(column=4, row=3, sticky=(W, N, E, S))
Button_division.grid(column=5, row=3, sticky=(W, N, E, S))

Button4.grid(column=0, row=4, sticky=(W, N, E, S))
Button5.grid(column=1, row=4, sticky=(W, N, E, S))
Button6.grid(column=2, row=4, sticky=(W, N, E, S))
Button_tan.grid(column=3, row=4, sticky=(W, N, E, S))
Button_ctan.grid(column=4, row=4, sticky=(W, N, E, S))
Button_multiplicacion.grid(column=5, row=4, sticky=(W, N, E, S))

Button1.grid(column=0, row=5, sticky=(W, N, E, S))
Button2.grid(column=1, row=5, sticky=(W, N, E, S))
Button3.grid(column=2, row=5, sticky=(W, N, E, S))
Button_log.grid(column=3, row=5, sticky=(W, N, E, S))
Button_exp.grid(column=4, row=5, sticky=(W, N, E, S))
Button_suma.grid(column=5, row=5, sticky=(W, N, E, S))

Button_e.grid(column=0, row=6, sticky=(W, N, E, S))
Button0.grid(column=1, row=6, sticky=(W, N, E, S)) #(columnspan=2, sticky=(W,E)) Con sticky agrega para anclar de lado a lado el 0.
Button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
Button_sqrt.grid(column=3, row=6, sticky=(W, N, E, S))
Button_cbrt.grid(column=4, row=6, sticky=(W, N, E, S))
Button_resta.grid(column=5, row=6, sticky=(W, N, E, S))


Button_potencia.grid(column=0, row=7, sticky=(W, N, E, S))
Button_x.grid(column=1, row=7, sticky=(W, N, E, S))
Button_y.grid(column=2, row=7, sticky=(W, N, E, S))
Button_raiz_cuadrada.grid(column=3, row=7, sticky=(W, N, E, S))
Button_igual.grid(column=4, row=7, columnspan=2, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-o>', TemaObscuro)

root, mainloop()
