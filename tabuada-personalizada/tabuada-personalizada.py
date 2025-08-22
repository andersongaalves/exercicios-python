# 1. Tabuada personalizada

# Peça um número e mostre sua tabuada (1 a 10).
# Use for para a tabuada.
# Use try/except para validar a entrada.

print('Bem vindo a tabuada personalizada.')
print('Iremos mostrar a tabuada de qualquer número que você digitar')

RESPOSTA_AFIRMATIVA = ['sim', 's', 'quero', '']
RESPOSTA_NEGATIVA = ['nao', 'n', 'não']

while True:
    entrada_n = input('Digite um número: ')
    try:
        numero = float(entrada_n)

        print(f'\nTabuada do {numero:.0f}:\n' + '-' * 20)

        for i in range(1, 11):
            resultado = numero * i
            print(f'{numero:.0f} x {i} = {resultado:.0f}')
            
        print('-' * 20)

        continuar_calculando = input('Deseja continuar calculando (Sim/Não)?: '
                                     ).lower().strip()

        if continuar_calculando in RESPOSTA_NEGATIVA:
            break
        
    except ValueError:
        print('Digite APENAS números')