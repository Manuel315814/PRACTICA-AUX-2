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

#####     SEGUNDO PROBLEMA     #####
lista = []

for i in range(5):
    numero = int(input("INGRESE LOS NUMEROS: "))
    lista.append(numero)

suma = sum(lista)
promedio = suma / len(lista)

print("LISTA DE NUMEROS:", lista)
print("LA SUMA ES:", suma)
print("EL PROMEDIO ES:", promedio)