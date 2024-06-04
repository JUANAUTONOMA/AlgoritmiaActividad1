'''
Autor: Juan Pablo Lenis Rebolledo, Nicolas Romero Guarnizo
Código: 2235347, 2240393
Fecha: 04/06/2024
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


#Boton para salir de la aplicación
def salir():
    raiz.destroy()

#Boton para borrar los campos de texto   
def borrar():
    direccionCombo.set("")
    numeroPosTb.delete(0, END)
    
    varposInicial.set("")
    varposFinal.set("")
    direccionCombo.current(0)

#Función para determinar la posición final del robot
def DeterminarPosicionFinal(direccion, posicionInicial, UnidadesDeMovimiento, largo_maximo, ancho_maximo):
    #Si la posición actual es un string, se convierte a tupla
    if isinstance(posicionInicial, str):
        posicionInicial = posicionInicial.replace("(", "").replace(")", "").split(',')
        posicionInicial = tuple(map(int, posicionInicial))
    #Se obtienen las coordenadas actuales
    x_actual, y_actual = posicionInicial
    nuevaPosicion = (0,0)
    #Se determina la nueva posición del robot
    if direccion == "Arriba":
        nueva_y = y_actual + UnidadesDeMovimiento
        if nueva_y <= largo_maximo / 2:
            nuevaPosicion = (x_actual, nueva_y)
            return (nuevaPosicion)
    elif direccion == "Abajo":
        nueva_y = y_actual - UnidadesDeMovimiento
        if nueva_y >= -largo_maximo / 2:
            nuevaPosicion = (x_actual, nueva_y)
            return (nuevaPosicion)
    elif direccion == "Derecha":
        nueva_x = x_actual + UnidadesDeMovimiento
        if nueva_x <= ancho_maximo / 2:
            nuevaPosicion = (nueva_x, y_actual)
            return (nuevaPosicion)
    elif direccion == "Izquierda":
        nueva_x = x_actual - UnidadesDeMovimiento
        if nueva_x >= -ancho_maximo / 2:
            nuevaPosicion = (nueva_x, y_actual)
            return (nuevaPosicion)    
      
    #Si el movimiento es inválido, se muestra un mensaje de error y se retorna la posición actual
    root = tk.Tk()
    root.withdraw() 
    messagebox.showerror("Error", "Movimiento fuera de límites")
    root.destroy()

    return (posicionInicial)

#Función para calcular el movimiento del robot    
def CalcularMovimiento():
    #Se obtienen los valores del campo direccionCombo
    DireccionDeMovimiento = direccionCombo.get()
    #Determina si el campo posInicialTb está vacío asigna el valor (0,0) a la variable posicionInicial en caso de que tenga un valor asignado se asigna el valor de posInicialTb a la variable posicionInicial
    if posInicialTb.get() == "":
        posicionInicial = (0,0)
    else:
        posicionInicial = posFinalTb.get()
    #Si el campo numeroPosTb está vacío se muestra un mensaje de error
    if numeroPosTb.get() == "":
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "El campo de número de posiciones no puede estar vacío")
        root.destroy()
        return
    UnidadesDeMovimiento = int(numeroPosTb.get())

    #Se obtienen los valores de los campos largoTb y anchoTb
    largo_maximo = varLargo.get()
    ancho_maximo = varAncho.get()
    
    #Se determina la posición final del robot
    PosicionFinal = DeterminarPosicionFinal(DireccionDeMovimiento, posicionInicial, UnidadesDeMovimiento, largo_maximo, ancho_maximo)

    #Se actualizan los campos posInicialTb y posFinalTb
    varposInicial.set(str(posicionInicial))
    varposFinal.set(str(PosicionFinal))    


#Interfaz gráfica
raiz = Tk()
raiz.title("Control Robot")
raiz.resizable(0,0)


#Contenedor componentes de interfaz gráfica
contenedor1 = LabelFrame(raiz, text="Datos", bd = 3)
contenedor1.pack(padx = 5, pady = 5)

#Componentes de la interfaz gráfica
direccionLabel = Label(contenedor1, text="Dirección del movimiento: ").grid(row=0, column=0, sticky = "w", padx=5, pady=5)
direccionCombo = ttk.Combobox(contenedor1, state="readonly",width=12,values=["Arriba","Abajo","Derecha", "Izquierda"])
direccionCombo.grid(row=0,column=1,padx=5, pady=5)
direccionCombo.current(0)
numeroPosLabel = Label(contenedor1, text="Número de posiciones: ").grid(row=1, column=0, sticky = "w", padx=5, pady=5)
numeroPosTb = Entry(contenedor1, width=10)
numeroPosTb.grid(row=1,column=1,padx=5, pady=5, sticky="w")

largoLabel = Label(contenedor1, text="Largo del plano: ").grid(row=4, column=0, sticky="w", padx=5, pady=5)
varLargo = IntVar()
varLargo.set(50)
largoTb = Entry(contenedor1, textvariable=varLargo, state="readonly",width=10)
largoTb.grid(row=4, column=1, padx=5, pady=5, sticky="w")
anchoLabel = Label(contenedor1, text="Ancho del plano: ").grid(row=4, column=2, sticky="w", padx=5, pady=5)
varAncho = IntVar()
varAncho.set(100)
anchoTb = Entry(contenedor1, textvariable=varAncho, state="readonly", width=10)
anchoTb.grid(row=4, column=3,columnspan=2, padx=5, pady=5, sticky="w")
posInicialLabel = Label(contenedor1, text="Posición inicial: ").grid(row=5, column=0, sticky="w", padx=5, pady=5)
varposInicial = StringVar()
posInicialTb = Entry(contenedor1, textvariable=varposInicial, state="readonly", width=10)
posInicialTb.grid(row=5, column=1,columnspan=2, padx=5, pady=5, sticky="w")
posFinalLabel = Label(contenedor1, text="Posición final: ").grid(row=5, column=2, sticky="w", padx=5, pady=5)
varposFinal = StringVar()
posFinalTb = Entry(contenedor1, textvariable=varposFinal, state="readonly", width=10)
posFinalTb.grid(row=5, column=3,columnspan=2, padx=5, pady=5, sticky="w")


#Contenedor de los botones
contenedor2 = LabelFrame(raiz, text="",bd =3)
contenedor2.pack(padx = 5, pady = 5)


botonIniciar = Button(contenedor2,text="Iniciar",width=10, command=CalcularMovimiento).grid(row=0, column=0, padx = 5, pady=5)
botonBorrar = Button(contenedor2,text="Borrar",width=10, command=borrar).grid(row=0, column=1,padx = 5, pady=5)
botonSalir = Button(contenedor2,text="Salir",width=10, command=salir).grid(row=0, column=2,padx = 5, pady=5)

raiz.mainloop()




