from tkinter import *
import os
os.system("cls")


ventana = Tk()
ventana.title("Calculadora")
ind = 0

#Funciones
def click_boton(valor):
    global ind
    texto_e.insert(ind, valor)
    ind += 1
#borrar
def limpiar():
    texto_e.delete(0, END)
    ind = 0
#operaciones
def operacion():
    ecua = texto_e.get()
    resultado = eval(ecua)
    texto_e.delete(0, END)
    texto_e.insert(0, resultado)
    ind = 0

#Entrada de texto
texto_e = Entry(ventana, font = ("Georgia 20"))
texto_e.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 5, height = 2, command = lambda: click_boton(0))

boton_limpiar = Button(ventana, text = "AC", width = 30, height = 2, command = lambda: limpiar())
boton_punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))

boton_division = Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_multiplicacion = Button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_suma = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_resta = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_igual = Button(ventana, text = "=", width = 18, height = 2, command = lambda: operacion())

#Botones en pantalla
#Fila 1
boton_limpiar.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
boton_division.grid(row = 1, column = 3, padx = 5, pady = 5)
#Fila 2
boton1.grid(row =2 , column =0, padx = 5, pady = 5)
boton2.grid(row =2 , column = 1, padx = 5, pady = 5)
boton3.grid(row =2 , column = 2, padx = 5, pady = 5)
boton_multiplicacion.grid(row =2 , column = 3, padx = 5, pady = 5)
#Fila 3
boton4.grid(row =3 , column = 0, padx = 5, pady = 5)
boton5.grid(row =3 , column = 1, padx = 5, pady = 5)
boton6.grid(row =3 , column = 2, padx = 5, pady = 5)
boton_suma.grid(row =3 , column = 3, padx = 5, pady = 5)
#Fila 4
boton7.grid(row =4 , column = 0, padx = 5, pady = 5)
boton8.grid(row =4 , column = 1, padx = 5, pady = 5)
boton9.grid(row =4 , column = 2, padx = 5, pady = 5)
boton_resta.grid(row =4 , column =3 , padx = 5, pady = 5)
#Fila 5
boton0.grid(row =5 , column = 0, padx = 5, pady = 5)
boton_punto.grid(row =5 , column = 1, padx = 5, pady = 5)
boton_igual.grid(row =5 , column =2 , columnspan =2, padx = 5, pady = 5)


ventana.mainloop()