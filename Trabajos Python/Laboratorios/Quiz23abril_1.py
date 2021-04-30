#Especificar las variables, para evitar confusión al mirar el código después y que sea fácil para la interacción con el usuario.
tamaño = int(input("Ingrese cuántos valores quiere ver: ")) #Array
multiplo = int(input("Ingrese el número, que será el multiplo de los valores que quiere ver: "))
multiplos = [] #Lista para guardar los multiplos para facilidad

for num in range(1,tamaño+1): #Rango de 1, hasta los valores ingresados +1
    multiplos.append(num*multiplo) #Multiplica cada valor del rango por el multiplo ingresado.
print("Los",tamaño,"multiplos de",multiplo,"son: ",multiplos)
