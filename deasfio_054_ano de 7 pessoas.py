'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.   '''
maior = 0
menor = 0
from datetime import date
for pessoas in range (0,7):
    ano = int(input('Qual o ano do nascimento.'))
    ano = (date.today().year-(ano))
    if ano < 18:
        menor += 1# menor recebe menor +1
    elif ano > 18:
        maior += 1# maior recebe maior +1
else:
    print('temos {}  maior de idade'.format(maior))
    print('temos {}  menor de idade'.format(menor))
    print('Total de {} pessoas'.format(pessoas+1))


