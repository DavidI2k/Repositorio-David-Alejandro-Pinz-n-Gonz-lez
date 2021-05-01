#Ejercicio 35
usuario = "costeños@gmail.com"
contraseña = 12345

ig_usuario = str(input("usuario: "))
ig_contraseña = int(input("contraseña: "))

if ig_usuario==usuario and ig_contraseña==contraseña:
    print("siga papi")
else:
    print("impostor")
    exit()