#Otra vez especificar las variables, y agregar texto para facilitar la interacción con el usuario.
Tamaño = int(input("Ingrese cuántos nombres va a ingresar: ")) #Array.
Nombres = [] #Lista para almacenar los nombres.
Cantidad = [] #Lista para almacenar lo largo que son los nombres ingresados.
for num in range (0,Tamaño): #Rango que mira de 0 hasta como se definió "Tamaño"
 Nombres.append(input("Ingresa el nombre de una persona, para que este se agregue a la lista: ")) #Ingresa en la lista las personas,
 #Tomando en cuenta el rango, y así pregunte varias veces
print ("Se ingresaron los siguientes nombres: ",Nombres)
for i in range (0,Tamaño): #Mira el rango de 0 hasta como se definió "Tamaño", para que pregunte varias veces
 Cantidad.append(len(Nombres[i])) #Mete a la lista, la longitud de cada nombre, en la posición del rango 0 hasta tamaño
 #Esto para que la longitud de cada nombre sea respecto a su posición en la lista
print ("La longitud de cada nombre en orden es: ",Cantidad)
