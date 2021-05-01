#Ejercicio 32
def val_pagar(km,dias):
    total=km*5000
    return total


km=int(input("Km a recorrer: "))
dias=int(input("¿Cuántos días se quedará: "))

if km<20:
    print("Ingrese más kilometros")
    exit()

valor_a_pagar = val_pagar(km,dias)
print(f'Su total a pagar es:{valor_a_pagar}')

if km>=1000 and dias>=7:
    descuento=valor_a_pagar*0.15
    print("El descuento obtenido es de:",descuento)