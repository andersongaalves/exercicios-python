def separar_primeiros_digitos_cpf(inp):
    """
    Separa os nove primeiros dígitos de um CPF, ignorando pontos e traços.

    Args:
        inp (str): CPF digitado pelo usuário, podendo conter '.' e '-'.

    Returns:
        list[int]: Lista com os 9 primeiros dígitos do CPF.

    Raises:
        TypeError: Se a entrada não for uma string.
        ValueError: Se a string estiver vazia.
    
    Example:
        >>> separar_primeiros_digitos_cpf('746.824.890-70')
        [7, 4, 6, 8, 2, 4, 8, 9, 0]
    """

    if not isinstance(inp, str):
        raise TypeError(f'{inp} deve ser uma str')

    primeiros_digi = []

    for numeros_cpf in inp:
        if len(primeiros_digi) == 9:
            break
        if not numeros_cpf.isdigit():
            continue
        primeiros_digi.append(int(numeros_cpf))
    
    return primeiros_digi

def multiplicar_elementos_por_x_regressivo(iterable):
    """
    Multiplica todos os elementos de uma lista ou tupla pela quantidade
    de elementos + 1 regressivamente. 
    Ex: 

    lista = ['7', '8']
    X = 2 + 1

    calculo = 7 * 3 == 21
    calculo2 = 8 * 2 == 16

    resultado = ('21', '16')

    Args:
        iterable (list | tuple): Coleção de elementos que serão calculados

    Returns:
        tuple: Coleção com resultados
    """

    if not isinstance(iterable, (list, tuple)):
        raise TypeError(f'"{iterable}" deve ser do tipo list ou tuple')
    if not iterable:
        raise ValueError(f'"{iterable}" não pode estar vazia')
    
    x = len(iterable) + 1
    prmrs_d_mltpl = []

    for n_atual in iterable:
        prmrs_d_mltpl.append(x * int(n_atual))
        x -= 1
    return tuple(prmrs_d_mltpl)

def somar_elementos(lista):

    """
    Soma os elementos de um objeto list ou tuple

    Args:
        lista (list | tuple): Coleção de números que serão somados.

    Returns:
        (int | float): Retorna a soma de todos elementos da lista
    """

    if not isinstance(lista, (list, tuple)):
        raise TypeError(f'"{lista}" deve ser do tipo list ou tuple')
    if not lista:
        raise ValueError(f'"{lista}" não pode estar vazia')

    soma_d_mltpl = 0
    for i, d_mltpl in enumerate(lista, start=1):
        soma_d_mltpl += d_mltpl
        if i == len(lista):
            return soma_d_mltpl

def multiplicar_por_dez_e_retornar_resto_por_onze(n):

    """
    Multiplica um número por dez e retorna o resto da sua divisão por onze.

    Args:
        n (int): Número que será calculado
    
    Returns:
        int: Resto da divisão de (n * 10) por 11

    """

    if not isinstance(n, int):
        raise TypeError(f'"{n}" deve ser int')
    return (n * 10) % 11

def digito_cpf(n):
    """
    Verifica se n é maior ou menor que 9 e retorna um resultado de acordo

    Args:
        n (int): Número a ser verificado
    
    Returns:
        int: Retorna n ou 0 de acordo com o resultado da comparação
    """

    if not isinstance(n, int):
        raise TypeError(f'"{n}" deve ser do tipo int')
    return n if not n > 9 else 0

def tratar_cpf(cpf):
    """
    Verifica se o CPF é válido e remove pontos e traços

    Args:
        cpf (str): Entrada do CPF digitado.
    
    Returns:
        str: Retorna uma string apenas com os dígitos do CPF
    """
    if not isinstance(cpf, str):
        raise TypeError(f'{cpf} deve ser uma str')
    if not cpf:
        raise ValueError(f'{cpf} não pode estar vazio')

    cpf_numeros = ''

    for digitos in cpf:
        cpf_numeros += digitos if digitos.isdigit() else ''
    if len(cpf_numeros) != 11:
        raise ValueError(f'{cpf} CPF inválido')
    return cpf_numeros

def validar_cpf(cpf, n, n2):
    """
    Verifica se os dois últimos dígitos do CPF batem com os
    resultados dos cálculos.

    Args:
        cpf (str): CPF digitado pelo usuário.
        n (int): Resultado do cálculo do primeiro dígito.
        n2 (int): Resultado do cálculo do segundo dígito.

    Returns:
        bool: True se os dois últimos dígitos conferirem, False caso contrário.
    """

    if not isinstance(cpf, str):
        raise TypeError(f'{cpf} deve ser list ou tuple')
    if not isinstance(n, int) or not isinstance(n2, int):
        raise TypeError(f'{n} e {n2} devem ser int')
    if not cpf or n is None or n2 is None:
        raise ValueError(f'{cpf}, {n} ou {n2} está vazio')
    
    return (int(cpf[-2]), int(cpf[-1])) == (n, n2)

def formatar_cpf(cpf):
    """
    Percorre um iterável verificando se é um cpf e formatando de acordo.

    Args:
        cpf (str | list | tuple): Coleção onde os dígitos do CPF se encontram.
    
    Returns:
        str: Retorna o CPF formatado com traços e pontos.

    """
    if not isinstance(cpf, (str, list, tuple)):
        raise TypeError(f'"{cpf}" deve ser iterável.')
    if not cpf:
        raise ValueError(f'"{cpf}" não pode estar vazio')
    if len(cpf) > 11:
        raise ValueError(f'{cpf} não é um cpf')
    
    out = ''

    for i, n in enumerate(cpf, start=1):
        n = str(n)
        if i in (4, 7):
            out += '.'
        elif i == 10:
            out += '-'
        out += n

    return out

while True:

    try:

        entrd_cpf = tratar_cpf(input('Digite seu CPF: '))

        digitos = separar_primeiros_digitos_cpf(entrd_cpf)
        digitos_multi = multiplicar_elementos_por_x_regressivo(digitos)
        soma = somar_elementos(digitos_multi)
        resultado = multiplicar_por_dez_e_retornar_resto_por_onze(soma)
        primeiro_d = digito_cpf(resultado)

        digitos.append(primeiro_d)

        cpf_cru = digitos

        digitos_multi_2 = multiplicar_elementos_por_x_regressivo(cpf_cru)
        soma_2 = somar_elementos(digitos_multi_2)
        resultado_2 = multiplicar_por_dez_e_retornar_resto_por_onze(soma_2)
        segundo_d = digito_cpf(resultado_2)

        digitos.append(segundo_d)

        if not validar_cpf(entrd_cpf, primeiro_d, segundo_d):
            print('CPF inválido')
            continue

        cpf_formatado = formatar_cpf(digitos)

        print(cpf_formatado)

    except ValueError:
        print(f'')
    except TypeError:
        print(f'{TypeError}')