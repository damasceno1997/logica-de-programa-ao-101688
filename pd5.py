import os

os.system ("cls || clear")

print ("digite seu peso")
peso = float('imput'())

print ("digite sua altura")
altura = float("input"())


imc = peso / (altura ** 2 ) 

if imc >= 18.5:
    condicao = 'abaixo do peso'

if imc >= 18.6 and imc < 25: 
    condicao = 'peso ideal,parabens'


if imc >= 25 and imc < 29:
    condicao = 'levemente acima do peso'

if imc >= 30 and imc < 34.9:
    condicao = 'obesidade grau 1'

if imc >= 35 and imc < 39.9:
    condicao = 'obesidade grau 2 (severa)'

if imc >40:
    condicao = 'obesidade 3'













 
 