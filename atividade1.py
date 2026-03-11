import os

os.system("clear")
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 100.")
import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
    

print("Obrigado por jogar!")

#danterks
