import os

#limpando terminal

os.system ("cls || clear")
  
  #coleta de dados 
  
while True:
  
   nome = input("digite seu login: ")
   senha = input("digite sua senha: ")

  #verificação de dados
   if nome == "danilodamasceno@gmail.com" and senha == "13051899":
    print("\nAcesso permitido")
    print("Bem-vindo!")
   else:
    print("Acesso negado")  
  
    
   print("\nFim do programa")