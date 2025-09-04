def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula o imc com base no peso e altura.

    Args:
        peso (float | int): Peso em kg.
        altura (float | int): Altura em cm ou metros.
    
    Returns:
        float: Retorna o IMC.

    Raises:
        TypeError: Se peso ou altura não forem float/int.
        ValueError: Se peso ou altura forem menores ou iguais a zero.
    
    Example:
        >>> calcular_imc(80, 175)
        26.12

        >>> calcular_imc(83.50, 1.82)
        25.21

    """
    if not isinstance(peso, (float, int)):
        raise TypeError('O peso deve ser um número')
    if not isinstance(altura, (float, int)):
        raise TypeError('A altura deve ser um número')
    if peso <= 0:
        raise ValueError('Peso deve ser maior que zero')
    if altura <= 0:
        raise ValueError('Altura deve ser maior que zero')
    
    altura = altura / 100 if altura > 10 else altura
    
    return round(peso / (altura * altura), 2)

dados_pessoas = []

while True:

    qtd_pessoas = input('O IMC de quantas pessoas você quer calcular?: ')

    if not qtd_pessoas.isdigit():
        print('\nPor favor, digite apenas números inteiros\n')
        continue

    int_qtd_pessoas = int(qtd_pessoas)

    for n_pessoa in range(1, int_qtd_pessoas + 1):

        peso = input(f'\nInsira o peso da pessoa {n_pessoa} (Ex. 70): ')
        altura = input(f'Insira a altura da pessoa {n_pessoa}(Ex. 1.70): ')

        try:
            peso = float(peso)
            altura = float(altura)

            if altura <= 0:
                print('\nAltura deve ser maior que zero\n')
                continue
            if peso <= 0 :
                print('\nPeso deve ser maior que zero\n')
                continue

        except ValueError:
            print('\nPor favor, digite apenas números válidos\n')
            break

        dados_pessoas.append([peso, altura])

    print()
    for i, dados in enumerate(dados_pessoas):
        imc = calcular_imc(dados[0], dados[1])
        print(f'IMC pessoa {i + 1}: {imc:.2f}')

    dados_pessoas.clear()

    continuar = input('\nDeseja continuar calculando(Sim/Não)?: ').lower().strip()

    if continuar in ('n', 'nao', 'não'):
        print('Até a próxima')
        break
    else:
        continue