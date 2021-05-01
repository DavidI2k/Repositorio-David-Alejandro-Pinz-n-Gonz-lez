#Ejercicio 47
n = int(input("número 1: "))
m = int(input("Número 2: "))

if m>n:
    for i in range(n+1,m):
        print(i)
else:print("Número 2 es menor que Número 1")