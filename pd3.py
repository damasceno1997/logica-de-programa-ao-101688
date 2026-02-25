import os

os.system (" cls || clear")


print ("quantas maças você deseja?")
macas = int(input())

if macas< 12:
    preco = 1.30

if macas>= 12: 
    preco = 1.00

print(f"valor total da compra: {preco}")


print ("\n__________programa finalizado.__________")