soma = 0
contador = 0

while True:
    numero = int(input("Digite um número positivo (negativo para sair): "))
    
    if numero < 0:
        break  # encerra o loop
    
    soma += numero
    contador += 1

# cálculo da média
if contador > 0:
    media = soma / contador
    print(f"\nMédia dos valores: {media:.2f}")
else:
    print("Nenhum valor positivo foi informado.")
    
print