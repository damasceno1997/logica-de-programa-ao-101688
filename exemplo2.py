import os

os.system("cls")

def saudacao(nome):
    print(f"Olá, {nome}!")
    print("Seja bem-vindo ao nosso site!")

    # exemplo de uso da função

nome_visitante = input("Digite seu nome: ")
saudacao (nome=nome_visitante)