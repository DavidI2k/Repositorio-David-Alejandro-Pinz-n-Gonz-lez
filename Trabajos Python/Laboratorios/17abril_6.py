def factorial(numero):
    f = 1 #Variable que guarde resultados
    if numero != 0:
        for i in range(1, numero + 1): #Mira cada número en un rango de 1, mas
            #El numero ingresado, pero sumado 1
            f = f * i #Factorial, multiplica esta variable por i, que sería igual a todos los números desde un rango de 1 hasta
            # el número que se ingrese + 1, ej: de 1 a 5 +1 = 6
    return f #Devuelve el resultado de f


cantidad = 0 #Variable para guardar cuántos números fueron ingresados
num = int(input("Ingrese su número, ingrese -1, para parar de ingresar números: "))
while num != -1: #Ciclo while para que pregunte siempre por un número
    print("Factorial:", factorial(num))
    cantidad += 1 #Suma 1 cada vez que pasa por el ciclo while, así sabemos cuántos números se ingresaron
    num = int(input("Ingrese su número, ingrese -1 para parar de ingresar números: "))
print("Se leyeron", cantidad, "números")
