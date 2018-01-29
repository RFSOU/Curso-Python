'''Crie um programa que faça o computador jogar jokenpô com você'''
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tezoura')
computador = randint(0,2)

print('''Vamos jogar JOKENPO escolha Sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-'*11)
print('O você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('=-'*11)
if computador==0:#computador jogou pedra
    if jogador==0:
        print('Empate')
    elif jogador==1:
        print('Jogador venceu!')
    elif jogador==2:
        print('Computadpr venceu!')
    else:
        print('Jogada Invalida!')
elif computador==1:#computador jogou papel
    if jogador==0:
        print('Computador venceu!')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('Jogador venceu!')
    else:
        print('Jogada Invalida!')
elif computador==2:#computador jogou tesousa
    if jogador==0:
        print('Jogador Venceu!')
    elif jogador==1:
        print('Computador Venceu!')
    elif jogador==2:
        print('Empate!')
    else:
        print('Jogada Invalida!')

