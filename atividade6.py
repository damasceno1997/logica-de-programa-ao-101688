import os 

os.system ("cls || clear")


soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    
    soma += nota
    contador += 1
    
    resposta = input("Deseja inserir outra nota? (s/n): ").lower()
    
    if resposta == "n":
        break
    elif resposta != "s":
        print("Resposta inválida! Encerrando...")
        break

# cálculo da média
if contador > 0:
    media = soma / contador
    print(f"\nMédia das notas: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")
