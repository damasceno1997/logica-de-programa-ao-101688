import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class livro:
    nome: str
    autor: str
    categoria: str
    preço: str


QUANTIDADE_LIVROS = 0
listas_livros = []

while True:
    print ('== sistema de cadastro ==')
    print (' 1 - adicionar livro ' )
    print (' 2 - listar livros ')
    print (' 3 - sair ')



    opção = input('Digite a opção desejada: ')
    
    if opção == '1':
        print('== Solicitando dados ==')
        novo_livro = livro(
            nome=input('Digite o nome do livro: '),
            autor=input('Digite o nome do autor: '),
            categoria=input('Digite a categoria do livro: '),
            preço=input('Digite o preço do livro: ')
        )

        print('== Salvando dados ==')
        with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{novo_livro.nome}, {novo_livro.autor}, {novo_livro.categoria}, {novo_livro.preço}\n')
                print('Salvo com sucesso!')

    elif opção == '2':
            print('== Listando livros ==')
            with open('catalogo_livros.csv', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    nome, autor, categoria, preço = linha.strip().split(',')
                    listas_livros.append(livro(
                        nome=nome,
                        autor=autor,
                        categoria=categoria,
                        preço=preço
                    ))

            for livro in listas_livros:
                print(f'Nome: {livro.nome}')
                print(f'Autor: {livro.autor}')
                print(f'Categoria: {livro.categoria}')
                print(f'Preço: {livro.preço}\n')

    elif opção == '3':
        print('== Saindo do programa ==')
        break

    else:
        print('Opção inválida. Por favor, tente novamente.\n')

