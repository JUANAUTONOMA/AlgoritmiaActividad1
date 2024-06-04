'''
Autor: Escriba aquí su nombre y apellido completo
Código: Escriba aquí su código de estudiante
Fecha: Escriba aquí la fecha de realización
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk



def salir():
    raiz.destroy()
    
def borrar():
    direccionCombo.set("")
    numeroPosTb.delete(0, END)
    
    varposInicial.set("")
    varposFinal.set("")
    direccionCombo.current(0)

def DeterminarPosicionFinal(direccion, posicion_actual, UnidadesDeMovimiento, largo_maximo, ancho_maximo):
    if isinstance(posicion_actual, str):
        posicion_actual = posicion_actual.replace("(", "").replace(")", "").split(',')
        posicion_actual = tuple(map(int, posicion_actual))
    x_actual, y_actual = posicion_actual

    if direccion == "Arriba":
        nueva_y = y_actual + UnidadesDeMovimiento
        if nueva_y <= largo_maximo / 2:
            return (x_actual, nueva_y)
    elif direccion == "Abajo":
        nueva_y = y_actual - UnidadesDeMovimiento
        if nueva_y >= -largo_maximo / 2:
            return (x_actual, nueva_y)
    elif direccion == "Derecha":
        nueva_x = x_actual + UnidadesDeMovimiento
        if nueva_x <= ancho_maximo / 2:
            return (nueva_x, y_actual)
    elif direccion == "Izquierda":
        nueva_x = x_actual - UnidadesDeMovimiento
        if nueva_x >= -ancho_maximo / 2:
            return (nueva_x, y_actual)    
      

    root = tk.Tk()
    root.withdraw() 
    messagebox.showerror("Error", "Movimiento fuera de límites")
    root.destroy()

    return posicion_actual
    
def CalcularMovimiento():
    DireccionDeMovimiento = direccionCombo.get()
    if posInicialTb.get() == "":
        posicion_actual = (0,0)
    else:
        posicion_actual = posFinalTb.get()
    print(posicion_actual)
    if numeroPosTb.get() == "":
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "El campo de número de posiciones no puede estar vacío")
        root.destroy()
        return
    UnidadesDeMovimiento = int(numeroPosTb.get())
    largo_maximo = varLargo.get()
    ancho_maximo = varAncho.get()
    
    PosicionFinal = DeterminarPosicionFinal(DireccionDeMovimiento, posicion_actual, UnidadesDeMovimiento, largo_maximo, ancho_maximo)

    varposInicial.set(str(posicion_actual))
    varposFinal.set(str(PosicionFinal))    


#Interfaz gráfica
raiz = Tk()
raiz.title("Control Robot")
raiz.resizable(0,0)


#Contenedor componentes de interfaz gráfica
contenedor1 = LabelFrame(raiz, text="Datos", bd = 3)
contenedor1.pack(padx = 5, pady = 5)

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




