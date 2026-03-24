import os

os.system ("cls || clear")

soma_notas = 0
quantidade_notas = 0

print ("bem vindo ao prograna de calculo de notas")
nota = float(input("Digite a nota: "))
soma_notas += nota


#pergutar ao usuario se deseja adicionar mais uma nota
while True:
    resposta = input("Deseja adicionar mais uma nota? (s/n): ")
    if resposta.lower() == "s":
        nota = float(input("Digite a nota: "))
        soma_notas += nota
        quantidade_notas += 1
    elif resposta.lower() == "n":
        break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
        
if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"A média das notas é: {media:.2f}")
    
    
print ("\nprograma finalizado")