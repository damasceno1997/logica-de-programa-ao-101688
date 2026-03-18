import os 

os.system (" cls || clear")


while True:

  n1 = (float(input("Digite a primeira nota: ")))
  n2 = (float(input("Digite a segunda nota: ")))
  n3 = (float(input("Digite a terceira nota: ")))


  if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10 and n3 >= 0 and n3 <= 10:
    media = (n1 + n2 + n3) / 3
    print(f"\n A média do aluno é: {media:.2f}")
    break
    
else:
    print("\nNota inválida! As notas devem ser entre 0 e 10.")

  
if media >= 7:
    print("\nAluno aprovado!")
elif media >= 5 and media < 7:
    print("\nAluno em recuperação!")
else:
    print("\nAluno reprovado!")
    
print("\nPrograma encerrado.")

