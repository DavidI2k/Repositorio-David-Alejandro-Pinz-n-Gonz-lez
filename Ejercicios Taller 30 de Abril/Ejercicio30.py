#EJERCICIO 30
cn = int(input("Ingrese cuántos números quiere comparar: "))
i = 1
lista = []
while cn > 0:
    n = int(input(f"Ingrese el número{i}: "))
    lista.append(n)
    i= i+1
    cn = cn-1

print("El número mayor de los ingresados es: ",max(lista))
print("El número menor de los ingresados es: ",min(lista))

