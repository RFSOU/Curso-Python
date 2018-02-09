'''Faça um programa que jogue par ou impar com o computador. O jogo sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor'))
    computador = randint(0,10)
    total = jogador+computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar:[P/I]?')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador} e o Total é {total}')
    if tipo == 'P':
        if total % 2 == 0:
            v += 1
            print('Você venceu!')

        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            v += 1
            print('Você venceu!')

        else:
            print('Você perdeu!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER!  Você venceu {v} vezes.')
