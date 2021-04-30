palabra = input("Ingrese la palabra a mirar si es palindromo o no: ")
palabralrev = palabra
palabra = list(palabra)
palabralrev = list(palabralrev)
palabralrev.reverse()
if palabra == palabralrev:
    print("La palabra", *palabra, " es un palíndromo")
else:
    print("La palabra", *palabra, " no es un palíndromo")