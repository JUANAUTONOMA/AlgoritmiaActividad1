#Importar la libreria para trabajar la interfaz gráfica

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random
import tkinter.scrolledtext as st

#Funcion para determinar monedas ganadas o perdidas
def determinarMonedasGanadasYPerdidas(monedas, monedasFinales):
    if monedas > monedasFinales:
        return "Has perdido " + str(monedas - monedasFinales) + " monedas"
    elif monedas < monedasFinales:
        return "Has ganado " + str(monedasFinales - monedas) + " monedas"
    else:
        return "No has ganado ni perdido monedas"

#Función para determinar el resultado de la tragamonedas
def determinarResultado(monedasGanadas):
    if monedasGanadas == 5:
        return "¡Felicidades, ganaste 5 monedas!"
    elif monedasGanadas == 2:
        return "¡Felicidades, ganaste 2 monedas!"
    else:
        return "No tienes ningun acierto, ¡continua intentando!"
    
#Determina si el usuario gana monedas
def determinarMonedasGanadas(numero1, numero2, numero3):
    if numero1 == numero2 and numero1 == numero3:
        return 5
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return 2
    else:
        return 0


#Funcion que inicia la partida
def partida(monedas, continuarJuando):
    contador = 1    
    while continuarJuando == "SI" or monedas > 0:
        #Indica al usuario el numero de la partida
        monedas -= 1
        textResultados.insert(END, f"Partida {contador}\n")
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
        textResultados.insert(END, determinarResultado(monedasGanadas) + "\n")
        textResultados.insert(END, f"La cantidad de monedas acumuladas es {monedas}\n")
        if monedas > 0:            
            continuarJuando = simpledialog.askstring("Input", "¿Desea seguir jugando?, por favor difite SI/NO:")
            if continuarJuando == "NO":
                textResultados.insert(END, f"La partida a terminado\n")                
                return monedas
        else:
            textResultados.insert(END, f"La partida a terminado\n") 
            return monedas    
        contador += 1

#Función para jugar
def principal():    
    textResultados.config(state="normal")
    while True:        
        monedas = simpledialog.askstring("Input", "Ingrese la cantidad de monedas a jugar: ")
        if monedas :
            monedas = int(monedas)
            if monedas > 0:
                bJugar.config(state="disable")
                textResultados.insert(END, f"El juego inicia con " + str(monedas) + " monedas\n")
                continuarJuando = "SI"
                monedasFinales = partida(monedas, continuarJuando) 
                textResultados.insert(END, determinarMonedasGanadasYPerdidas(monedas, monedasFinales) + "\n")
                bJugar.config(state="normal")              
                break
            else:
                textResultados.insert(END, f"Por favor ingrese un número mayor a 0\n")                
        else:
            textResultados.insert(END, f"Por favor ingrese un número mayor a 0\n")

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


