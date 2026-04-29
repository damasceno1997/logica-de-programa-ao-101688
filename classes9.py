import os
from dataclasses import dataclass

os.system("cls")

#definindo uma classe
@dataclass
class endereco:
    logradouro: str           #definbir um atributo string é texto
    numero: int           #definir um atributo int é número int


@dataclass
class cliente:
    nome: str            #definbir um atributo string é texto
    idade:  int         #definir um atributo int é número inteiro
    endereço: endereco


    def mostrar_dados(self):
        print (f"nome: {self.nome}")
        print (f"idade: {self.idade}")
        print (f"logradouro: {self.endereço.logradouro}")
        print (f"numero: {self.endereço.numero}\n")


print ("== solicitando dados do fornecedor ==")
cliente = cliente (
    nome= input("Digite o nome do fornecedor: "),
    idade= int(input("Digite a idade do fornecedor: ")),
    endereço= endereco(
        logradouro= input("Digite o logradouro do fornecedor: "),
        numero= int(input("Digite o número do fornecedor: "))
    
))


print ("== exibindo dados do fornecedor ==")
cliente.mostrar_dados()