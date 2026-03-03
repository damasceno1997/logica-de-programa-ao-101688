import os

os.system ("cls || clear")

#coleta de dados

nome = input("nome do empregado:")

matricula = int (input("digite sua matricula:"))

nascimento = int(input("digite seu ano de nascimento:"))

tempo = int (input("digite seu tempo trabalhado:"))

#processamento

idade = 2026 - nascimento

if idade >= 65 or tempo >= 30:
    resultado = ("requerer aposentadoria")
    
    
else: 
    resultado = ('não requerer aposentadoria')
    
    print ("\n-----resultado-----")
    print (f"idade: {idade} ")
    print (f'tempo: {tempo}')
    print (f"matricula {matricula}")
    print (f"frequerimento {resultado}")
    



