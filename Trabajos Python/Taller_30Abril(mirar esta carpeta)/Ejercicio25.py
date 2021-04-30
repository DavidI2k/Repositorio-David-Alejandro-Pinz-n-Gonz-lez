#EJERCICIO 25
compra = float(input("Ingrese el valor de su compra, si mayor a 150.000, se le aplica un descuento del 5%: "))
IVA = compra*0.19
total = compra+IVA
if compra > 150.000:
    desc = total*0.5
    total = total-desc
    print("El valor total de su compra con descuento, sumado el IVA es:{}".format(total))
else:
    print("El valor total de su compra sin descuento, sumado el IVA, es:{}".format(total))