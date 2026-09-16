numero = float(input("numero decimal: "))

binario = ""

while numero > 0:
    residuo = numero % 2
    binario = str(residuo) + binario
    numero = numero // 2

print("resultado binario:", binario)