import os

os.system("cls || clear")

#faça uma funçao que receba um valor inteiro e verifioca se o valor é positivo ou negativo 

def positivo_ou_negativo(numero):
    if numero > 0:
        print(f"O numero {numero} é positivo.")
    elif numero < 0:
        print(f"O numero {numero} é negativo.")
    else:
        print("O numero é zero.")

numero = int(input("Digite um numero: "))
positivo_ou_negativo(numero)




