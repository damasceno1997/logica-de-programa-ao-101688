import os 

os.system ('cls || clear')

#calcule a media ritimetica de varios valores positivos inseridos pelo usuario, o final da leitura acontecera quando o usuario digitar um valor negativo. mostre a media ritimetica dos valores inseridos

soma_inversos = 0
quantidade_valores = 0
print ("Bem vindo ao programa de calculo de media ritimetica")
while True:
    valor = float(input("Digite um valor positivo (ou um valor negativo para finalizar): "))
    if valor < 0:
        break
    soma_inversos += 1 / valor
    quantidade_valores += 1
    
if quantidade_valores > 0:
    media_ritimetica = quantidade_valores / soma_inversos
    print(f"A média ritimetica dos valores inseridos é: {media_ritimetica:.2f}")
    
print ("\nPrograma finalizado")