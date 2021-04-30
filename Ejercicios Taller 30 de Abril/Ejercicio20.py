#EJERCICIO 20
ci = 0
ven = 0
die = 0
cin = 0
dos = 0
mil = 0
din = float(input("Ingrese la cantidad de dinero: "))
while din >= 50.000:
    ci += 1
    din -= 50.000
while din >= 20.000:
    ven += 1
    din -= 20.000
while din >= 10.000:
    die += 1
    din -= 10.000
while din >= 5.000:
    cin += 1
    din -= 5.000
while din >= 2.000:
    dos += 1
    din -= 2.000
while din >= 1.000:
    mil += 1
    din -= 1.000

print(f"Su usaron {ci}, billetes de 50mil pesos")
print(f"Su usaron {ven}, billetes de 20mil pesos")
print(f"Su usaron {die}, billetes de 10mil pesos")
print(f"Su usaron {cin}, billetes de 5mil pesos")
print(f"Su usaron {dos}, billetes de 2mil pesos")
print(f"Su usaron {mil}, billetes de Mil pesos")