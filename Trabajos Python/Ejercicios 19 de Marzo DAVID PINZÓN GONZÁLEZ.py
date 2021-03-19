#EJERCICIO 1
print('\033[91m'+"EJERCICIO 1"+'\033[0m') # Esto es solo para que quede las letras en color rojo
x=0
while x < 9:
    x = x+0.1
    print(x)

#EJERCICIO 2
print('\033[91m'+"EJERCICIO 2"+'\033[0m')
num = 1
for y in range(100,200):
    print(y)

#EJERCICIO 3
print('\033[91m'+"EJERCICIO 3"+'\033[0m')
for z in range(5,21,3):
    print(z)

#EJERCICIO 4
print('\033[91m'+"EJERCICIO 4"+'\033[0m')
numx = int(input("Ingrese un número entero positivo:"))
for v in range (numx, numx*2):
    print(v)

#EJERCICIO 5
print('\033[91m'+"EJERCICIO 5"+'\033[0m')
frase = str(input(""))
for n in "aeiou":
    if n in frase:
        print(n)

#EJERCICIO 7
print('\033[91m'+"EJERCICIO 7"+'\033[0m')
total = 0
for nnn in range(101):
    total=total+nnn
print("La suma de los números es:",total)

#EJERCICIO 8
print('\033[91m'+"EJERCICIO 8"+'\033[0m')
aninicial = int(input("Ingrese el año inicial: "))
anfinal = int(input("Ingrese el año final: "))
for anio in range(aninicial, anfinal+1):
    if anio%10==0:
        print("Años multiplos de 10: ",anio)
    if anio%4==0 or anio%400==0 and anio%100 != 0:
        print("Años biciestos:",anio)
    print("Años en este rango: ",anio)

#EJERCICIO 9
print('\033[91m'+"EJERCICIO 9"+'\033[0m')
numero = int(input("Ingrese su número: "))
p = 1
if numero != 0:
    for hh in range (1,numero+1):
        p = p*hh
print("El factorial es: ",p)

#EJERCICIO 10
print('\033[91m'+"EJERCICIO 10"+'\033[0m')
v1 = 0
v2 = 1
print(v1)
print(v2)
for madre69 in range(8):
    v3 = v1+v2
    print(v3)
    v1 = v2
    v2 = v3




