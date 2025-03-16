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

#####     TERCER PROBLEMA     #####
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero): 
        if numero % i == 0:
            return False
    return True
print("VERICAMOS SI ESTOS NUMEROS SON PRIMOS O NO")
print("EL NUMERO 2 ES PRIMO ? ", es_primo(2)) 
print("EL NUMERO 4 ES PRIMO ? ", es_primo(4)) 
print("EL NUMERO 3 ES PRIMO ? ", es_primo(3))
print("EL NUMERO 6 ES PRIMO ? ", es_primo(6))
print("EL NUMERO 5 ES PRIMO ? ", es_primo(5)) 
print("EL NUMERO 8 ES PRIMO ? ", es_primo(8))
print("EL NUMERO 7 ES PRIMO ? ", es_primo(7))
print("EL NUMERO 9 ES PRIMO ? ", es_primo(9))
print("EL NUMERO 11 ES PRIMO ? ", es_primo(11))  
print("EL NUMERO 25 ES PRIMO ? ", es_primo(25)) 