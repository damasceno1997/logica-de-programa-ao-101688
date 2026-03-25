import os 

os.system ("cls || clear")

# criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 3

print ('adicionando 3 notas.')
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"digite a {i+1}ª nota:"))
    vetor_notas.append(nota)
    
    print ('\nexibindo as notas informadas') 
    #forEach
    for uma_nota in vetor_notas:
        print (f"nota: {uma_nota}")