abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
"p","q","r","s","t","u","v","w","x","y","z"]

for letra in range(len(abecedario),1,-1):
    if letra%3 == 0:
        abecedario.pop(letra-1)

print(abecedario)