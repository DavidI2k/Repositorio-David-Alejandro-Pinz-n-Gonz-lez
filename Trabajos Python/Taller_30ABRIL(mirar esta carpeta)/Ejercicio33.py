#Ejercicio 33
year = int(input("Ingrese el año a mirar si es bisiesto o no: "))
if year%4!=0:
    print("No es bisiesto")
elif year%4 ==0 and year%100!=0:
    print("Es bisiesto")
elif year%4==0 and year%100==0 and year%400!=0:
    print("No es bisisesto")
elif year%4==0 and year%100==0 and year%400==0:
    print("Es bisisesto")