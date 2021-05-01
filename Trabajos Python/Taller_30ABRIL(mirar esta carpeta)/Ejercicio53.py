#Ejercicio 53
k=int(input("numeros?="))
lista1=[]
lista2=[]
r=1
while r>0:
    for i in range(k):
        if i>100:
            lista1.append(i)
    for i in range(k):
        if i<100:
            lista2.append(i)
    r-=1
print("Mayor que 100: ",len(lista1))
print("Menores que 100: ",len(lista2))