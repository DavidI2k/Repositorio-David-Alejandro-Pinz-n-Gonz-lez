#Ejercicio 49
i=1
k=10
suma=0
while k>0:
    n= int(input("#"+str(i)+"="))
    i+=1
    k-=1
    suma+=n
print(suma)
print("Promedio: ",suma/10)