import os

os.system (" cls || clear")




print ("digite seu nome")
nome = (input())

print ("digite sua primeira nota")
nota1 = float(input())


print ("digite sua segunda nota")
nota2 = float(input())

media = (nota1 + nota2) /2

if media >= 9:
    conceito = 'A'

if media >= 7.5 and media <9: 
    conceito = 'B'


if media >= 6 and media < 7.5:
    conceito = 'C'

if media >= 4 and media < 6:
    conceito = 'D'

if media < 4:
    conceito = 'E'

if conceito in['A', 'B','C']:


     print ("aprovado.")

else: 
    print ("reprovado👎")



print ('\n--------------programa finalizado.----------------')    


print('\n' * 3 )

