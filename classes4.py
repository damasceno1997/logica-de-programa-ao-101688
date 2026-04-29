import os
from dataclasses import dataclass

os.system("cls")

#definindo uma classe
@dataclass
class Cliente:
    nome: str            #definbir um atributo string é texto
    email:  str          #definir um atributo int é número inteiro
    telefone: str

print ("== solicitando dados do cliente ==")
cliente = Cliente(
    nome= input("Digite seu nome: "),
    email= input("Digite seu email: "),
    telefone= input("Digite seu telefone: \n")
)
os.system("cls")
print ("== exibindo dados do cliente ==")
print (f"nome: {cliente.nome}")
print (f"email: {cliente.email}")
print (f"telefone: {cliente.telefone}\n")