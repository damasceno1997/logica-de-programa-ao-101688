import os 

os.system ("cls || clear")

# criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 2

print (f'adicionando {QUANTIDADE_NOTAS} notas.')
for i in range(QUANTIDADE_NOTAS):
 nota = float(input(f"digite a {i+1}ª nota:"))
 #adicionar nota no vetor
vetor_notas.append(nota)
    
    
#sum (valor) = soma todas os valores do vetor.
media = sum (vetor_notas) / QUANTIDADE_NOTAS
    
print ('\nexibindo as notas informadas') 
    #forEach= percorre o vetor sem informar a quantidade.
    #enumerate = atarves da variavel i, numera a qiantidade de repetiçoes.
for i, uma_nota in enumerate (vetor_notas, start=1):
        print (f"{i}ª nota: {uma_nota}")
        
print (f"media: {media:.2f}") 