nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
nota = float(input("ingrese su nota: "))


agregar_estudiantes= []
estudiante = {"nombre" : nombre,
                "edad" : edad,
                "nota" : nota
}
agregar_estudiantes.append (estudiante)
print (agregar_estudiantes[0])
nombre2 = input("ingrese su nombre: ")
edad2 = input("ingrese su edad: ")
nota2 = float(input("ingrese su nota: "))
estudiante2= {

" nombre": nombre2,
"edad" :edad2,
 "nota":nota2

}
agregar_estudiantes.append(estudiante2)
print (agregar_estudiantes[1])
nombre3 = input("ingrese su nombre: ")
edad3 = input("ingrese su edad: ")
nota3 = float(input("ingrese su nota: "))
estudiante3= {

" nombre": nombre3,
"edad" :edad3,
 "nota":nota3

}
agregar_estudiantes.append(estudiante3)


promedios_notas= [] 
promedios_notas.append(agregar_estudiantes)
promedio = nota + nota2 + nota3
division = promedio / 3
cantidad = agregar_estudiantes
print ("total de estudiantes: 3 ")
print("promedio de los estudiantes actuales: ",division)


#no entendi como es que funcionan los diccionarios







