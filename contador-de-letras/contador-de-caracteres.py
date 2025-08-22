# 2. Contador de letras

# Peça uma palavra e mostre quantas vezes cada letra aparece.
# Use for para percorrer a string.
# Use if para contar apenas letras (ignorar espaços).

RESPOSTA_NEGATIVA = ['nao', 'n', 'não']
TITULO = 'Contador de caracteres'

print (TITULO.center(120, '='))

while True:

    palavra = input('\nDigite uma palavra ou frase: ').lower().strip()
    letras_processadas = []

    print (f'\nAnalisando palavra: {palavra.upper()}\n')
    print('-' * 40)

    if len(palavra) <= 1:
        print('Por favor, digite mais de uma letra')
        continue

    for letra in sorted(palavra):
        if letra == ' ' or letra in letras_processadas: #Ignora os espaços e letras que já
            continue                                      #foram contadas

        ocorrencias = palavra.count(letra)

        print(f'{letra} aparece {ocorrencias} vezes.'.capitalize())

        letras_processadas.append(letra)
    
    continuar = input('\nDeseja continuar contando(Sim/Não)?: ').lower().strip()

    if continuar in RESPOSTA_NEGATIVA:
        break