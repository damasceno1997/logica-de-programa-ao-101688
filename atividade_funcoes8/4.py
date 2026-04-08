import os

os.system ("cls || clear")
def logo ():
    print("==========")
    print('  SENAI  ')
    print("==========")

#funçao com parametro e semretono
def somar(a, b):
    return a + b

#funçao com parametro e com retorno
def subtrair(a, b):
    return a - b

#funçao com parametro e sem retorno
def multiplicar(a, b):
    print (f"multiplicação = {a * b}")

def divisao(a, b):
        return a / b


logo()
print ("= solicitando dados =")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
divisao = divisao(n1, n2)

logo()
print ("= exibindo resultado =")
print (f"soma = {soma}")
print (f"subtração = {subtracao}")
multiplicar (n1, n2)
divisao (n1, n2)

