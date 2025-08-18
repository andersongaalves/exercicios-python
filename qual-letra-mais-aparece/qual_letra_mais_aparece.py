frase = input('Digite uma frase: ').lower()

maior_contagem = 0
indice = 0
letra = ''
letras_mais_frequentes = letra

while indice < len(frase):
    letra = frase[indice]
    ocorrencias = frase.count(letra)

    if letra == ' ':
        indice += 1
        continue

    if ocorrencias > maior_contagem:
        maior_contagem = ocorrencias
        indice_principal = indice
    elif ocorrencias == maior_contagem and letra not in letras_mais_frequentes:
        letras_mais_frequentes += f',{letra}'
        indice_secundario = indice
    indice += 1

if len(letras_mais_frequentes) == 1:
    print(f'A letra que mais aparece é "{letras_mais_frequentes}" de índice {indice_principal}. Ela aparece {maior_contagem} vezes')
elif len(letras_mais_frequentes) == 2:
    print(f'As letras que mais aparecem são "{letras_mais_frequentes}" nos índices {indice_principal} e {indice_secundario}. Elas aparecem {maior_contagem} vezes')
