#fazer um programa que solicita o preço de um produto e inflaciona esse preço em 10%  se ele for menor que 100 e 20% se ele for maior ou igual a 100. utilize uma funçao com retornop para obter o resulktado solicitado


import os

os.system ("cls || clear")

def inflacionar (preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20
    
preco = float(input("Digite o preço do produto: "))
preco_inflacionado = inflacionar(preco)
print(f"O preço inflacionado do produto é: R$ {inflacionar(preco):.2f}")


print("\nprograma finalizado")