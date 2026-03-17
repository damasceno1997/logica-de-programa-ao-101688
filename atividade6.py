import os 
import time 

os.system ("cls")


soma = 0 

quantidade_notas = 5

for i in range(quantidade_notas):
    nota = int(input("digite uma nota:"))
    soma += nota
    
    
media = soma / quantidade_notas

print (f"media: {media}")    