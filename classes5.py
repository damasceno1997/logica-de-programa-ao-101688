import os
from dataclasses import dataclass

os.system("cls")

#definindo uma classe
@dataclass
class paciente:
    nome: str            #definbir um atributo string é texto
    idade:  int         #definir um atributo int é número inteiro
    peso: str
    altura: str

print ("== solicitando dados do paciente ==")
paciente = paciente(
    nome= input("Digite seu nome: "),
    idade= int(input("Digite sua idade: ")),
    peso= input("Digite seu peso: "),
    altura= input("Digite sua altura: \n")
)
os.system("cls")
print ("== exibindo dados do paciente ==")
print (f"nome: {paciente.nome}")
print (f"idade: {paciente.idade}")
print (f"peso: {paciente.peso}")
print (f"altura: {paciente.altura}\n")



