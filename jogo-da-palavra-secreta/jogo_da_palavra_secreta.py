import random

PALAVRAS_POSSIVEIS = ['amarelo', 'python', 'computador', 'linguagem']
RESPOSTA_AFIRMATIVA = ['sim', 'iniciar', 's', 'desejo']
RESPOSTA_NEGATIVA = ['n', 'nao', 'não']

while True:
    print('Bem vindo ao jogo da palavra secreta!')
    iniciar = input('Deseja iniciar (sim/não)?: ').lower()
    
    if iniciar in RESPOSTA_AFIRMATIVA:

        tentativas = 10
        palavra = random.choice(PALAVRAS_POSSIVEIS)
        palavra_final = '*' * len(palavra)

        print(f'Existe uma palavra secreta e é seu dever descobrir qual é.')

        while True:
            print(f'Você tem {tentativas} tentativas.')
            print(f'{palavra_final}')
            
            letra_correta = False

            in_letra = input('Digite uma letra: ').lower()

            if len(in_letra) > 1:
                print('Digite apenas UMA letra')
                continue
            elif in_letra.isdigit():
                print('Digite APENAS letras')
                continue

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