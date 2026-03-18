import os

#limpar o terminal
os.system ("cls || cler")



#repetiçao
while True:
    
    #entrada de dados
   nota = float(input("Digite a nota do aluno: "))
    
    #verificaçao de nota
   if nota >= 0 and nota <= 10:
       #exibir a nota do aluno
     print(f"\n a nota do aluno é: {nota}")
     #parar a repetiçao
     break
 
   # se a nota for invalida vai mostar a mensagem de erro e solicitar a nota novamente
   else: 
        print(f"\nNota inválida! A nota deve ser entre 0 e 10.")
        
    #finalizar o programa
print("\nPrograma encerrado.") 
 
 
