import os 

os.system ("cls || clear")

tentativas = 0

while tentativas < 3:
    

    login = input("digite seu login: ")
    senha = int(input("digite sua senha: "))
    
    if login == "danilodamasceno2007@gmail.com" and senha == 12345678:
        print("\nLogin bem-sucedido!")
        break
    else:
        print("\nlogin ou senha incorretos> tente novamente")
        
    tentativas += 1 
    if tentativas == 3:
        print("\nNúmero máximo de tentativas atingido. Acesso bloqueado.")
        break