import os
from dataclasses import dataclass

os.system("cls")

#definindo uma classe
@dataclass
class fornecedor:
    nome: str            #definbir um atributo string é texto
    email:  str        #definir um atributo int é número inteiro
    telefone: str
    endereço: str

    def mostrar_dados(self):
        print (f"nome: {self.nome}")
        print (f"email: {self.email}")
        print (f"telefone: {self.telefone}")
        print (f"endereço: {self.endereço}\n")


print ("== solicitando dados do fornecedor ==")
os.system("cls")
fornecedor = fornecedor(
    nome= input("Digite o nome do fornecedor: "),
    email= input("Digite o email do fornecedor: "),
    telefone= input("Digite o telefone do fornecedor: "),
    endereço= input("Digite o endereço do fornecedor: \n")
)


print ("== exibindo dados do fornecedor ==")
fornecedor.mostrar_dados()

