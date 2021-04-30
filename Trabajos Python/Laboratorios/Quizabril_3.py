#Cómo estamos en un país de habla español, traduzcamos el nombre de las variables para facilidad.
Materias = ["Matemáticas","Física","Química","Historia","Lenguaje"] #Lista con las materias
Notas = [] #Lista dónde se almacenaran las notas
for Clase in Materias: #Revisa cada item individualmente, en forma númerica (posición en la lista), de la lista Materias
    NotaIndv = input("¿Qué nota has sacado en "+ Materia +"?: ")
    Notas.append(NotaIndv)
for i in range(0,5): #Se mira cada número en un rango de 0 a 5
    print("En "+Materias[i]+" obtuviste una nota de: "+Notas[i])
    #Para saber cuál materia va con cuál nota, se usa el contador i, para así dar la nota de cada materia
    #Basada en su posición en la lista


