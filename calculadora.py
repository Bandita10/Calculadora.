#Librerias.
from tkinter import *
from tkinter import ttk
#Para sacar la raiz cuadrada
import math


root = Tk()
root.title("Calculadora")
#Coordenadas de donde saldra la interfaz grafica.
root.geometry("+500+80")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

entrada1 = StringVar()
label_entrada1 = ttk.Lable(mainframe, textvariable=entrada1)
label_entrada1.grid(column=0, row=0)

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2)

#Aqui se crean los botones del 0 al 9.
Button0 = ttk.Button(mainframe, text="0")
Button1 = ttk.Button(mainframe, text="1")
Button2 = ttk.Button(mainframe, text="2")
Button3 = ttk.Button(mainframe, text="3")
Button4 = ttk.Button(mainframe, text="4")
Button5 = ttk.Button(mainframe, text="5")
Button6 = ttk.Button(mainframe, text="6")
Button7 = ttk.Button(mainframe, text="7")
Button8 = ttk.Button(mainframe, text="8")
Button9 = ttk.Button(mainframe, text="9")

#Aqui se crean los botones de Borrar, Borrrar_todo, parentesis y punto.
Button_borrar = ttk.Button(mainframe, text=chr(9003))
Button_borrar_todo = ttk.Button(mainframe, text="C")
Button_parentesis1 = ttk.Button(mainframe, text="(")
Button_parentesis2 = ttk.Button(mainframe, text=")")
Button_punto = ttk.Button(mainframe, text=".")

#Aqui se crean los botones de opeaciones.
Button_division = ttk.Button(mainframe, text=chr(247))
Button_multiplicacion = ttk.Button(mainframe, text="x")
Button_resta = ttk.Button(mainframe, text="-")
Button_suma = ttk.Button(mainframe, text="+")

Button_igual = ttk.Button(mainframe text="=")
Button_raiz_cuadrada = ttk.Button(mainframe text="√")

#colocar botones en pantalla.
Button_parentesis1.grid(column=0, row=2)
Button_parentesis2.grid(column=1, row=2)
Button_borrar_todo.grid(column=2, row=2)
Button_borrar.grid(column=3, row=2)

root, mainloop()

