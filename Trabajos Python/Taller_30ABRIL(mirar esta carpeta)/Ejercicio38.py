#Ejercicio 38
lista=[]
contador=int(input("Cuántos números ingresara?: "))
i=1
while contador>0:
    num=int(input("#"+str(i)+":"))
    i+=1
    lista.append(num)
    contador-=1
uno=lista[0]
dos=lista[-1]

if dos>uno:
    print("La secuencia incrementa")
else:print("La secuencia decrementa")