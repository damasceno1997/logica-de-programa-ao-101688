# fazer um programa que solicita um valor em metros e por meio da funçao, funçao retorna o correspodente em centimetros

import os

os.system ("cls || clear")
def logo ():
    print("==========")
    print('  SENAI  ')
    print("==========")

def centimetros(metros):
    return metros * 100

logo()
metros = float(input("Digite quantos metros: "))
resultado = centimetros(metros)
print(f"{metros} metros equivalem a {resultado} centímetros.")

print("\nprograma finalizado")
