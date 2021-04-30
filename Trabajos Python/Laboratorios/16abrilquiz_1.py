def ingresar(numeros):
    suma = 0
    while numeros != 0:
        digito = numeros%10
        suma = suma+digito
        numeros = numeros//10
    return suma

num = int(input("Ingrese el número que quiere procesar, si quiere parar, ingrese el número 0: "))
while num != 0:
    print("La suma de los dígitos de ese número es: ",ingresar(num))
    num = int(input("Ingrese el número que quiere procesar, si quiere parar, ingrese el número 0: "))







