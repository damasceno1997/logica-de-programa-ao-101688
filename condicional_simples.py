import os

# limpa o terminal
os.system("cls || clear")


idade= int(input("digite a sua idade: "))

#condicional simples.
if idade < 18:
   print ("acesso negado.")
else:
    print ("Acesso permitido.")


print ("programa encerrado.")


