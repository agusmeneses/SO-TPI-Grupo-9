import re
import operator

"""-----------Aqui se capturan los datos del txt y se los muestra por pantalla-----------"""


def captura_datos(f, cont, procesos, ti_total):
    for line in f:
        result = re.search(r"Proceso[ ]*[\d]:[ ]*(\d+),[ ]*(\d+),[ ]*(\d+),[ ]*(\d+)", line)
        if result is None:
            pass
        else:
            cont += 1
            """ ID:[TAM,TA,TI] """
            procesos[result.group(1)] = [result.group(2), result.group(3), result.group(4)]
    print("La cantidad de Procesos es: ", cont)
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
    return (procesos, ti_total)


"""-----------------------------------------------------------------------------------------"""

"""-------------------------Mostrar instancia----------------------------"""


def imprimir_instancia(i):
    print("Instancia:", i, end=" ")
    input("Presionar Enter")


"""----------------------------------------------------------------------"""

"""-------------------------Mostrar estados----------------------------"""


def imprimir_estados(estado1, estado2, estado3, estado4):
    print("Nuevo: ", estado1)
    print("Ls: ", estado2)
    print("L: ", estado3)
    print("E: ", estado4)


"""--------------------------------------------------------------------"""

"""---------------Aqui se definen las variables que seran usadas--------------"""
procesos = {}
cont = 0
f = open("Datos.txt", "r")
grado_multi = 0
ti_total = 0
memoria = [250, 120, 60]  # La primera es el SO

estado_nuevo = {}
estado_ls = {}
estado_listo = {}
estado_ejecucion = {}

proceso_a_listo = {}
proceso_a_ejec = {}
"""--------------------------------------------------------------------------"""

"""........................CÓDIGO............................."""

procesos, ti_total = captura_datos(f, cont, procesos, ti_total)  # CAPTURA DE DATOS Y MUESTRA

y = dict(sorted(procesos.items(), key=lambda x: (x[1])))  # ORDENO PROCESOS POR TA

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

        """carga LISTO (L) /// VER QUE PASA ACA SI HAY VARIOS CON TI IGUAL Y PUEDE ENTRAR UNO POR TAMAÑO MENOR"""
        ti_menor = 100
        for k, v in estado_ls.items():  # ITERA SOBRE LOS LISTO Y SUSPENDIDO Y ELIGE 1 QUE ES EL QUE TIENE TI MENOR
            if int(estado_ls[k][2]) < int(ti_menor):
                ti_menor = int(estado_ls[k][2])
                proceso_a_listo.clear()
                proceso_a_listo[k] = estado_ls[k]
                indice = k

        if (int(memoria[0]) == 250) and (int(proceso_a_listo[indice][0]) < int(
                memoria[0])):  # SI LA PARTICION [O] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
            memoria[0] -= int(proceso_a_listo[indice][0])
            estado_listo[indice] = proceso_a_listo[indice]
            estado_listo[indice].append(0)
            try:
                del estado_ls[indice]
            except:
                err = 1
        else:
            if (int(memoria[1]) == 120) and (int(proceso_a_listo[indice][0]) < int(
                    memoria[1])):  # SI LA PARTICION [1] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                memoria[1] -= int(proceso_a_listo[indice][0])
                estado_listo[indice] = proceso_a_listo[indice]
                estado_listo[indice].append(1)
                try:
                    del estado_ls[indice]
                except:
                    err = 1
            else:
                if (int(memoria[2]) == 60) and (int(proceso_a_listo[indice][0]) < int(
                        memoria[2])):  # SI LA PARTICION [2] ESTA LIBRE Y EL PROCESO PUEDE ENTRAR EN ESE ESPACIO LIBRE
                    memoria[2] -= int(proceso_a_listo[indice][0])
                    estado_listo[indice] = proceso_a_listo[indice]
                    estado_listo[indice].append(2)
                    try:
                        del estado_ls[indice]
                    except:
                        err = 1

        """-------------------------carga EJECUCION (E)--------------------------"""
        if estado_ejecucion == {}:  # SI NO HAY NADA EN EJECUCION BUSCA EL DE TI MENOR GUARDA EL IND (INDICE) Y LO PONE EN EJECUCION
            ti_menor = 100
            for k1, v1 in estado_listo.items():
                if int(estado_listo[k1][2]) < int(ti_menor):
                    ti_menor = int(estado_listo[k1][2])
                    proceso_a_ejec[k1] = estado_listo[k1]
                    ind = k1

            estado_ejecucion[ind] = proceso_a_ejec[ind]
            estado_ejecucion[ind][2] = int(estado_ejecucion[ind][2])
            try:
                del estado_listo[ind]
            except:
                err = 1

        if estado_ejecucion[ind][2] > 0:  #SI NO LLEGO A CERO EL TI LO DESCUENTA EN CADA ITERACION DE INSTANCIA
            estado_ejecucion[ind][2] -= 1

        if estado_ejecucion[ind][2] == 0: #SI LLEGO MUESTRA, TERMINA EL PROCESO, RESTABLECE LA MEMORIA Y DESCUENTA EL NIVEL DE MULTI

            print("En el instante: ", i + 1)
            imprimir_estados(estado_nuevo, estado_ls, estado_listo, estado_ejecucion)

            if estado_ejecucion[ind][3] == 2:
                memoria[2] = 60
            else:
                if estado_ejecucion[ind][3] == 1:
                    memoria[1] = 120
                else:
                    if estado_ejecucion[ind][3] == 0:
                        memoria[0] = 250

            del estado_ejecucion[ind]
            grado_multi -= 1
