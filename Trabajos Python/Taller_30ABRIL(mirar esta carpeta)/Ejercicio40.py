#Ejercicio 40
numero = int(input("Día: "))
if numero<0 and numero>7:
    exit()

if numero==1:
    print("Lunes")
elif numero==2:print("Martes")
elif numero==3:print("Miercoles")
elif numero==4:print("Jueves")
elif numero==5:print("Viernes")
elif numero==6:print("Sábado")
elif numero==7:print("Domingo")