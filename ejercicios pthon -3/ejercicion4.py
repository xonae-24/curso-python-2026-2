saldo = 1500000
depositos = 0
retiros = 0
movimientos = []

while True:
    print("\n1. consultar saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("4. ver movimientos realizados")
    print("5. salir")

    opcion = int(input("seleccione una opcion: "))

    if opcion == 1:
        print("saldo disponible:", saldo)

    elif opcion == 2:
        dinero = float(input("ingrese el valor a depositar: "))

        if dinero > 0:
            saldo += dinero
            depositos += 1
            movimientos.append("deposito: $" + str(dinero))
            print("deposito realizado")
        else:
            print("no se permiten depositos negativos")

    elif opcion == 3:
        dinero = float(input("ingrese el valor a retirar: "))

        if dinero < 10000:
            print("el retiro minimo es de $10000")
        elif dinero + 4500 > saldo:
            print("saldo insuficiente")
        else:
            saldo -= dinero + 4500
            retiros += 1
            movimientos.append("retiro: $" + str(dinero))
            print("retiro realizado")
            print("costo del retiro: $4500")

    elif opcion == 4:
        print("\nmovimientos realizados:")

        if len(movimientos) == 0:
            print("no hay movimientos")
        else:
            for movimiento in movimientos:
                print(movimiento)

    elif opcion == 5:
        print("cantidad de depositos:", depositos)
        print("cantidad de retiros:", retiros)
        print("gracias por usar el cajero")
        break

    else:
        print("opcion no valida")