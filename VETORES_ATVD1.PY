import os

os.system ("cls || clear")


# criando um vetor.
vetor_notas = []


#adicionando 3 notas.
for i in range(3):
    nota = float(input("digite uma nota"))
    vetor_notas.append(nota)
    
    #exibindo as notas informadas 
    
    for i in range (3):
        print (f"nota: {vetor_notas [i]}")
                                                            