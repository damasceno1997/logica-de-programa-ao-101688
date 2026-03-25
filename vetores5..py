import os 

os.system ("cls || clear")

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

print (f'adicionando {QUANTIDADE_NUMEROS} numeros.')
for i in range(QUANTIDADE_NUMEROS):
 numero = int(input(f"digite o {i+1}ª numero:"))
 #adicionar nota no vetor
vetor_numeros.append(numero)
    
    

    
print ('\nexibindo os numeros informados') 
 
for i, um_numero in enumerate (vetor_numeros, start=1):
        print (f"numeros: {QUANTIDADE_NUMEROS}")
        
print (f"numero_maior: {vetor_numeros:.2f}") 


