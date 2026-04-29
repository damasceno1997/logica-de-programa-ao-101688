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

print ("== solicitando dados do fornecedor ==")
fornecedor = fornecedor(
    nome= input("Digite o nome do fornecedor: "),
    email= input("Digite o email do fornecedor: "),
    telefone= input("Digite o telefone do fornecedor: "),
    endereço= input("Digite o endereço do fornecedor: \n")
)


os.system("cls")
print ("== exibindo dados do fornecedor ==")
print (f"nome: {fornecedor.nome}")
print (f"email: {fornecedor.email}")
print (f"telefone: {fornecedor.telefone}")
print (f"endereço: {fornecedor.endereço}\n")

