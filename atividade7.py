import os

os.system("cls")

# Solicita as 3 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Mostra a média
print(f"Média: {media:.2f}")

# Verifica a situação do aluno
if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("Recuperação")
    
    
print("\n fim de programa")