import os

#limpa o terminal

os.system("cls || clear")

#repetidor

while True:


#entrada de dados

 a = float(input("digite o primeiro numero:"))
 b = float(input("digite o segundo numero:"))

#calcule

 soma = a + b
 subtracao = a - b
 multiplicacao = a * b
 divisao = a / b

#resultado

 print ("\n---RESULTADO---:")
 print (f"soma: {soma:.2f}")
 print (f"subtração: {subtracao:.2f}")
 print (f"multiplicação: {multiplicacao:.2f}")
 print (f"divisão: {divisao:.2f}")

 print("\n-------programa finalizado.-------")
 print("\n" * 2)
 