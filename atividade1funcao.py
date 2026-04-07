import os

os.system("cls")

#funçao com  párametro
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    # exemplo de uso da função

numero = int(input("Digite um número para ver a tabuada: "))

#chamando a funçao
#enviando parametros
tabuada(numero)