#Ejercicio 48
n = int(input("n: "))
m = int(input("m: "))
suma=0
if m>n:
    for i in range(n+1,m):
        i=i
        suma+=i
else:print("m es menor que n")
print(suma)