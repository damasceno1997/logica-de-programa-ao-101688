import os

os.system ('cls || clear')

#Foram coletados os dados de idade, sexo (M/F) e salário.  Faça um algoritmo que informe:  a) a média de salário do grupo;b) maior e menor idade do grupo; c) quantidade de mulheres com salário a partir de R$ 5.000,00.Crie um menu com três opções.Código |   Descrição       1        |   Adicionar pessoa        2       |   Exibir resultados        3       |   Sair O final da leitura de dados se dará com quando o usuário digitar o número código 3. Ao adicionar uma pessoa, deve-se limpar o terminal e apresentar o menu novamente.

print ("Bem vindo ao programa de coleta de dados")

idades = []
sexos = []
salarios = []

while True:
    print("\nMenu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    opcao = input("Digite o código da opção desejada: ")
    
    if opcao == "1":
        os.system ('cls || clear')
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: "))
        
        idades.append(idade)
        sexos.append(sexo)
        salarios.append(salario)
        
    elif opcao == "2":
        if len(salarios) > 0:
            media_salario = sum(salarios) / len(salarios)
            maior_idade = max(idades)
            menor_idade = min(idades)
            quantidade_mulheres_salario_alto = sum(1 for s, sal in zip(sexos, salarios) if s == "F" and sal >= 5000)
            
            print(f"Média de salário do grupo: R$ {media_salario:.2f}")
            print(f"Maior idade do grupo: {maior_idade} anos")
            print(f"Menor idade do grupo: {menor_idade} anos")
            print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres_salario_alto}")
        else:
            print("Nenhuma pessoa cadastrada.")
            
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")
        
print ("\nPrograma finalizado")