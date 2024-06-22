#Importar la libreria para trabajar la interfaz gráfica

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random
import tkinter.scrolledtext as st

#Funcion para determinar monedas ganadas o perdidas
def determinarMonedasGanadasYPerdidas(monedas, monedasFinales):
    mensajeMonedasfinales = ""
    if monedas > monedasFinales:
        mensajeMonedasfinales = "Has perdido " + str(monedas - monedasFinales) + " monedas"
        return mensajeMonedasfinales
    elif monedas < monedasFinales:
        mensajeMonedasfinales = "Has ganado " + str(monedasFinales - monedas) + " monedas"
        return mensajeMonedasfinales
    else:
        mensajeMonedasfinales = "No has ganado ni perdido monedas"
        return mensajeMonedasfinales

#Función para determinar el resultado de la tragamonedas
def determinarResultado(monedasGanadas):
    mensajeResultado = ""
    if monedasGanadas == 5:
        mensajeResultado = "¡Felicidades, ganaste 5 monedas!"
        return mensajeResultado
    elif monedasGanadas == 2:
        mensajeResultado = "¡Felicidades, ganaste 2 monedas!"
        return mensajeResultado
    else:
        mensajeResultado = "No tienes ningun acierto, ¡continua intentando!"
        return mensajeResultado
    
#Determina si el usuario gana monedas
def determinarMonedasGanadas(numero1, numero2, numero3):
    monedasObtenidas = 0
    if numero1 == numero2 and numero1 == numero3:
        monedasObtenidas = 5
        return monedasObtenidas
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        monedasObtenidas = 2
        return monedasObtenidas
    else:
        return monedasObtenidas


#Funcion que inicia la partida
def partida(monedas, continuarJuando):
    contador = 1    
    while continuarJuando == "SI" or monedas > 0:
        #Indica al usuario el numero de la partida
        monedas -= 1
        nivelPartida = "Partida: " + str(contador) + "\n"
        textResultados.insert(END, nivelPartida)
        #determinarResultado()
        #Se generan los números aleatorios
        numero1 = random.randint(1, 6)
        numero2 = random.randint(1, 6)
        numero3 = random.randint(1, 6)
        #Se muestran los números generados
        resultado = "los numeros son: " + str(numero1) + " - " + str(numero2) + " - " + str(numero3) + "\n"
        textResultados.insert(END, resultado)
        #Se determinan las monedas ganadas
        monedasGanadas = determinarMonedasGanadas(numero1, numero2, numero3)
        monedas = monedas + monedasGanadas
        #Se muestra el resultado de la partida
        mensajeResultado = determinarResultado(monedasGanadas) + "\n"
        textResultados.insert(END, mensajeResultado)
        monedasAcumuladas = "La cantidad de monedas acumuladas es " + str(monedas) + "\n"
        textResultados.insert(END, monedasAcumuladas)
        mensajeFinPartida = "La partida a terminado\n"
        if monedas > 0:            
            continuarJuando = simpledialog.askstring("Input", "¿Desea seguir jugando?, por favor difite SI/NO:")            
            if continuarJuando == "NO":
                textResultados.insert(END, mensajeFinPartida)                
                return monedas
        else:
            textResultados.insert(END, mensajeFinPartida) 
            return monedas    
        contador += 1

#Función para jugar
def principal():    
    textResultados.config(state="normal")
    valida = True
    mensajeError = "Por favor ingrese un número mayor a 0\n"
    while valida == True:        
        monedas = simpledialog.askstring("Input", "Ingrese la cantidad de monedas a jugar: ")
        print(monedas)
        if monedas :
            monedas = int(monedas)
            if monedas > 0:
                bJugar.config(state="disable")
                textoInicio = "El juego inicia con " + str(monedas) + " monedas\n"
                textResultados.insert(END, textoInicio)
                continuarJuando = "SI"
                monedasFinales = partida(monedas, continuarJuando)
                monedasFinJuego = determinarMonedasGanadasYPerdidas(monedas, monedasFinales) + "\n"
                textResultados.insert(END, monedasFinJuego)
                bJugar.config(state="normal")              
                valida = False
            else:
                textResultados.insert(END, mensajeError)                
        else:
            textResultados.insert(END, mensajeError)

    textResultados.config(state="disable")

#Interfaz Gráfica
raiz = Tk()
raiz.title("TRAGAMONEDAS")
raiz.resizable(0,0)

#Contenedor de los controles de usuario
ventana = Frame(raiz, bd=5, relief="sunken")
ventana.pack(padx=10, pady=10)

textInstrucciones = Text(ventana, width= 80,height = 5, padx = 5, pady= 5)
textInstrucciones.grid(row=1, column = 0, padx = 10, pady=5)
instrucciones = """Jugar a las maquinitas tragamonedas es una de las formas más populares de juegos de azar en el mundo y potencialmente, una de las más dañinas.

                       Bienvenidos y a jugar"""
textInstrucciones.insert(INSERT, instrucciones)
textInstrucciones.config(state="disable")

bJugar = Button(ventana, text="Iniciar Juego", command=principal)
bJugar.grid(row=2, column=0,padx=10, pady=10)

ventana1 = Frame(raiz, bd=5)
ventana1.pack(padx=10, pady=10)
'''
Investigue cómo funciona el área de Texto en Tkinter de python Text
'''
textResultados = st.ScrolledText(ventana, width= 90,height = 20,state="disable", padx = 5, pady= 5)
textResultados.grid(row=3,column = 0, pady = 10, padx = 10)

raiz.mainloop()


