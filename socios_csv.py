import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class socio:
    nome: str
    cpf: str
    telefone: str

QUANTIDADE_SOCIOS = 0
listas_socios = []

while True:

    print ('== sistema de cadastro ==')
    print (' 1 - adicionar sócio ' )
    print (' 2 - listar sócios ')
    print (' 3 - sair ')

    opção = input('Digite a opção desejada: ')
    
    if opção == '1':
        print('== Solicitando dados ==')
        novo_socio = socio(
            nome=input('Digite seu nome: '),
            cpf=input('Digite o CPF: '),
            telefone=input('Digite seu telefone: ')
        )

        print('== Salvando dados ==')
        with open('novos_socios.csv', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{novo_socio.nome}, {novo_socio.cpf}, {novo_socio.telefone}\n')
                print('Salvo com sucesso!')

    elif opção == '2':
            print('== Listando sócios ==')
            with open('novos_socios.csv', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    nome, cpf, telefone = linha.strip().split(',')
                    listas_socios.append(socio(
                        nome=nome,
                        cpf=cpf,
                        telefone=telefone
                    ))

            for socio in listas_socios:
                print(f'Nome: {socio.nome}')
                print(f'CPF: {socio.cpf}')
                print(f'Telefone: {socio.telefone}\n')

    elif opção == '3':
        print('== Saindo do programa ==')
        break
    