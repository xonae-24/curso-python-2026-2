cantidad = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma = 0

numero = int(input("ingrese un numero: "))

while numero != 0:

    cantidad += 1
    suma += numero

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if cantidad == 1:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero

    numero = int(input("ingrese un numero: "))

print("\ncantidad de numeros:", cantidad)
print("positivos:", positivos)
print("negativos:", negativos)
print("pares:", pares)
print("impares:", impares)
print("suma total:", suma)

if cantidad > 0:
    promedio = suma / cantidad
    print("promedio:", promedio)
    print("numero mayor:", mayor)
    print("numero menor:", menor)
else:
    print("no se ingresaron numeros")