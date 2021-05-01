#EJERCICIO 21
numero = int(input("Ingrese un número de 4 dígitos a reordernar: "))
num_alrev = 0
while numero > 0:
    residuo = numero % 10
    num_alrev = (num_alrev*10)+residuo
    numero = numero // 10

print(f"El número reordenado inversamente es: {num_alrev}")

