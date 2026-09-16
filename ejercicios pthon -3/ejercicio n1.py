while True:
    try:
        lado1 = float(input("ingrese la medida del primer lado:  "))
        lado2 = float(input("ingrese la medidad del  segundo lado: "))
        lado3 = float(input("ingrese la medida del tercer lado: "))
        if lado1 > 0 and lado2 > 0 and lado3 > 0:
            break

        else:
            print("solo se permiten numeros positivos")

    except ValueError:
        print("por favor ingrese un valor valido")

triangulo = (
    (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
)

if triangulo:
    print("\nLos lados ingresados si forman un triangulo")

    if lado1 == lado2 == lado3:
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("El triangulo es isoceles")
    else:
        print("El triangulo es escaleno")
else:
    print("\n la suma de lados no pueden forman un triangulo")
    print("no cumple los requisitos para forman un triangulo")
