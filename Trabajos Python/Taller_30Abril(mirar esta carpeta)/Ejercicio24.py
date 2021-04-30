#EJERCICIO 24
num = int(input("Ingrese el número a comprobar si es positivo o negativo: "))
if num  > 0 and num %2 == 0:
    print("Es un número par-positivo")
elif num < 0 and num%2 == 0:
    print("Es un número par-negativo")
elif num > 0 and num %2 != 0:
    print("Es un número impar-positivo")
elif num < 0 and num%2 != 0:
    print("Es un número impar-negativo")
elif num == 0:
    print("El número es cero!")
