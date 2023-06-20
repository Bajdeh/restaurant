import numpy

arreglo_rest = numpy.zeros((3,3))

Fanta = 1000
Score = 2000
bluelabel = 80000

fideoconsalsa = 8000
pizzadelchicocesar = 6500
porotos = 10000

jalea = 3000
Heladopiña = 5000
torta = 6500

lista_rut = []


def opcion ():
    while True:
        try:
            opcion = int(input("Ingrese su opcion :"))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("Ingrese entre 1 y 6")
        except:
            print("Ingrese una opcion valida")

def verrestaurant():
    for x in range(2):
            for y in range(2):
                print(arreglo_rest[x][y],end=" ")
            print()




def reservar():
    rut = validar_rut
    nombre = validar_nombre
    correo = validar_correo
    cantidad = validar_cant


def validar_nombre():
    nombre = input("ingrese su nombre:")
    if len(nombre.strip()) > 3:
        return nombre
    else:
        print("Ingrese un nombre como minimo de 3 palabras")

def validar_correo ():
    if "@" in correo:
        return correo
    else:
        print("Ingrese un correo correspondiente con @")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut, sin digito verificador ademas sin punto :"))
            if rut > 1000000 and rut<99999999:
                lista_rut.append[rut]
                return rut
            else:
                print("Ingrese un rut valido")
        except:
            print("Ingrese valores positivos ")

def validar_cant():

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de personas para asistir: "))
            if cantidad < 7 and cantidad >1:
                return cantidad
            else:
                print("Ingrese una cantidad entre 1 a 6")
        except:
            print("Ingrese numeros validos")

def validar_carta():
    rut = validar_rut
    for x in lista_rut:
        for x in range (len(lista_rut)):
            if rut == lista_rut[x]:
                pass
                
            else:
                print("Ingrese un rut valido en alguna de las mesas para pedir la carta")
                        


def validar_comestibles():
    while True:
        print("""Menú Comestibles
        1.Bebestibles
        2.Platos
        3.Postres
        4.Pedir
        5.Cancelar""")



