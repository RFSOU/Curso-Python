'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
computador = randint(0,5)              # faz o computador pensar um numero de 0 a 5 e joga na variavel computador.
print('\033[0;31;0m-=-\033[m'*20)      # cria uma linha de 20 caracteres
print('\033[0;31;0m Vou Pensar em um numero entre 0 e 5. Tente Adivinhar...\033[m')
print('\033[0;31;0m-=-\033[m'*20)      # cria uma linha de 20 caracteres
jogador = int(input('\033[0;31;0m Em que numero eu pensei?\033[m'))
# Jogador tenta adivinhar
print('\033[0;30;41m PROCESSANDO...\033[m')
sleep(3)                               # do metodo time faz o computador
                                       # dormir conforme
if jogador == computador:
    print('\033[0;31;0m PARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[0;31;0m GANHEI! eu pensei no numero \033[0;31;0m{} \033[0;31;0m e não no \033[0;31;0m{}!'
          '\033[m'.format(computador, jogador))

    print()
