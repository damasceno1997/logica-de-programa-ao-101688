import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def calcular_imc(peso, altura):
    return peso /  altura ** 2

def  classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"
    
    
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []


# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()

    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    # Verificando se o usuário quer sair

    if nome.lower() == 'sair':
        break

sobrenome = input("Digite o sobrenome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
altura = float(input("Digite a altura do usuário (em metros): "))
peso = float(input("Digite o peso do usuário (em quilogramas): "))



idade = int(input("Digite a idade do usuário: "))
altura = float(input("Digite a altura do usuário (em metros): "))
peso = float(input("Digite o peso do usuário (em quilogramas): "))


    # Adicionando os dados às listas
nomes.append(nome)
sobrenomes.append(sobrenome)
idades.append(idade)
alturas.append(altura)
pesos.append(peso)


# Exibindo os dados armazenados

logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("sobrenome:", sobrenomes[i])
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    imc = calcular_imc(pesos[i], alturas[i])
    classificacao = classificar_imc(imc)
    print("IMC:", round(imc, 2))
    print("Classificação:", classificacao)
    print("-" * 20)

    





