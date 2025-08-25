import os
import time

def tratar_entrada(entrd):
    if not isinstance(entrd, str):
        raise ValueError('Entrada deve ser uma string')
    
    return entrd.lower().strip()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_pontos(duracao):
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(duracao / 3)
    
def inserir(name: str, qtd: int | float, lista: list = None) -> str | list:
    """
    Retorna ou insere um item e sua quantidade a uma lista.

    Args:
        name (str): Nome do item.
        qtd (int | float): Quantidade do item.
        lista (list, opcional): Lista onde será inserido.
    
    Returns:
        str | list: 
            - Se lista for None -> retorna apenas a string "Item Qtdx".
            - Se lista for list -> insere na lista e retorna a própria lista.
    
    Raises:
        TypeError: Se 'name' não for str, 'qtd' não for int/float e se 'lista' não for list/None.
        ValueError: Se 'name' estiver vazio ou se 'qtd' for menor ou igual a zero.

    Example:
        >>> inserir('Pão', 2)
        'Pão 2x'

        >>> inserir('pão', 2, ['Manteiga 1x'])
        ['Manteiga 1x', 'Pão 2x']

    """
    #TypeError
    if not isinstance(name, str):
        raise TypeError(f'{name} precisa ser uma str, você passou {type(name).__name__}')
    if not isinstance(qtd, (int, float)):
        raise TypeError(f'{qtd} precisa ser um int ou float, você passou {type(qtd).__name__}')
    if lista is not None and not isinstance(lista, list):
        raise TypeError(f'{lista} precisa ser uma list, você passou {type(lista).__name__}')
    
    #ValueError
    if not name.strip():
        raise ValueError(f'{name} não pode estar vazio')
    if qtd <= 0:
        raise ValueError(f'{qtd} deve ser maior que zero')

    item = f'{name.title()} {qtd}x'

    if lista is None:
        return item
    
    lista.append(item)
    return lista

def exibir_lista_formatada(lista, titulo=None):
    if lista is not None and not isinstance(lista, list):
        raise TypeError(f'{lista} deve ser do tipo list')
    
    elif lista == []:
        lista_vazia = 'Sua lista está vazia'
        return lista_vazia
    
    if not titulo:
        resultado = 'Sem título' + '\n\n'
        for index, item in enumerate(lista, start=1):
            resultado += (f'{index} - {item}\n')
        return resultado
    else:
        resultado = titulo + '\n\n'
        for index, item in enumerate(lista, start=1):
            resultado += (f'{index} - {item}\n')
        return resultado

MENU = ('i', 'd', 'inserir', 'deletar')

lista_de_compras = []

while True:
    limpar_terminal()

    if lista_de_compras:
        print(exibir_lista_formatada(lista_de_compras, 'Lista de compras'))

    menu_selecionado = tratar_entrada(input('Selecione uma opção\n[I]nserir [D]eletar: '))

    if menu_selecionado not in MENU:
        print('Digite uma opção válida')
        animacao_pontos(2)
        continue

    while menu_selecionado.startswith('i'):

        limpar_terminal()

        if not lista_de_compras:
            nome_item = tratar_entrada(input('Digite o item que você deseja adicionar: ') )
        else:
            print(exibir_lista_formatada(lista_de_compras, 'Lista de compras'))
            nome_item = tratar_entrada(input('Continue adicionando ou digite "Voltar" caso queira retornar ao menu: ') )
        
        if nome_item.isdigit():
            print('Por favor, digite apenas letras')
            animacao_pontos(2)
            continue
        elif len(nome_item) <= 1:
            print('Por favor, digite mais de uma letra')
            animacao_pontos(2)
            continue
        elif nome_item == 'voltar':
            break

        while True:
            limpar_terminal()

            qtd_item = (input(f'Quantas unidades de {nome_item} você quer adicionar?: '))

            if not qtd_item.isdigit():
                print('Por favor, digite apenas números')
                animacao_pontos(2)
                continue

            qtd_item = int(qtd_item)
            inserir(nome_item, qtd_item, lista_de_compras)
            break
        

    while menu_selecionado.startswith('d'):

        limpar_terminal()
        
        if not lista_de_compras:
            print('Não há o que deletar da lista')
            animacao_pontos(2)
            break

        print(exibir_lista_formatada(lista_de_compras, 'Lista de compras'))

        deletar_item = input('Qual o número do item que você deseja deletar?: ')

        if not deletar_item.isdigit():
            print('Por favor, digite apenas números da lista')
            animacao_pontos(2)
            continue

        deletar_item = int(deletar_item)

        if deletar_item > len(lista_de_compras):
            print('Por favor, digite apenas números da lista')
            animacao_pontos(2)
            continue
        
        i = deletar_item - 1

        print(f'Você deletou', lista_de_compras.pop(i))
        animacao_pontos(2)
        break