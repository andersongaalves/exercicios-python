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

def adicionar_letra_correta (letra: str, palavra: str, palavra_final: str) -> str:
    """
    Verifica se 'letra' está contida na 'palavra' e revela os locais em que ela aparece.

    Args:
        letra(str): Letra enviada pelo usuário.
        palavra(str): Palavra sorteada pelo sistema.
        palavra_final(str): Palavra sorteada preenchida por '*'.

    Returns:
        str: Se 'letra' estiver na 'palavra', revela os locais em que ela aparece, se
        não, retorna 'palavra_final' sem alterações.

    Raises:
        TypeError: Se 'letra', 'palavra' ou 'palavra_final' não forem str.

    Example:
        >>> adicionar_letra_correta('a', 'amarelo', '*******')
        'a*a****'

        >>> adicionar_letra_correta('y', 'amarelo', '*******')
        '*******'
    """

    if not isinstance(letra, str):
        raise TypeError('letra deve ser str')
    
    if not isinstance(palavra, str):
        raise TypeError('palavra deve ser str')
    
    if not isinstance(palavra_final, str):
        raise TypeError('palavra_final deve ser str')
    
    if letra.isdigit():
        raise ValueError('letra não pode ser um número')
    
    if not letra:
        raise ValueError('letra não pode estar vazia')
    
    if not palavra:
        raise ValueError('palavra não pode estar vazia')
    
    if not palavra_final:
        raise ValueError('palavra_final não pode estar vazia')

    letra = letra.lower().strip()
    palavra = palavra.lower()
    palavra_final = list(palavra_final.lower())

    for i, letra_comparada in enumerate(palavra):
        if letra_comparada == letra:
            palavra_final[i] = letra

    return ''.join(palavra_final)

PALAVRAS_POSSIVEIS = ['amarelo', 'python', 'computador', 'linguagem']
RESPOSTA_AFIRMATIVA = ['sim', 'iniciar', 's', 'desejo']
RESPOSTA_NEGATIVA = ['n', 'nao', 'não']

while True:
    print('Bem vindo ao jogo da palavra secreta!')
    try:
        iniciar = tratar_input_texto(input('Deseja iniciar (sim/não)?: '))
    except ValueError:
        print('O campo não pode estar vazio')
        continue
    
    if iniciar in RESPOSTA_AFIRMATIVA:

        tentativas = 10
        palavra = random.choice(PALAVRAS_POSSIVEIS)
        palavra_final = '*' * len(palavra)

        print(f'Existe uma palavra secreta e é seu dever descobrir qual é.')

        while True:
            print(f'Você tem {tentativas} tentativas.')
            print(f'{palavra_final}')
            
            try:
                in_letra = tratar_input_texto(input('Digite uma letra: '))
            except ValueError:
                print('O campo não pode estar vazio')
                continue

            if len(in_letra) > 1:
                print('Digite apenas UMA letra')
                continue

            elif in_letra.isdigit():
                print('Digite APENAS letras')
                continue
  
            if verificar_se_letra_esta_na_palavra(in_letra, palavra):
                palavra_final = adicionar_letra_correta(in_letra, palavra, palavra_final)
            else:
                tentativas -= 1
                print('Letra errada.')

            if tentativas == 0:
                print(f'Que pena! você perdeu. A palavra final era "{palavra}"')
                break

            if palavra_final == palavra:
                print(f'Parabéns! A palavra final era "{palavra_final}"')
                break

    elif iniciar in RESPOSTA_NEGATIVA:
        break
    else:
        print('Você não digitou um comando')

print('Até a proxima')