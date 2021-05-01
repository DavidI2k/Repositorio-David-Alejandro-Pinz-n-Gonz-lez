#Ejercicio 55
n = int(input("Número 1:"))
k=9
i=10
r=2
lista1=[]
if n>=0:
    while k>0:
        n = int(input("numero "+str(r)+":"))
        if n<0:
            print("Ingresó un número negativo")
            exit()
        lista1.append(n)
        k-=1
        r+=1
    if n == 5:
        while i>0 and n==5:
            n = int(input("numero "+str(r)+":"))
            lista1.append(n)
            i-=1
            r+=1