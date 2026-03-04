import os

os.system("cls || clear")

while True:

 n1 = int(input("\nDigite o primeiro número: "))
 n2 = int(input("Digite o segundo número: "))    
 caracter = input("digite uma caractere: ")
 calculos = n1, n2, caracter


 match calculos:
    case n1, n2, "+":
        
        print(f"\nA soma de {n1} + {n2} é igual a: {n1 + n2}")
    case n1, n2, "-":
        print(f"\n a subtração de {n1} - {n2} é igual a: {n1 - n2}")
    case n1, n2, "*":
        print(f"\n a multiplicação de {n1} * {n2} é igual a: {n1 * n2}")
    case n1, n2, "/": 
        if n2 != 0:
          print(f"\n a divisão de {n1} / {n2} é igual a: {n1 / n2:.2f}")
        else:
          print("Erro: Divisão por zero não é permitida.")
            
            
print("\nFim do programa")


    
    
    
    