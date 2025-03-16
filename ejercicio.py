#####     PRIMER PROBLEMA     #####
numeros = []
numero = 0

while numero >= 0:
    try:
        numero = int(input("INGRESE LOS NUMEROS:"))
        if numero >= 0:
            numeros.append(numero)
    except ValueError:
        print("ERROR, INGRESE UN NUMERO ENTERO")