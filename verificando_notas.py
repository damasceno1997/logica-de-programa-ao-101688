import os

os.system("cls || clear")

nota = int(input("Digite uma nota: "))

if nota >=0 and nota <= 10:
    print("essa nota esta entre 0 e 10.")   
else:
    print("a nota deve ser entre 0 e 10")
    
print ("\nFim do programa")