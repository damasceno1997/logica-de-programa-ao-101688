import os

#limpa o terminal.
os.system("cls")

print("- solicitando dados -") 

nome = input ("digite seu nome:") 

primeira_nota = float(input("digite a primeira nota: "))
segunda_nota = float(input("digite a sua segunda nota: "))
...
#calcule

média = (primeira_nota + segunda_nota)

#mostre a media

print (f"a média de {nome:} é: {média:.2f}")

