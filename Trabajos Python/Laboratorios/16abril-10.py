cadena = str(input("Ingrese su cadena: "))
def cont_palabra(cadena):
    lista = cadena.split()
    ult_palabra = lista[-1]
    print(len(ult_palabra))
cont_palabra(cadena)