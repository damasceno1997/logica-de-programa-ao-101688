import os
import time


os.system(" cls || clear")


#contagem regressiva ate  o numero 1

numero = int(input("Digite um número para iniciar a contagem regressiva: "))

for i in range ( numero, 0, -1):
        print(i)
        #espera 1 segundos
        time.sleep(1) 


print ("\nFim da contagem regressiva!")