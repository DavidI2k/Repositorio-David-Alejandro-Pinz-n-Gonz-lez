def frecuencia(numero, digito):
    cant = 0
    while numero != 0: #Se crea un loop while mienntras el número sea diferente de cero
        ultDigito = numero % 10 #Se mira el modulo del numero en 10
        if ultDigito == digito: #Si el resultad de ultDigito es igual al digito, se le suma 1 a cant
            cant += 1
        numero = numero // 10
    return cant


num = int(input("Ingrese su número: "))
un_digito = int(input("Ingrese su dígito: "))
print("Frecuencia del dígito en el número:", frecuencia(num, un_digito))

