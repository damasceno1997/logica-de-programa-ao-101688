import os

os.system("cls || clear")

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O numero {numero} é pár.")
    else:
        print(f"o numero {numero}é impar.")

        numero = int(input("digite um numero:"))
        par_ou_impar(numero)


