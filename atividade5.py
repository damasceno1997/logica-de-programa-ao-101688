import os

os.system ('cls || clear')

# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos das famílias da cidade. A prefeitura deseja saber:   a) total de famílias que responderam a pesquisa; b) média do salário da população;c) média do número de filhos; d) maior salário; e) menor salário. Crie um menu com duas opções. Código |   Descrição      1         |   Adicionar família      2        |   Sair e exibir resultadosO final da leitura de dados se dará com quando o usuário digitar o número código 2. 


print ("Bem vindo ao programa de pesquisa de dados")

salarios = []
filhos = []

while True:
    print("\nMenu:")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")
    
    opcao = input("Digite o código da opção desejada: ")
    
    if opcao == "1":
        os.system ('cls || clear')
        salario = float(input("Digite o salário da família: "))
        numero_filhos = int(input("Digite o número de filhos da família: "))
        
        salarios.append(salario)
        filhos.append(numero_filhos)
        
    elif opcao == "2":
        break
    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")
        
if len(salarios) > 0:
    total_familias = len(salarios)
    media_salario = sum(salarios) / total_familias
    media_filhos = sum(filhos) / total_familias
    maior_salario = max(salarios)
    menor_salario = min(salarios)
    
    print(f"Total de famílias que responderam a pesquisa: {total_familias}")
    print(f"Média do salário da população: R$ {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário: R$ {maior_salario:.
2f}")
    print(f"Menor salário: R$ {menor_salario:.2f}")
else:
    print("Nenhuma família cadastrada.")
    
print ("\nPrograma finalizado")