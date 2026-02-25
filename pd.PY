import os

os.system ("cls || clea")

print ("digite um numero")
numero1 = int(input())

print ("digite o segundo numero")
numero2 = int(input())

media = (numero1 + numero2) /2
soma = (numero1 + numero2)
produto = (numero1 * numero2)
menor = min(numero1, numero2)
maior = max(numero1, numero2)


print ("\n-----resultados-----\n")
print (f'média: {media}')
print (f'soma: {soma}')
print (f'produto: {produto}')
print (f'menor: {menor}')
print (f'maior: {maior}')

if numero1 == numero2:
    print ('os numeros são iguais.')

else:
    print('os numero são diferentes.')

print ('\nfim do programa.')
print ('\n' * 4) 
