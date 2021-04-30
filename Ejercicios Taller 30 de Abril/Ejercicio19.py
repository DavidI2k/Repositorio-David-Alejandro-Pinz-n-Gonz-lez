#EJERCICIO 19
segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = int(segundos/1800)
horas = int(segundos/3600)
segundo = int(segundos%60)
print("El resultado es: ",horas,":",minutos,":",segundo)