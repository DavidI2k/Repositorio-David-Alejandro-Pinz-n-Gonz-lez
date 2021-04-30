def sumaDigitos(numero):
    suma = 0 #Variable para guardar la suma
    while numero != 0:
        digito = numero % 10 #Con esto agarramos los digitos de ese número
        suma = suma + digito
        numero = numero // 10
    return suma


cantidad = 0 #Variable para mostrar la cantidad de números
mayor = -1
numero = int(input("Ingrese un número posiivo, para terminar de ingresar números, ingrese un número negativo: "))
while numero >= 0:
    suma = sumaDigitos(numero)
    if suma > mayor:
        mayor = suma
        n_mayorsuma = numero
    if suma < 10:
        cantidad += 1
    numero = int(input("Número positivo: "))
print("Sumatoria de dígitos de", n_mayorsuma, ":", mayor)
print("Cantidad con sumatoria menor a 10:", cantidad)
