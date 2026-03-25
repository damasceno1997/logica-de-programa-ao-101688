import os

os.system ("cls || clear")


vetor_numeros = []
QUANTIDADE_NUMEROS = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_total = 0 
soma_total = 0
soma_pares = 0 

print (f'adicionando {QUANTIDADE_NUMEROS} numeros.')
for i in range(QUANTIDADE_NUMEROS):
 numero = int(input(f"digite o {i+1}ª numero:"))
 #adicionar nota no vetor
vetor_numeros.append(numero)
    
    
for uma_nota in vetor_numeros:
    
    if uma_nota % 2 == 0:
        quantidade_pares += 1 

    
print ('\nexibindo os numeros informados') 



if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0
    
if quantidade_total > 0:
    media_geral = soma_total / quantidade_total
else:
    media_geral = 0
    
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")