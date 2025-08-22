# 3. Conversor de temperatura

# Usuário escolhe C → F ou F → C.
# Faça o menu em while.
# Use try/except para validar os números.

import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_pontos(tempo):
    time.sleep(tempo / 3)
    print('.')
    time.sleep(tempo / 3)
    print('.')
    time.sleep(tempo / 3)
    print('.')    

def converta_temperatura(unidade, temperatura):
    temperatura = float(temperatura)

    if unidade in CELSIUS:
        return temperatura * 1.8 + 32
    elif unidade in FAHRENHEIT:
        return (temperatura - 32) / 1.8

TITULO = 'Conversor de Temperatura Celsius e Fahrenheit'
CELSIUS = ['celsius', 'c']
FAHRENHEIT = ['fahrenheit', 'f']
NEGATIVA = ['não', 'n', 'nao']

historico = []

while True:
    limpar_terminal()

    print(TITULO.center(120, '=') + '\n')

    if historico:
        print(f'Historico: {historico}\n' + f"{'-' * 100}")


    unidade = input('Qual unidade você deseja converter \n' \
    'Celsius (C) ou Fahrenheit (F)?: ').lower()
    

    if unidade not in CELSIUS + FAHRENHEIT:
        print('Informe uma unidade válida.')
        animacao_pontos(1.5)
        continue

    temperatura = input('Informe a temperatura: ')

    try:
        temperatura_float = float(temperatura)
        temperatura_final = converta_temperatura(unidade, temperatura_float)

        if unidade in CELSIUS:
            print(f'{temperatura} celsius é {temperatura_final:.2f} em fahrenheit.')
        elif unidade in FAHRENHEIT:
            print(f'{temperatura} fahrenheit é {temperatura_final:.2f} em celsius.')
        
        historico.append(f'{temperatura}°{unidade[0].upper()} -> {temperatura_final:2g}')

    except ValueError:
        print('Digite um valor válido.')
        animacao_pontos(1.5)
        continue

    continuar = input('Quer continuar convertendo?: ').lower().strip()

    if continuar in NEGATIVA:
        print('Até a próxima!')
        animacao_pontos(1.5)
        exit()