cantidad = int(input("ingrese la cantidad de terminos: "))

a = 0
b = 1
suma = 0
pares = 0
impares = 0

for i in range(cantidad):
    print(a, end=" ")

    suma += a

    if a % 2 == 0:
        pares += 1
    else:
        impares += 1

    siguiente = a + b
    a = b
    b = siguiente

print("\nsuma de los terminos:", suma)
print("terminos pares:", pares)
print("terminos impares:", impares)