#EJERCICIO 27
i = 0
notas = []
while i < 5:
    i = i+1
    nts = float(input(f"Ingrese la nota {i}: "))
    notas.append(nts)

Def = (notas[0]*0.15)+(notas[1]*0.20)+(notas[2]*0.15)+(notas[3]*0.30)+(notas[4]*0.20)
if Def <= 2.0:
    print("Su definitiva ha sido de:",Def,"No puede habilitar")
elif Def < 3.0:
    print("Su definitiva ha sido de:",Def,"Reprobó la materia")
elif Def >= 3.0 and Def<4.5:
    print("Su definitiva ha sido de:",Def,"Ha aprobado la materia")
if Def >= 4.5:
    print("Su definitiva ha sido de:",Def,"Felicitaciones, aprobó con un buen promedio :)")

