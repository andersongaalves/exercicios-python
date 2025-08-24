import random

def verificar_se_letra_esta_na_palavra(letra: str, palavra: str) -> bool:
    """
    Verifica se a letra enviada pelo usuário está contida na palavra.

    Args:
        letra (str): Letra enviada pelo usuário.
        palavra (str): Palavra sorteada pelo sistema.

    Returns:
        bool: True se letra estiver na palavra, False caso contrário.

    Raises:
        TypeError: Se 'letra' ou 'palavra' não forem str.
        ValueError: Se 'letra' ou 'palavra' estiverem vazios.
        ValueError: Se 'letra' tiver mais de um caractere.

    Example:
        >>> verificar_se_letra_esta_na_palavra('a', 'amarelo')
        True

        >>> verificar_se_letra_esta_na_palavra('i', 'amarelo')
        False
    """

    if not isinstance(letra, str):
        raise TypeError('letra deve ser str')
    if not isinstance(palavra, str):
        raise TypeError('palavra deve ser str')
    
    if not letra:
        raise ValueError('letra não pode estar vazia')
    if not palavra:
        raise ValueError('palavra não pode estar vazia')
    if len(letra) > 1:
        raise ValueError("letra deve ter apenas um caractere")
    
    return letra.lower() in palavra.lower()

def tratar_input_texto(entrada: str) -> str:
    """
    Transforma todo o texto de entrada em minúsculo e retira espaços
    desnecessários.

    Args:
        entrada(str): Texto digitado pelo usuário.
    
    Returns:
        str: Texto em minúsculo e sem espaços desnecessários.
    
    Raises:
        TypeError: Se 'entrada' não for str.
        ValueError: Se 'entrada' estiver vazia.

    Example:
        >>> tratar_input_texto(' Sim ')
        'sim'
    """
    if not isinstance(entrada, str):
        raise TypeError('entrada deve ser str')
    if not entrada:
        raise ValueError('entrada não pode estar vazia')
    
    return entrada.lower().strip()

PALAVRAS_POSSIVEIS = ['amarelo', 'python', 'computador', 'linguagem']
RESPOSTA_AFIRMATIVA = ['sim', 'iniciar', 's', 'desejo']
RESPOSTA_NEGATIVA = ['n', 'nao', 'não']

while True:
    print('Bem vindo ao jogo da palavra secreta!')
    iniciar = tratar_input_texto(input('Deseja iniciar (sim/não)?: '))
    
    if iniciar in RESPOSTA_AFIRMATIVA:

        tentativas = 10
        palavra = random.choice(PALAVRAS_POSSIVEIS)
        palavra_final = '*' * len(palavra)

        print(f'Existe uma palavra secreta e é seu dever descobrir qual é.')

        while True:
            print(f'Você tem {tentativas} tentativas.')
            print(f'{palavra_final}')
            
            letra_correta = False

            in_letra = tratar_input_texto(input('Digite uma letra: '))

            if len(in_letra) > 1:
                print('Digite apenas UMA letra')
                continue
            elif in_letra.isdigit():
                print('Digite APENAS letras')
                continue
            
            

            print(verificar_se_letra_esta_na_palavra(in_letra, palavra))






            for i, letra_comparada in enumerate(palavra):
                if letra_comparada == in_letra:
                    palavra_final = palavra_final[:i] + in_letra + palavra_final[i+1:]
                    letra_correta = True

            if not letra_correta:
                tentativas -= 1
                print('Letra errada.')


            if tentativas == 0:
                print(f'Que pena! você perdeu. A palavra final era "{palavra_final}"')
                break

            if palavra_final == palavra:
                print(f'Parabéns! A palavra final era "{palavra_final}"')
                break

    elif iniciar in RESPOSTA_NEGATIVA:
        break
    else:
        print('Você não digitou um comando')

print('Até a proxima')