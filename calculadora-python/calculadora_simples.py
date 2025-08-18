# Calculadora

print('Bem vindo à calculadora!')

while True:
    entrada_numero_1 = input('Digite um número: ')
    entrada_operador = input('Digite um operador (+, -, *, /): ')
    entrada_numero_2 = input('Digite outro número: ')

    try:
        entrada_numero_1 = float(entrada_numero_1)
        entrada_numero_2 = float(entrada_numero_2)

        if entrada_operador == '+':
            resultado = entrada_numero_1 + entrada_numero_2
        elif entrada_operador == '-':
            resultado = entrada_numero_1 - entrada_numero_2
        elif entrada_operador == '*':
            resultado = entrada_numero_1 * entrada_numero_2
        elif entrada_operador == '/':
            resultado = entrada_numero_1 / entrada_numero_2
        else:
            print('Operador inválido!')
            continue

        print(f'Resultado: {resultado:.2f}')

    except ValueError:
        print('Erro: você não digitou um número válido!')
    except ZeroDivisionError:
        print('Erro: divisão por zero não é permitida!')

    sair_continuar = input('Você quer continuar calculando (sim/não)? ').lower().strip()

    if sair_continuar in ['não', 'nao', 'n']:
        print('Você escolheu sair')
        break
    elif sair_continuar in ['sim', '']:
        print('Você escolheu continuar')
