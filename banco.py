import os 

os.system ("cls || clear")

print ("\n======= bem vindo ao menu do banco itau =======\n")

print ("1 - criar usuario")
print ("2 - sacar")
print ("3 - depositar")
print ("4 - extrato")
print ("5 - sair")

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    saldo = float(input("Digite o saldo inicial do usuário: "))
    return nome, saldo



def sacar (saldo):
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor_saque
        print(f"Saque realizado com sucesso. Saldo atual: {saldo:.2f}")
    return saldo


def depositar (saldo):
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    print(f"Depósito realizado com sucesso. Saldo atual: {saldo:.2f}")
    return saldo


def extrato (saldo):
    print(f"Saldo atual: R${saldo:.2f}")
saldo = 0.0



while True:
    
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        nome, saldo = criar_usuario()
    elif opcao == "2":
        saldo = sacar(saldo)
    elif opcao == "3":
        saldo = depositar(saldo)
    elif opcao == "4":
        extrato(saldo)
    elif opcao == "5":
        print("seçao finalizada Obrigado por usar o banco itau!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")