#ejemplo 1
nombres = ["David","Carlos","Juan","Diego"]
adjetivos = ["Es grande", "Es divertido", "Es estudioso", "Es pequeño"]

for n in nombres:
    for b in adjetivos:
        print(n,b)

#EJEMPLO 2

for num in range(20,0,-1):
    for num2 in range(3):
        print (num,num2)