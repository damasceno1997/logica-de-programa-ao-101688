import os 

os.system("cls || clear")

vetor = []

for i in range(5):
    numero = float(input("Digite um número: "))
    if numero < 0:
        vetor.append(0)
    else:
        vetor.append(numero)

print("Os valores do vetor são:", vetor)

