# 4. Lista de compras

# Usuário pode adicionar itens a uma lista.
# Use for para exibir todos os itens ao final.
# Use while para permitir adicionar até o usuário digitar "sair".

import os
import time

def tracado(vezes):
    return print('-' * vezes)

def animacao_espera():
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print() 

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

TITULO = 'Bem vindo a sua Lista de Compras'
NEGATIVA = ['n', 'nao', 'não']

lista = []

while True:

    limpar_terminal()
    print('\n' + TITULO.center(125, '-'))
    
    if lista: #Exibe os itens da lista atual em sequência
        print('Lista')
        tracado(60)
        for i, lista_final in enumerate(lista, start=1):
            print(f'{i}. {lista_final}')
        tracado(60)

        continuar = input('\nDeseja continuar adicionando (Sim/Não)?: ').lower().strip()

        if continuar in NEGATIVA: #Encerra o programa
            print('\nAté a próxima lista.')
            break

    nome_item = input('\nO que você deseja adicionar na lista?: ').capitalize().strip()

    if len(nome_item) <= 1: #Não permite escrever apenas um carácter
        print('Digite mais de um carácter.')
        animacao_espera()
        continue

    quantidade_item = input(f'\nQuantos {nome_item} você deseja adicionar (Apenas números)?: ')

    if not quantidade_item.isdigit(): #Permite escrever apenas números
        print('\nPor favor, digite apenas números na quantidade de itens.\n')
        animacao_espera()
        continue

    lista.append(f'{quantidade_item}x {nome_item}')