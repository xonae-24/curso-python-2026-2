#reto 1
nombre_de_empleado = input("ingrese su nombre: ")
horas= int(input("ingrese el numero de horas trabajadas: "))
valorhora = 10
salario= horas * valorhora 
print ("nombre del empleado: ",nombre_de_empleado)
print ("horas trabajadas: ",horas)
print ("valor de hora en dolares: ",valorhora)
print ("salario: ",salario)


#reto 2
nombre = str(input("ingrese su nombre:"))
valorcomida= int(input("ingrese el valor de la comida:"))
valorbebida= int(input("ingrese el valor de la bebida:"))
subtotal = valorcomida +valorbebida
propina = 10/100 * subtotal
total= subtotal + propina
print("comida:",valorcomida)
print("bebida_",valorbebida)
print("cuenta:", total)



#reto 3
nombre= str(input("ingrese su nombre: "))
peso= float(input("ingrese su peso en KG: "))
estatura= float(input("ingrese su estatura: "))
IMC = peso / estatura**2
print ("nombre: " ,nombre)
print ("peso:",peso)
print ("estatura: ",estatura)
print ("IMC: " ,IMC)

#reto 4

codigopc= (input("ingrese el codigo del equipo: "))
marca= str(input("ingrese la marca del equipo: "))
procesador= (input("ingrese el procesador del equipo: "))
ram= (input("ingrese la cantidad de ram del equipo: "))
capacidaddisco= (input("ingrese la capacidad del disco duro: "))
os= (input("ingrese el sistema operativo del equipo: "))
estado= str(input("en que estado esta el equipo: "))
print("="*40)
print(f"{'FICHA TECNICA DE EQUIPO':^40}")
print("codigo del equipo: ",codigopc)
print("marca del equipo: ",marca)
print("procesador del equipo: ",procesador)
print("cantidad de ram: ",ram)
print("capacidad de almacenamiento: ",capacidaddisco)
print("sistema operativo: ",os)
print("estado del equipo: ",estado)
print("="*40)

#reto 5

codigo= input("ingrese el codigo del estudiante: ")
nombre= input("ingrese el nombre del estudiante: ")
edad = input("ingrese su edad: ")
programa = input("ingrese el progroma en el que esta inscrito: ")
semestre = input("ingrese el semestre en el que esta:")
materias = int(input("ingrese el numero de materias que cursa: "))
valormaterias = float(input("ingrese el valor de cada materia: "))

totalmatricula = materias * valormaterias
print ("="*40)
print(f"{'REGISTRO DE MATRICULA':^40}")
print ("="*40)
print("codigo del estudiante: ",codigo)
print("nombre del estudiante: ",nombre)
print("edad del estudiante: ",edad)
print("programa en el que esta inscrito: ",programa)
print("semestre en el que esta: ",semestre)
print("numero de materias que cursa: ",materias)
print("valor de cada materia: ",valormaterias)
print ("="*40)



# actividad de analisis
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)
#pregunta 1: :el problema que presenta es que la variable de la edad es tipo string y no se puede usar en una operacion matematica
#pregunta 2: el input devuelve un string y no un numero
#pregunta 3: pues se puede corregir colocando primero el int antes que el input para que sea un variable tipo entera
#pregunta 4: 
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
#se añade int antes del input
nueva_edad= edad + 5
print (nombre)
print(nueva_edad)















