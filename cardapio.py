import os

os.system ("cls || clear")

while True:
    print("Bem-vindo ao cardápio do restaurante!")

    print("\n 1 - picanha - R$ 25,00")
    print("\n 2 - lasanha - R$ 20,00")
    print("\n 3 - strogonoff - R$ 18,00")
    print("\n 4 - bife acelebolado - R$ 15,00")
    print("\n 5 - pao com ovo - R$ 5,00")
    
    escolha = input("\nDigite o número do prato que deseja pedir: ")
    if escolha == "1":
        print("\nVocê escolheu picanha. O valor é R$ 25,00.")
    elif escolha == "2":
        print("\nVocê escolheu lasanha. O valor é R$ 20,00.")
    elif escolha == "3":
        print("\nVocê escolheu strogonoff. O valor é R$ 18,00.")
    elif escolha == "4":
        print("\nVocê escolheu bife acelebolado. O valor é R$ 15,00.")
    elif escolha == "5":
        print("\nVocê escolheu pão com ovo. O valor é R$ 5,00.")
    else:
        print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")
        
    continuar = input("\nDeseja fazer outro pedido? (sim/não): ")
    if continuar.lower() != "sim":
        print("\nObrigado por visitar nosso restaurante! Volte sempre!")
        break
    
print("\n fim de programa")
    
    

        
        