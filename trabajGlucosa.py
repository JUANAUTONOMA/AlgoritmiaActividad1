from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.scrolledtext as st

def obtenerMedicionPorComida(mediciones):
    mediciones_antes_desayuno = []
    mediciones_despues_desayuno = []
    mediciones_antes_almuerzo = []
    mediciones_despues_almuerzo = []
    mediciones_antes_cena = []
    mediciones_despues_cena = []

    for i in range(len(mediciones)):
        if i % 6 == 0:
            mediciones_antes_desayuno.append(mediciones[i])
        elif i % 6 == 1:
            mediciones_despues_desayuno.append(mediciones[i])
        elif i % 6 == 2:
            mediciones_antes_almuerzo.append(mediciones[i])
        elif i % 6 == 3:
            mediciones_despues_almuerzo.append(mediciones[i])
        elif i % 6 == 4:
            mediciones_antes_cena.append(mediciones[i])
        elif i % 6 == 5:
            mediciones_despues_cena.append(mediciones[i])

    return (mediciones_antes_desayuno, mediciones_despues_desayuno, 
            mediciones_antes_almuerzo, mediciones_despues_almuerzo, 
            mediciones_antes_cena, mediciones_despues_cena)

def determinarMayorNivelDC(*args):
    return max(max(arg) for arg in args if arg)

def determinarMenorNivelAC(*args):
    return min(min(arg) for arg in args if arg)

def generarReporteGlucosaAlto(*args):
    alto_count = sum(1 for medicion in args for valor in medicion if valor > 140)
    return f'Número de mediciones de glucosa altas: {alto_count}\n'

def generarReporteGlucosaNormalDespuesDeComer(mediciones):
    normal_count = sum(1 for valor in mediciones if 70 <= valor <= 140)
    return f'Número de mediciones de glucosa normales después de la cena: {normal_count}\n'

def determinarNGPromedioAD(mediciones):
    return sum(mediciones) / len(mediciones) if mediciones else 0

def generarReporteGNAlto(*args):
    reporte = ''
    for i, mediciones in enumerate(args):
        if i == 0 or i == 1:
            comida = 'desayuno'
        elif i  == 2 or i == 3:
            comida = 'almuerzo'
        elif i == 4 or i == 5:
            comida = 'cena'
        if i == 0 or i == 2 or i == 4:
            momento = 'antes'
        elif i == 1 or i == 3 or i == 5:
            momento = 'después'
        for valor in mediciones:
            if valor > 140:
                reporte += f'{valor} {momento} del {comida}\n'
    return reporte   


def generarReporteGNNormalDC(mediciones):
    reporte = ''
    for valor in mediciones:
        if valor >= 70 and valor <= 140:
            reporte += f'{valor}\n'
    return reporte
   

def generarReporte(mediciones):
    (mediciones_antes_desayuno, mediciones_despues_desayuno, 
     mediciones_antes_almuerzo, mediciones_despues_almuerzo, 
     mediciones_antes_cena, mediciones_despues_cena) = obtenerMedicionPorComida(mediciones)

    mayor_nivel_despues_comidas = determinarMayorNivelDC(
        mediciones_despues_desayuno, mediciones_despues_almuerzo, mediciones_despues_cena)
    menor_nivel_antes_comidas = determinarMenorNivelAC(
        mediciones_antes_desayuno, mediciones_antes_almuerzo, mediciones_antes_cena)
    reporte_glucosa_alta = generarReporteGlucosaAlto(
        mediciones_antes_desayuno, mediciones_despues_desayuno, 
        mediciones_antes_almuerzo, mediciones_despues_almuerzo, 
        mediciones_antes_cena, mediciones_despues_cena)
    mediciones_glucosa_alta = generarReporteGNAlto(mediciones_antes_desayuno, mediciones_despues_desayuno,
                                                mediciones_antes_almuerzo, mediciones_despues_almuerzo,
                                                mediciones_antes_cena, mediciones_despues_cena)
    reporte_glucosa_normal_despues_cena = generarReporteGlucosaNormalDespuesDeComer(mediciones_despues_cena)
    mediciones_glucosa_normal_despues_cena = generarReporteGNNormalDC(mediciones_despues_cena)
    promedio_antes_desayuno = determinarNGPromedioAD(mediciones_antes_desayuno)

    reporte = (f'El mayor nivel de glucosa después de comidas es: {mayor_nivel_despues_comidas}\n'
               f'El menor nivel de glucosa antes de comidas es: {menor_nivel_antes_comidas}\n'
               f'Las mediciones con nivel alto son: \n{mediciones_glucosa_alta}'
               f'{reporte_glucosa_alta}'               
               f'Las mediciones con nivel normal despues de la cena son: \n{mediciones_glucosa_normal_despues_cena}'
               f'{reporte_glucosa_normal_despues_cena}'               
               f'El promedio de los niveles de glucosa antes del desayuno es: {promedio_antes_desayuno}\n')

    return reporte

def principal():
    resultados.config(state='normal')    
    mediciones = []
    valida = True
    mensajeErrorNombre = "Por favor ingrese un nombre de paciente\n"
    while valida == True:
        nombrePaciente = simpledialog.askstring("Input", "Ingrese el nombre del paciente: ")
        if nombrePaciente :
            agregar_dias = simpledialog.askstring("input", "Desea agregar mediciones hoy? SI/NO: ").upper()
            while agregar_dias == 'SI':
                for _ in range(6):
                    medicion = simpledialog.askstring("input", "Ingrese su medición de glucosa: ")
                    if medicion:
                        mediciones.append(int(medicion))
                agregar_dias = simpledialog.askstring("input", "Desea agregar mediciones hoy? SI/NO: ").upper()
            reporte = generarReporte(mediciones)
            resultados.insert(END, "Paciente: " + nombrePaciente + "\n")
            resultados.insert(END, reporte)
            break
        else:
            messagebox.showerror("Error", mensajeErrorNombre)

    
    resultados.config(state='disabled')

def salir():
    raiz.destroy()

def borrar():
    resultados.config(state="normal")
    resultados.delete("1.0", "end")
    resultados.config(state="disabled")

# Interfaz Gráfica de usuario
raiz = Tk()
raiz.resizable(0, 0)
raiz.title("Centro de Salud - Salud y Bienestar")

# Contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10, padx=10)

iniciarB = Button(marco1, text="Iniciar Toma", command=principal)
iniciarB.grid(row=1, column=0, padx=3, pady=3)
salirB = Button(marco1, text="Salir", width=12, command=salir)
salirB.grid(row=1, column=1, padx=3, pady=3)
borrarB = Button(marco1, text="Borrar", width=12, command=borrar)
borrarB.grid(row=1, column=2, padx=3, pady=3)

# Contenedor Resultados
marco2 = LabelFrame(raiz, text="Resultados toma de niveles de glucosa")
marco2.config(bd=3, relief="sunken", padx=15, pady=15)
marco2.pack(pady=10, padx=10)

resultados = st.ScrolledText(marco2, width=100, height=10)
resultados.grid(row=0, column=0, pady=10, padx=10)
resultados.config(state='disabled')

raiz.mainloop()