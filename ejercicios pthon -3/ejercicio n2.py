cantidadestudiantes = int(input("ingrese la cantidad de estudiantes: "))

aprobados = 0
reprobados = 0
suma_promedios = 0
promediomasalto = 0
promediomasbajo = 5

for i in range(1, cantidadestudiantes + 1):

    print("\nestudiante", i)

    nota1 = float(input("ingrese la calificacion 1 (0.0 - 5.0): "))
    nota2 = float(input("ingrese la calificacion 2 (0.0 - 5.0): "))
    nota3 = float(input("ingrese la calificacion 3 (0.0 - 5.0): "))

    promedio = (nota1 + nota2 + nota3) / 3

    print("promedio:", round(promedio, 2))

    if promedio <= 2.9:
        print("clasificacion: reprobado")
        reprobados += 1
    elif promedio <= 3.9:
        print("clasificacion: aprobado")
        aprobados += 1
    elif promedio <= 4.5:
        print("clasificacion: sobresaliente")
        aprobados += 1
    else:
        print("clasificacion: excelente")
        aprobados += 1

    sumapromedios += promedio

    if promedio > promediomasalto:
        promediomasalto = promedio

    if promedio < promediomasbajo:
        promediomasbajo = promedio

promediogeneral = sumapromedios / cantidadestudiantes

print("\n===== resultados del grupo =====")
print("cantidad de estudiantes aprobados:", aprobados)
print("cantidad de estudiantes reprobados:", reprobados)
print("promedio general del grupo:", round(promediogeneral, 2))
print("promedio mas alto:", round(promediomasalto, 2))
print("promedio mas bajo:", round(promediomasbajo, 2))