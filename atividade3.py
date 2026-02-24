import os

os.system ("cls || clear")

nota1 = float(input ("digite sua primeira nota:"))
nota2 = float(input ("digite sua segunda nota:"))
nota3 = float(input ("digite sua terceira nota:"))


media = (nota1 + nota2 + nota3) /3

print (f"A media das notas é: {media:.2f}")

if media >= 7:
    resultado = "aprovado"

else:
    resultado = "reprovado"

print ("exibindo dados")    
print (f"media:{media}")
print (f"resultado:{resultado}")