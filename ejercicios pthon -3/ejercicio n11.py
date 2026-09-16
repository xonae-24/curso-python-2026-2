import random

print("1. facil")
print("2. intermedio")
print("3. dificil")

opcion = int(input("seleccione una dificultad: "))

if opcion == 1:
    limite = 20
    intentos = 6
elif opcion == 2:
    limite = 50
    intentos = 5
elif opcion == 3:
    limite = 100
    intentos = 4
else:
    print("opcion no valida")
    exit()

secreto = random.randint(1, limite)
restantes = intentos

while restantes > 0:
    numero = int(input("adivine el numero: "))
    restantes -= 1

    if numero == secreto:
        print("numero correcto")
        puntaje = restantes * 20
        print("puntaje:", puntaje)
        break
    elif numero < secreto:
        print("el numero secreto es mayor")
    else:
        print("el numero secreto es menor")

    print("intentos restantes:", restantes)

if restantes == 0 and numero != secreto:
    print("se terminaron los intentos")
    print("el numero secreto era:", secreto)