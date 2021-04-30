cedula = int(input("Ingrese su cedula: "))
def ced_colb(cedula):
    if len(str(cedula))>6:
        print("True")
    else:
        print("False")


ced_colb(cedula)