import os
from unittest import case 

os.system("cls || clear")

 #menu
 
print("Bem-vindo ao cardápio do restaurante!")
 
print ("""
 ==========MENU==========
 
    CODIGO |     PRATO      |   PREÇO
     1     | PICANHA        |  R$ 25,00
     2     | LASANHA        |  R$ 20,00
     3     | STROGONOFF     |  R$ 18,00
     4     | BIFE ACEBOLADO | R$ 15,00
     5     | PÃO COM OVO    | R$ 5,00
  
     """)
 
codigo = int(input("Digite o código do prato que deseja pedir: "))

match codigo:

    case 1:
        print("Você pediu PICANHA  VALOR R$ 25,00")
    case 2:
        print("Você pediu LASANHA  VALOR R$ 20,00")
    case 3:
        print("Você pediu STROGONOFF  VALOR R$ 18,00")
    case 4:
        print("Você pediu BIFE ACEBOLADO  VALOR R$ 15,00")
    case 5:
        print("Você pediu PÃO COM OVO  VALOR R$ 5,00")
    case _:
        print("Prato não encontrado")



print ("\nFim do programa")