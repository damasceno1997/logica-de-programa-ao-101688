Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis 
    nome: caractere
    idade:inteiro
   primeira_nota: real
   segunda_nota: real
   soma: real
   media:real
    resultado:caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   //entrada de dados
   
    escreva ("digite seu nome:")
     leia (nome)
     
     escreva ("digite sua idade")
       leia (idade)
       
   escreva("digite a primeira nota:")
   leia (primeira_nota)
   
   
   escreva("digite a segunda nota:")
   leia (segunda_nota)

    //processamneto

   soma <- primeira_nota + segunda_nota
   media <- soma / 2
   
   //media <- primeira_nota + segunda_nota / 2
   
   se media >= 7 entao
   resultado <- "aprovado"
   
   senao
   
   resultado <- "reprovado"
   
   fimse
   
   //saida
   escreval
   escreval ("seu nome:" , nome)
   escreval ("sua idade:" , idade)
   
   escreval("esta é a soma das notas", soma)
   escreval ("esta é a media das notas", media)
   escreval
    escreval ("voce está ", resultado)
    
Fimalgoritmo