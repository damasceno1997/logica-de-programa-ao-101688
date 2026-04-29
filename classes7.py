import os
from dataclasses import dataclass

os.system("cls")

#definindo uma classe
@dataclass
class Cliente:
    nome: str            #definbir um atributo string é texto
    email:  str          #definir um atributo int é número inteiro
    telefone: str
    

    def mostrar_dados(self):
        print (f"nome: {self.nome}")
        print (f"email: {self.email}")
        print (f"telefone: {self.telefone}\n")


print ("== solicitando dados do cliente ==")
cliente = Cliente(
    nome= input("Digite seu nome: "),
    email= input("Digite seu email: "),
    telefone= input("Digite seu telefone: \n")
)

print ("== exibindo dados do cliente ==")
cliente.mostrar_dados()
