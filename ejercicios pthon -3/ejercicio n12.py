usuario_correcto = "administrador"
clave_correcta = "python2026"

intentos = 3

while intentos > 0:
    usuario = input("ingrese el usuario: ")
    clave = input("ingrese la contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("acceso correcto")
        break

    if usuario != usuario_correcto and clave != clave_correcta:
        print("usuario y contraseña incorrectos")
    elif usuario != usuario_correcto:
        print("usuario incorrecto")
    else:
        print("contraseña incorrecta")

    intentos -= 1
    print("intentos restantes:", intentos)

if intentos == 0:
    print("sistema bloqueado")
else:
    while True:
        print("\n1. consultar informacion")
        print("2. cambiar contraseña")
        print("3. cerrar sesion")

        opcion = int(input("seleccione una opcion: "))

        if opcion == 1:
            print("informacion del sistema")

        elif opcion == 2:
            actual = input("ingrese la contraseña actual: ")

            if actual == clave_correcta:
                nueva = input("ingrese la nueva contraseña: ")
                clave_correcta = nueva
                print("contraseña cambiada correctamente")
            else:
                print("contraseña actual incorrecta")

        elif opcion == 3:
            print("sesion cerrada")
            break

        else:
            print("opcion no valida")