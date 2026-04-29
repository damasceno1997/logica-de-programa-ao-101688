import os
from dataclasses import dataclass

os.system ("cls")

#definindo uma classe
@dataclass
class Cliente:
    nome: str            #definbir um atributo string é texto
    email:  str          #definir um atributo int é número inteiro
    telefone: str

@dataclass
class Funcionario:
    nome: str
    email: str
    matricula: str
    setor: str

cliente1 = Cliente ('Maria', 'maria@email.com', '71 98873-8233')

Funcionario1 = Funcionario ('matheus', 'matheus@email.com', '12345', 'TI')


# print (f"nome: {cliente1.nome} , email: {cliente1.email} , telefone: {cliente1.telefone}")
print (f"nome: {cliente1.nome}")
print (f"email: {cliente1.email}")
print (f"telefone: {cliente1.telefone}\n,")

print (f"nome: {Funcionario1.nome}")
print (f"email: {Funcionario1.email}")
print (f'matricula: {Funcionario1.matricula}')
print (f"setor: {Funcionario1.setor}")

