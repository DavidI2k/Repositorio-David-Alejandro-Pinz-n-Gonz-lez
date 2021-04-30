repetir = "si"
def numprimo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            return True

while repetir == "si":
    num = int(input("Ingrese el número a comprobar si es primo: "))
    if num == 0 or num < 0:
        #Acá solo comprueba si el número es 0 o negativo, para que vuelva a empezar el ciclo while
        print("Número invalido, solo ingrese números mayores a 1!")
        continue #Esto permite que vuelva a empezar con tal de que se cumpla la condición
    elif numprimo(num):
        print(f"El número {num} es primo.") #Utilizo F, para concatenar la variable dentro de una cadena
    else:
        print(f"El número {num} no es primo.") #Acá lo mismo, concateno la varabible dentro de una cadena
    repetir = input("¿Quieres ingresar otro número? escribe si o no: ")
    if repetir == "no": #Todo este código sirve para la variable repetir, que permite al usuario decidir si quiere introducir otro número
        #o no
        print("El programa ha finalizado con éxito")





