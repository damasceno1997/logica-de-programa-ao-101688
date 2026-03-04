import os

#limpando terminal
os.system("cls || clear")


print("\nBem-vindo ao sistema de faltas do senai")


#coleta de dados

while True:
    
    nome = input ("\ndigite seu nome: ")
    faltas = int(input (" digite seu número de faltas: "))
    media = float(input (" digite sua média: "))
    
    
    #analise de dados
    
    if faltas <= 40 and media >= 7.0:
        print("\nparabens voce foi aprovado!")
    else:
        print("\nAluno reprovado.")

    
print("\nFim do programa")  