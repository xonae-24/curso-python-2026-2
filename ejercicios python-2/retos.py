nombre = str(input("ingrese su nombre:"))
valorcomida= int(input("ingrese el valor de la comida:"))
valorbebida= int(input("ingrese el valor de la bebida:"))
cantidadpersonas= int(input("ingrese la cantidad de personas:"))
subtotal = valorcomida +valorbebida
propina = 10/100 * subtotal
total= subtotal + propina
print("comida:",valorcomida)
print("bebida_",valorbebida)
print("cuenta:", total)
print("valor por persona:", total/cantidadpersonas)

C= float(input("ingrese la temperatura: "))
F = (C * 9/5) +32
print("la temperatura en  celsius es: ",C)
print ("la temperatura en fahrenheit: ",F)

dolares = int(input("ingrese la cantidad de dolares: "))
cop = dolares * 3129.75
print("la cantidad de pesos colombianos es :",cop)














