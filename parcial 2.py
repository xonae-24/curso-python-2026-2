carros = [["", "", "", 0, 0, 0] for i in range(30)]
cantidad = 0
opcion = 0

while opcion != 4:
    print("\n1. ingresar carro")
    print("2. registrar salida")
    print("3. mostrar reportes")
    print("4. salir")

    opcion = int(input("seleccione una opcion: "))

    if opcion == 1:
        if cantidad < 30:
            carros[cantidad][0] = input("placa: ")
            carros[cantidad][1] = input("nombre del propietario: ")
            carros[cantidad][2] = input("numero de celular: ")
            carros[cantidad][3] = int(input("dia de ingreso: "))
            cantidad += 1
            print("carro registrado")
        else:
            print("taller lleno")

    elif opcion == 2:
        placa = input("placa del carro: ")
        encontrado = False

        for i in range(cantidad):
            if carros[i][0] == placa:
                encontrado = True

                if carros[i][4] == 0:
                    salida = int(input("dia de salida: "))
                    carros[i][4] = salida

                    if salida >= carros[i][3]:
                        carros[i][5] = salida - carros[i][3]
                    else:
                        carros[i][5] = 30 - carros[i][3] + salida

                    print("dias en el taller:", carros[i][5])
                else:
                    print("el carro ya fue entregado")
                break

        if encontrado == False:
            print("carro no encontrado")

    elif opcion == 3:
        terminados = 0

        print("\ncarros reparados:")

        for i in range(cantidad):
            if carros[i][4] != 0:
                terminados += 1
                print("placa:", carros[i][0])
                print("dias en el taller:", carros[i][5])

        print("total de carros reparados:", terminados)

        print("\ntodos los carros registrados:")

        for i in range(cantidad):
            print("placa:", carros[i][0])
            print("propietario:", carros[i][1])
            print("celular:", carros[i][2])

    elif opcion == 4:
        print("aplicacion cerrada")

    else:
        print("opcion incorrecta")























        