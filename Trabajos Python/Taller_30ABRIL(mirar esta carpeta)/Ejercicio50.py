#Ejercicio 50
i=1
k=int(input("Cuántos números ingresará?: "))
k1 = k
suma=0
while k>0:
    n= int(input("#"+str(i)+"="))
    i+=1
    k-=1
    suma+=n
print(suma)
print("Promedio:",suma/k1)