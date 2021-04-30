#EJERCICIO 6
i = 0
notas = []
while i < 5:
    i = i+1
    nts = float(input(f"Ingrese la nota {i}: "))
    notas.append(nts)

Def = (notas[0]*0.15)+(notas[1]*0.20)+(notas[2]*0.15)+(notas[3]*0.30)+(notas[4]*0.20)
if Def >= 3.0:
    print("Aprobó la materia con un promedio de:",Def,", felicitaciones")
else:
    print("Reprobó la materia con un promedio de:",Def,", necesita mejorar")



