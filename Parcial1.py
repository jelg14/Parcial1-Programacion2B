
import sys
from collections import *
marca = deque()
tamañoMotor = deque()
modelo = deque()
color = deque()
tipoTraccion = deque()
vehiculos = deque()

d = True
while(d):
    user = input("ingrese usuario:")
    password = input("ingrese contraseña:")

    u = "Admin"
    p = "123/*"

    if user == u and password == p:
        print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
        """)
        while True:
            print("""
**************SELECCIONE UNA OPCION:***************
***************************************************
** Agregar lista de vehiculos.................(1)
** Mostrar listado ingresados ............(2)
** Salir de la aplicacion .................(3)
***************************************************""")
            opcion = int(input())
            if opcion == 1:
                print("procesando peticion...")
                while True:
                    marca_vehiculo =input("ingrese marca del vehiculo ")
                    marca.append(marca_vehiculo)
                    tamaño_motor =input("ingrese el tamaño del motor que posee el vehiculo ")
                    tamañoMotor.append(tamaño_motor)
                    modelo_vehiculo =input("ingrese el modelo del vehiculo ")
                    modelo.append(modelo_vehiculo)
                    color_vehiculo =input("ingrese el color del vehiculo ")
                    color.append(color_vehiculo)
                    tipo_tranccion =input("ingrese el tipo de traccion del vehiculo ")
                    tipoTraccion.append(tipo_tranccion)
                    print("desea agregar otro dato?")
                    res = input()
                    if res == "no": break
            elif opcion == 2:
                print("imprimiendo...")
                while len(marca) > 0 and len(tamañoMotor) > 0 and len(modelo) > 0 and len(color) > 0 and len(tipoTraccion) > 0:
                    v =  {"Marca":marca.popleft(),"Motor":tamañoMotor.popleft(),"Modelo":modelo.popleft(),"Color":color.popleft(), "Traccion":tipoTraccion.popleft()}
                    vehiculos.append(v)
                print("#########################################Listado de Vehiculos###############################################")
                print(vehiculos)
                print("########################################################################################")
            elif opcion == 3:
                print("adios.")
                sys.exit(0)
            else: print("error: Comando desconocido")
    else:
        print("ERROR: Datos erroneos")
        opcion = input("¿Desea salir? ")
        if (opcion == "si"): d = False