import numpy
import time
import msvcrt
import os
lista_ruts = []
lista_filas = []
lista_columnas = []
lista_asistentes = []
array = numpy.zeros((10,10), int)

contadorPlat = 0
contadorGold = 0
contadorSilver = 0

acumuladorPlat = 0
acumuladorGold = 0
acumuladorSilver = 0

def limpiarPantalla():
    os.system('cls')

def esperarTecla(p_bool: bool, p_num: int):
    bool = p_bool
    if bool == True:
        time.sleep(p_num)
    print("Pulse una tecla para continuar")
    msvcrt.getch()

def validarRut():
    while True:
        try:
            rut = int(input("Íngrese el rut de la ubicación (sin puntos ni dígito verificador): "))
            if rut > 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! Debe registrar un rut disponible (sin puntos ni dígito verificador)")
        except:
            print("ERROR! Debe registrar un rut disponible (sin puntos ni dígito verificador)")

def solicitarCantidadEntradas():
    while True:
        try:
            cantidad = int(input("¿Cuantas entradas vá a comprar? (Disponible de 1 a 3): "))
            if cantidad in (1,2,3):
                return cantidad
            else:
                print("ERROR! Debe registrar una cantidad de entradas disponible, entre 1 y 3")
        except:
            print("ERROR! Debe registrar una cantidad de entradas disponible, entre 1 y 3")

def mostrarArray(p_array):
    print("\tConcierto Michael Jam")
    for x in range(10):
        if x == 9:
            print(f"Fila {x+1}:", end=" ")
        else:
            print(f"Fila {x+1}: ", end=" ")
        for i in range(10):
            print(p_array[x][i], end=" ")
        if x == 1:
            print("<- $120.000", end=" ")
        if x == 4:
            print("<- $80.000", end=" ")
        if x == 9:
            print("<- $50.000", end=" ")
        print(" ")
    print("Columna: 1 2 3 4 5 6 7 8 9 10")

def validarAsiento(p_str: str):
    while True:
        try:
            asiento = int(input(f"Íngrese una {p_str}: "))
            if asiento > 0 and asiento <= 10:
                return asiento
            else:
                print(f"ERROR! Debe registrar una {p_str} disponible")
        except:
            print(f"ERROR! Debe registrar una {p_str} disponible")

def salir(p_bool: bool, p_num: int):
    print("Usted saldrá de la aplicación")
    bool = p_bool
    if bool == True:
        time.sleep(p_num)
    print("Pulse una tecla para continuar")
    msvcrt.getch()

def mostrarMenu():
    print("""
**Venta de entradas Michael Jam**

1. Comprar entradas
2. Mostrar ubicaciones de asientós disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
    """)
def seleccionarOpcion():
    while True:
        try:
            userOption = int(input("Seleccione una opción: "))
            if userOption in(1,2,3,4,5):
                return userOption
            else:
                print("ERROR! debe registrar una opción disponible (1,2,3,4,5)")
        except:
            print("ERROR! debe registrar una opción disponible (1,2,3,4,5)")


