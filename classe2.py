import os
from dataclasses import dataclass

os.system ("cls")

@dataclass 
class Pessoa:
    nome: str
    idade: int

@dataclass # criador de classes
class Pet:
    nome: str #string é texto
    idade: int #inteiro é número inteiro

#usando uma classe
pessoa1 = Pessoa("Julia", 17)
pessoa2 = Pessoa("Amanda", 19)

pet1 = Pet("Totó", 4)
pet2 = Pet("Tom", 2)

print (f"nome: {pessoa1.nome} \nIdade: {pessoa1.idade}\n")
print (f"nome: {pessoa2.nome} \nIdade: {pessoa2.idade}\n")

print (f"nome: {pet1.nome} \nIdade: {pet1.idade}\n")
print (f"nome: {pet2.nome} \nIdade: {pet2.idade}\n")