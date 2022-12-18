import re
import operator
import os
import time
import sys

"""-----------Aqui se capturan los datos del txt y se los muestra por pantalla-----------"""


def captura_datos(f, cont, procesos, ti_total):
    for line in f:
        result = re.search(r"[ ]*(\d*.*),[ ]*(\d*.*),[ ]*(\d*.*),[ ]*(\d*.*),", line)
        if result is None:
            pass
        else:
            cont += 1
            """ ID:[TAM,TA,TI] """
            try:
                int(result.group(1))
                int(result.group(2))
                int(result.group(3))
                int(result.group(4))
            except:
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("Se encontraron letras entre los datos, verifique los datos e intente nuevamente")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                input("Presione una tecla para continuar: ")
                exit()
            procesos[result.group(1)] = [result.group(2), result.group(3), result.group(4)]
    print()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("Este es un script creado para simular la asignación de memoria usando Worst-Fit y SJF")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print()
    input("Presione una tecla para ver los procesos cargados: ")
    print("+--------+--------+--------+--------+")
    print("|ID      |TAM(Kb) |TA      |TI      |")
    print("+--------+--------+--------+--------+")
    for key, value in procesos.items():
        cadena = "|{:<8}|{:<8}|{:<8}|{:<8}|".format(key, value[0], value[1], value[2])
        ti_total += int(value[2])
        print(cadena)
        print("+--------+--------+--------+--------+")
    print("|TOTAL:  |        |        |", ti_total, "    |")
    print("+--------+--------+--------+--------+")
    print()
    if ti_total==0:
        print()
        input("No se encontró ningún proceso cargado, presione enter para finalizar.. ")
        exit()
    input("Presione una tecla para ver como se verá la memoria: ")
    print()


    value1 = "60K"
    value2 = "120K"
    value3 = "250K"
    SO = "100K SO"

    cadena1 = "|{:<8}|".format(value1)
    cadena2 = "|{:<8}|".format(value2)
    cadena3 = "|{:<8}|".format(value3)
    cadena4 = "|{:<8}|".format(SO)

    print("+--------+")
    print(cadena1)
    print("+--------+")
    print(cadena2)
    print("+--------+")
    print(cadena3)
    print("+--------+")
    print(cadena4)
    print("+--------+")
    print("+--------+")
    return (procesos, ti_total)


"""-----------------------------------------------------------------------------------------"""

"""-------------------------Mostrar instancia----------------------------"""


def imprimir_instancia(i):
    if str(opcion) == "N" or str(opcion) == "n":
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("En 10 segundos se mostrará el siguiente cambio")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        for u in range(10, 0, -1):
            sys.stdout.write(str(u) + ' ')
            sys.stdout.flush()
            time.sleep(1)
        os.system('cls')
        print()
        print()
        print("//--//--//--//--//--//--//")
        print("En el instante:",i+1, end=" ")
        print()
        print("//--//--//--//--//--//--//")
        print()
    else:
        print()
        input("Presione una tecla para continuar... ")
        print()
        os.system('cls')
        print("//--//--//--//--//")
        print("En el instante:",i+1, end=" ")
        print()
        print("//--//--//--//--// ")
        print()




"""----------------------------------------------------------------------"""

"""-------------------------Mostrar estados----------------------------"""
def imprimir_memoria(estado4,memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3):
    print("Memoria:")
    value1 = str(memoria[2]) + "K"
    value2 = str(memoria[1]) + "K"
    value3 = str(memoria[0]) + "K"
    SO = "100K SO"

    if (memoria[2] != 60):
        value1 = value1 + " ID: " + str(proceso_en_memoria_3)

    if (memoria[1] != 120):
        value2 = value2 + " ID: " + str(proceso_en_memoria_2)

    if (memoria[0] != 250):
        value3 = value3 + " ID: " + str(proceso_en_memoria_1)

    lista = list(estado4.keys())

    if lista[0] == proceso_en_memoria_3:
        cadena1 = "|{:<10}| En ejecucion".format(value1)
    else:
        cadena1 = "|{:<10}|".format(value1)

    if lista[0] == proceso_en_memoria_2:
        cadena2 = "|{:<10}| En ejecucion".format(value2)
    else:
        cadena2 = "|{:<10}|".format(value2)

    if lista[0] == proceso_en_memoria_1:
        cadena3 = "|{:<10}| En ejecucion".format(value3)
    else:
        cadena3 = "|{:<10}|".format(value3)

    cadena4 = "|{:<10}|".format(SO)

    print("+----------+")
    print(cadena1)
    print("+----------+")
    print(cadena2)
    print("+----------+")
    print(cadena3)
    print("+----------+")
    print(cadena4)
    print("+----------+")


def imprimir_estados(estado1, estado2, estado3, estado4, estado5, memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3):
    print("Estado Nuevo:", list(estado1.keys()))
    print("---------------------------------")
    print("Estado Listo y Suspendido:", list(estado2.keys()))
    print("---------------------------------")
    print("Estado Listo:", list(estado3.keys()))
    for key, value in estado3.items():
        print("     -Proceso",key,"con TI:",value[2])
    print("---------------------------------")
    print("Estado Ejecucion:", list(estado4.keys()))
    print("---------------------------------")

    terminado=list(estado5.keys())
    try:
        print("Estado Terminado: El proceso",terminado[-1],"fué el ultimo proceso en salir")
        print("-------------------------------------------------------------")
    except:
        err=0
    print()
    imprimir_memoria(estado4,memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)

"""--------------------------------------------------------------------"""
"""---------------Aqui se definen las variables que seran usadas--------------"""
procesos = {}
cont = 0
f = open("Datos.txt", "r")
grado_multi = 0
ti_total = 0
memoria = [250, 120, 60]  # La primera es el SO
proceso_en_memoria_1=0
proceso_en_memoria_2=0
proceso_en_memoria_3=0

lista_ti=[]
estado_nuevo = {}
estado_ls = {}
estado_listo = {}
estado_ejecucion = {}
estado_terminado = {}
aux={}
p=""
proceso_a_listo = {}
proceso_a_listo2 = {}
proceso_a_listo3 = {}

proceso_a_ejec = {}
"""--------------------------------------------------------------------------"""

"""........................CÓDIGO............................."""

procesos, ti_total = captura_datos(f, cont, procesos, ti_total)  # CAPTURA DE DATOS Y MUESTRA

y = dict(sorted(procesos.items(), key=lambda x: (x[1])))  # ORDENO PROCESOS POR TA

for key,value in y.items():
    if (int(key) < 0):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Se encontró un proceso con un ID menor a 0, corrija el error y ejecute nuevamente")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()
        input("Presione una tecla para continuar: ")
        exit()

    if (int(value[0]) > 250):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Se encontró un proceso con un tamaño (TAM) mayor a 250, corrija el error y ejecute nuevamente")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()
        input("Presione una tecla para continuar: ")
        exit()

    if (int(value[0]) < 0):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Se encontró un proceso con un tamaño (TAM) menor a 0, corrija el error y ejecute nuevamente")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()
        input("Presione una tecla para continuar: ")
        exit()

    if (int(value[2]) < 1):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Se encontró un proceso con un TI menor a 0, corrija el error y ejecute nuevamente")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()
        input("Presione una tecla para continuar: ")
        exit()

    if (int(value[1]) < 0):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Se encontró un proceso con un tiempo de acceso (TA) menor a 0, corrija el error y ejecute nuevamente")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()
        input("Presione una tecla para continuar: ")
        exit()


print()
print("//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//")
print("Debajo de aquí se mostrarán los instantes donde un cambio se produce")
print("//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//")
print()

opcion=input("¿Desea mostrar los resultados presionando ENTER? Y/N : ")
opcion=str(opcion)


os.system('cls')

if (opcion=="n" or opcion=="N"):
    print()
    input("Se mostrarán los procesos cada 10 segundos, presione una tecla para continuar.. ")
    print()

if cont > 10:  # MAS DE 10 PROCESOS NO PUEDEN SER TRATADOS (ASI ES LA CONSIGNA)
    print("\n ERROR -- La cantidad de procesos es mayor a 10, volver a cargar datos..")
    exit()
else:  # SI NO SON MAS DE 10

    for i in range(ti_total):  # ITERACION DE LAS INSTANCIAS
        for key, value in y.items():  # ITERACION DE CADA PROCESO

            """carga NUEVO (N)"""
            if (y[key][1]) == str(i):  # Si el TA es en esta instancia
                estado_nuevo[key] = y[key]  # y[key] es el proceso actual

        """carga LISTO/SUSPENDIDO (L/S)"""
        for k2, v2 in estado_nuevo.items():
            grado_multi = (len(estado_ls) + len(estado_listo) + len(estado_ejecucion))
            if grado_multi <= 4:  # Si hay lugar de multi, entra en L/S
                estado_ls[k2] = estado_nuevo[k2]
                grado_multi += 1  # Se incrementa el nivel de multiprogramación

        for k2, v2 in estado_ls.items():
            if k2 in estado_nuevo.keys():
                del estado_nuevo[k2]

        """carga LISTO (L) """
        ti_menor = 100
        ti_menor2 = 100
        ti_menor3 = 100

        """SELECCIÓN DE CANDIDATOS PARA ENTRAR A LISTO"""
        proceso_a_listo.clear()
        for k, v in estado_ls.items(): # ITERA SOBRE LOS LISTO Y SUSPENDIDO Y ELIGE 1 (EL QUE MENOR TI TIENE)
            if int(estado_ls[k][2]) < int(ti_menor):
                ti_menor = int(estado_ls[k][2])
                proceso_a_listo.clear()
                proceso_a_listo[k] = estado_ls[k]
                indice = k

        proceso_a_listo2.clear()
        for k, v in estado_ls.items(): # ITERA SOBRE LOS LISTO Y SUSPENDIDO Y ELIGE OTRO (EL 2 QUE MENOR TI TIENE)
            if int(estado_ls[k][2]) < int(ti_menor2) and int(estado_ls[k][2]) != int(ti_menor):
                ti_menor2 = int(estado_ls[k][2])
                proceso_a_listo2.clear()
                proceso_a_listo2[k] = estado_ls[k]
                indice2 = k

        proceso_a_listo3.clear()
        for k, v in estado_ls.items(): # ITERA SOBRE LOS LISTO Y SUSPENDIDO Y ELIGE OTRO (EL 3 QUE MENOR TI TIENE)
            if int(estado_ls[k][2]) < int(ti_menor3) and int(estado_ls[k][2]) != int(ti_menor) and int(estado_ls[k][2]) != int(ti_menor2):
                ti_menor3 = int(estado_ls[k][2])
                proceso_a_listo3.clear()
                proceso_a_listo3[k] = estado_ls[k]
                indice3 = k


        """---------------------------------------------------"""

        """TRATA PRIMER CANDIDATO PARA ENTRAR A LISTO"""
        try:
            if (int(memoria[0]) == 250) and (int(proceso_a_listo[indice][0]) <= int(
                    memoria[0])):  # SI LA PARTICION [O] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE Y TIENE ESPACIO SUFICIENTE
                memoria[0] -= int(proceso_a_listo[indice][0])
                estado_listo[indice] = proceso_a_listo[indice]
                estado_listo[indice].append(0)
                proceso_en_memoria_1=indice
                proceso_a_listo.clear()
                try:
                    del estado_ls[indice]
                except:
                    err = 1
            else:
                if (int(memoria[1]) == 120) and (int(proceso_a_listo[indice][0]) <= int(
                        memoria[1])):  # SI LA PARTICION [1] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE Y TIENE ESPACIO SUFICIENTE
                    memoria[1] -= int(proceso_a_listo[indice][0])
                    estado_listo[indice] = proceso_a_listo[indice]
                    estado_listo[indice].append(1)
                    proceso_en_memoria_2 = indice
                    proceso_a_listo.clear()
                    try:
                        del estado_ls[indice]
                    except:
                        err = 1

                else:
                    if (int(memoria[2]) == 60) and (int(proceso_a_listo[indice][0]) <= int(
                            memoria[2])):  # SI LA PARTICION [2] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE Y TIENE ESPACIO SUFICIENTE
                        memoria[2] -= int(proceso_a_listo[indice][0])
                        estado_listo[indice] = proceso_a_listo[indice]
                        estado_listo[indice].append(2)
                        proceso_en_memoria_3 = indice
                        proceso_a_listo.clear()
                        try:
                            del estado_ls[indice]
                        except:
                            err = 1

        except:
            err=1
        """---------------------------------------------------"""

        """TRATA SEGUNDO CANDIDATO PARA ENTRAR A LISTO"""
        try:
            if (int(memoria[0]) == 250) and (int(proceso_a_listo2[indice2][0]) <= int(
                    memoria[0])):  # SI LA PARTICION [O] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                memoria[0] -= int(proceso_a_listo2[indice2][0])
                estado_listo[indice2] = proceso_a_listo2[indice2]
                estado_listo[indice2].append(0)
                proceso_en_memoria_1 = indice2
                try:
                    del estado_ls[indice2]
                except:
                    err = 1
            else:
                if (int(memoria[1]) == 120) and (int(proceso_a_listo2[indice2][0]) <= int(
                        memoria[1])):  # SI LA PARTICION [1] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                    memoria[1] -= int(proceso_a_listo2[indice2][0])
                    estado_listo[indice2] = proceso_a_listo2[indice2]
                    estado_listo[indice2].append(1)
                    proceso_en_memoria_2 = indice2
                    try:
                        del estado_ls[indice2]
                    except:
                        err = 1
                else:
                    if (int(memoria[2]) == 60) and (int(proceso_a_listo2[indice2][0]) <= int(
                            memoria[2])):  # SI LA PARTICION [2] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                        memoria[2] -= int(proceso_a_listo2[indice2][0])
                        estado_listo[indice2] = proceso_a_listo2[indice2]
                        estado_listo[indice2].append(2)
                        proceso_en_memoria_3 = indice2
                        try:
                            del estado_ls[indice2]
                        except:
                            err = 1
        except:
            err=1
        """---------------------------------------------------"""

        """TRATA TERCER CANDIDATO PARA ENTRAR A LISTO"""
        try:
            if (int(memoria[0]) == 250) and (int(proceso_a_listo3[indice3][0]) <= int(
                    memoria[0])):  # SI LA PARTICION [O] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                memoria[0] -= int(proceso_a_listo3[indice3][0])
                estado_listo[indice3] = proceso_a_listo3[indice3]
                estado_listo[indice3].append(0)
                proceso_en_memoria_1 = indice3
                try:
                    del estado_ls[indice3]
                except:
                    err = 1
            else:
                if (int(memoria[1]) == 120) and (int(proceso_a_listo3[indice3][0]) <= int(
                        memoria[1])):  # SI LA PARTICION [1] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                    memoria[1] -= int(proceso_a_listo3[indice3][0])
                    estado_listo[indice3] = proceso_a_listo3[indice3]
                    estado_listo[indice3].append(1)
                    proceso_en_memoria_2 = indice3
                    try:
                        del estado_ls[indice3]
                    except:
                        err = 1
                else:
                    if (int(memoria[2]) == 60) and (int(proceso_a_listo3[indice3][0]) <= int(
                            memoria[2])):  # SI LA PARTICION [2] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                        memoria[2] -= int(proceso_a_listo3[indice3][0])
                        estado_listo[indice3] = proceso_a_listo3[indice3]
                        estado_listo[indice3].append(2)
                        proceso_en_memoria_3 = indice3
                        try:
                            del estado_ls[indice3]
                        except:
                            err = 1
        except:
            err=1

        """-------------------------Tratar SWAP de Listo por TI Menor--------------------------"""

        try:
            prueba=estado_listo[proceso_en_memoria_1]
            try:

                if (int(proceso_a_listo[indice][2]) < int(estado_listo[proceso_en_memoria_1][2])) and (int(proceso_a_listo[indice][0]) <= 250):
                    print()
                    imprimir_instancia(i-1)
                    aux[proceso_en_memoria_1] = estado_listo[proceso_en_memoria_1]
                    del estado_listo[proceso_en_memoria_1]
                    estado_listo[indice] = proceso_a_listo[indice]

                    aux[proceso_en_memoria_1].pop()
                    estado_ls[proceso_en_memoria_1] = aux[proceso_en_memoria_1]

                    del estado_ls[indice]

                    estado_listo[indice].append(1)
                    print("---------------------------------")
                    print("Se realizo un SWAP por TI menor")
                    print("---------------------------------")
                    print()
                    print("Se trajo a memoria el proceso con ID:", indice, "y se llevo a L/S el proceso con ID:",
                          proceso_en_memoria_1)
                    print()
                    proceso_en_memoria_1 = indice
                    memoria[0] = 250 - int(proceso_a_listo[indice][0])
                    imprimir_memoria(estado_ejecucion, memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)
            except:
                err=1
        except:
            try:
                prueba=estado_ejecucion[proceso_en_memoria_1]
            except:
                prueba=[]
        try:
            prueba=estado_listo[proceso_en_memoria_2]
            try:
                if (int(proceso_a_listo[indice][2]) < int(estado_listo[proceso_en_memoria_2][2])) and (int(proceso_a_listo[indice][0]) <= 120):
                    print()
                    imprimir_instancia(i-1)

                    aux[proceso_en_memoria_2] = estado_listo[proceso_en_memoria_2]
                    del estado_listo[proceso_en_memoria_2]
                    estado_listo[indice] = proceso_a_listo[indice]

                    aux[proceso_en_memoria_2].pop()
                    estado_ls[proceso_en_memoria_2] = aux[proceso_en_memoria_2]

                    del estado_ls[indice]


                    estado_listo[indice].append(1)
                    print("---------------------------------")
                    print("Se realizo un SWAP por TI menor")
                    print("---------------------------------")
                    print()
                    print("Se trajo a memoria el proceso con ID:", indice, "y se llevo a L/S el proceso con ID:",
                          proceso_en_memoria_2)
                    proceso_en_memoria_2=indice
                    print()
                    memoria[1] = 120 - int(proceso_a_listo[indice][0])
                    imprimir_memoria(estado_ejecucion, memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)
            except:
                err=1
        except:
            try:
                prueba=estado_ejecucion[proceso_en_memoria_2]
            except:
                prueba=[]
        try:
            prueba=estado_listo[proceso_en_memoria_3]
            try:
                if (int(proceso_a_listo[indice][2]) < int(estado_listo[proceso_en_memoria_3][2])) and (int(proceso_a_listo[indice][0]) <= 60):
                    print()
                    imprimir_instancia(i-1)
                    aux[proceso_en_memoria_3] = estado_listo[proceso_en_memoria_3]
                    del estado_listo[proceso_en_memoria_3]
                    estado_listo[indice] = proceso_a_listo[indice]

                    aux[proceso_en_memoria_3].pop()
                    estado_ls[proceso_en_memoria_3] = aux[proceso_en_memoria_3]

                    del estado_ls[indice]

                    estado_listo[indice].append(1)
                    print("---------------------------------")
                    print("Se realizo un SWAP por TI menor")
                    print("---------------------------------")
                    print()
                    print("Se trajo a memoria el proceso con ID:",indice,"y se llevo a L/S el proceso con ID:",proceso_en_memoria_3)
                    proceso_en_memoria_3 = indice
                    print()
                    memoria[2]= 60 - int(proceso_a_listo[indice][0])
                    imprimir_memoria(estado_ejecucion, memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)
            except:
                err=1
        except:
            try:
                prueba=estado_ejecucion[proceso_en_memoria_3]
            except:
                prueba=[]


        """-------------------------carga EJECUCION (E)--------------------------"""
        if estado_ejecucion == {}:  # SI NO HAY NADA EN EJECUCION BUSCA EL DE TI MENOR GUARDA EL IND (INDICE) Y LO PONE EN EJECUCION
            ti_menor = 100
            for k1, v1 in estado_listo.items():
                if int(estado_listo[k1][2]) < int(ti_menor):
                    ti_menor = int(estado_listo[k1][2])
                    proceso_a_ejec[k1] = estado_listo[k1]
                    ind = k1

            estado_ejecucion[ind] = proceso_a_ejec[ind]
            lista_ti.append(proceso_a_ejec[ind][2])
            estado_ejecucion[ind][2] = int(estado_ejecucion[ind][2])
            try:
                del estado_listo[ind]
            except:
                err = 1

        if estado_ejecucion[ind][2] > 0:  #SI NO LLEGO A CERO EL TI LO DESCUENTA EN CADA ITERACION DE INSTANCIA
            estado_ejecucion[ind][2] -= 1

        if estado_ejecucion[ind][2] == 0: #SI LLEGO MUESTRA, TERMINA EL PROCESO, RESTABLECE LA MEMORIA Y DESCUENTA EL NIVEL DE MULTI
            print()
            imprimir_instancia(i)
            print("El proceso",ind,"que estaba ejecutándose terminó y saldrá de memoria en este instante")
            print()
            imprimir_estados(estado_nuevo, estado_ls, estado_listo, estado_ejecucion, estado_terminado, memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)

            if estado_ejecucion[ind][3] == 2:
                memoria[2] = 60
            else:
                if estado_ejecucion[ind][3] == 1:
                    memoria[1] = 120
                else:
                    if estado_ejecucion[ind][3] == 0:
                        memoria[0] = 250

            estado_terminado[ind] = estado_ejecucion[ind]
            del estado_ejecucion[ind]
            grado_multi -= 1



        if (i==0): #MOSTRAR INSTANTE 0
            if str(opcion) == "N" or str(opcion) == "n":
                print()
                print("//--//--//--//--//")
                print("En el instante: ", i, end=" ")
                print()
                print("//--//--//--//--// ")
                print()
                imprimir_estados(estado_nuevo, estado_ls, estado_listo, estado_ejecucion, estado_terminado, memoria,
                                 proceso_en_memoria_1, proceso_en_memoria_2, proceso_en_memoria_3)

            else:
                print()
                print("//--//--//--//--//")
                print("En el instante:", i, end=" ")
                print()
                print("//--//--//--//--// ")
                print()
                imprimir_estados(estado_nuevo, estado_ls, estado_listo, estado_ejecucion, estado_terminado,memoria,proceso_en_memoria_1,proceso_en_memoria_2,proceso_en_memoria_3)

print()

print("-------------------------------------------------------------------------")
print("Al finalizar el orden de los procesos ejecutados fué:",", ".join(estado_terminado))
print("                             -Con los respectivos TI:",", ".join(lista_ti))
print("------------------------------------------------------------------------- ")
input("Presione una tecla para ver la memoria al finalizar: ")
print()

value1=str(memoria[2])+ "K"
value2=str(memoria[1])+ "K"
value3=str(memoria[0])+ "K"
SO="100K SO"

cadena1 = "|{:<10}|".format(value1)
cadena2 = "|{:<10}|".format(value2)
cadena3 = "|{:<10}|".format(value3)
cadena4 = "|{:<10}|".format(SO)

print("+----------+")
print(cadena1)
print("+----------+")
print(cadena2)
print("+----------+")
print(cadena3)
print("+----------+")
print(cadena4)
print("+----------+")
print()
input("FIN ")


