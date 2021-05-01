#Ejercicio 34
A = int(input("Ingrese el coeficiente de la variable cuadrática:"))
B = int(input("Ingrese el coeficiente de la variable líneal:"))
C = int(input("Ingrese el término independiente:"))
if ((B**2)-4*A*C) < 0:
      print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+((B**2-(4*A*C))**0.5))/(2*A)
  x2 = (-B-((B**2-(4*A*C))**0.5))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)