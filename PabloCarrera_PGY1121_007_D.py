from funciones import * 

while True:
    limpiarPantalla()
    mostrarMenu()
    opc = seleccionarOpcion()
    if opc == 1:
        limpiarPantalla()
        if 0 not in array:
            print("Están todos los asientos ingresados, regrese mas tarde")
            mostrarArray(array)
            esperarTecla(True, 2)
            continue
        cantidad = solicitarCantidadEntradas()
        time.sleep(0.5)
        for x in range(cantidad):
            limpiarPantalla()
            while True:
                mostrarArray(array)
                fila = validarAsiento("fila")
                columna = validarAsiento("columna")
                if array[fila-1][columna-1] == 0:
                    break
                else:
                    print("No está disponible.")
            while True:
                rut = validarRut()
                if rut not in lista_ruts:
                    break
                else: 
                    print("Ese rut no está disponible.")
            if fila in(1,2):
                contadorPlat += 1
                acumuladorPlat += 120000
            elif fila in(3,4,5):
                contadorGold += 1
                acumuladorGold += 80000
            else:
                contadorSilver += 1
                acumuladorSilver += 50000
            lista_ruts.append(rut)
            lista_filas.append(fila)
            lista_columnas.append(columna)
            array[fila-1][columna-1] = 1
            print("¡La comprá se a realizado correctamente!")
            esperarTecla(True, 1)
    elif opc == 2:
        limpiarPantalla()
        if 0 not in array:
            print("Están todos los asientos ocupados, regrese mas tarde")
            mostrarArray(array)
        else:
            print("\tASIENTOS DISPONIBLES")
            mostrarArray(array)
        esperarTecla(True, 1)
    elif opc == 3:
        limpiarPantalla()
        if len(lista_ruts) == 0:
            print("Aún no se a registrado ningun ásistente")
            esperarTecla(True, 2)
            continue
        lista_ruts.sort()
        print("Los ásistentes hasta el momento son: ")
        for x in range(len(lista_ruts)):
            print(f"{x+1}: ", lista_ruts[x])
        esperarTecla(True, 1)
    elif opc == 4:
        limpiarPantalla()
        print(F"""
___________________________________________
|Tipo Entrada       | Cantidad  |    Total |
|Platinium $120.000 |   {contadorPlat}       |   {acumuladorPlat} 
|Gold      $80.000  |   {contadorGold}       |   {acumuladorGold} 
|Silver    $50.000  |   {contadorSilver}       |   {acumuladorSilver} 
|TOTAL              |   {contadorPlat+contadorGold+contadorSilver}       |   {acumuladorSilver+acumuladorGold+acumuladorPlat}
-------------------------------------------
        """)
        esperarTecla(True, 1)
    elif opc == 5:
        limpiarPantalla()
        salir(True, 2)
        break
limpiarPantalla()
print("\nNombre: Pablo Carrera\nRut: 20.560.792-7\nFecha: 06/07/2023\n")
