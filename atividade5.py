import os

os.system ("cls || clear")



total = 0

while True:
    codigo = int(input("\nDigite o código do prato (1 a 5): "))

    if codigo == 1:
        valor = 25.00
    elif codigo == 2:
        valor = 20.00
    elif codigo == 3:
        valor = 18.00
    elif codigo == 4:
        valor = 15.00
    elif codigo == 5:
        valor = 5.00
    else:
        print("Código inválido!")
        continue  # volta pro início do loop

    print(f"Valor do prato: R${valor:.2f}")
    total += valor  # soma ao total

    resposta = input("\nDeseja escolher outro prato? (s/n): ").lower()

    if resposta == "n":
        break
    elif resposta != "s":
        print("Resposta inválida! Encerrando...")
        break

print(f"\nTotal a pagar: R${total:.2f}")
print("Programa encerrado.")




