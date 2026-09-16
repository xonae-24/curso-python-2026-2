numero = int(input("ingrese un numero: "))

contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
        contador += 1



if contador == 2:
    print("el numero es primo")
else:
    print("el numero no es primo")