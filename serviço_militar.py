import os

#limpando terminal

os.system("cls || clear")

print("\n Seja bem vindo ao serviço militar obrigatorio")

#coleta de dados

sexo = input("\nDigite seu sexo (MASCULINO/FEMININO): ") .lower()
ano_de_nascimento = int(input("Digite sua data de nascimento (exemplo 1999): "))
idade = 2026 - ano_de_nascimento

#analise/saida de dados

if idade >= 18 and sexo == "masculino":
    print("\nVocê é obrigado a se alistar no serviço militar.")
else:
    print("\nVocê não é obrigado a se alistar no serviço militar.") 
    
print("\nFim do programa") 