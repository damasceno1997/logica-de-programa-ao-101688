import os

os.system("cls")

#funçao com  párametro
def saudacao(n1,n2):
    soma = n1 + n2
    print(f"soma: {soma}")

    # exemplo de uso da função

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#chamando a funçao
#enviando parametros
somar = saudacao(primeiro_numero, segundo_numero)