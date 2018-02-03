''' Melhore o jogo do Desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep

jogador = 1
computador = 0
palpite = 0
while computador != jogador:
    computador = randint(0, 10)  # faz o computador pensar um numero de 0 a 10 e joga na variavel computador.
    print('\033[0;31;0m-=-\033[m' * 20)  # cria uma linha de 20 caracteres
    print('\033[0;31;0m Eu Pensei em um numero entre 0 e 10. Tente Adivinhar...\033[m')
    print('\033[0;31;0m-=-\033[m' * 20)  # cria uma linha de 20 caracteres
    jogador = int(input('\033[0;31;0m Em que numero eu pensei?\033[m'))  # Jogador tenta adivinhar
    print('\033[0;30;41m PROCESSANDO...\033[m')
    sleep(3)  # do metodo time faz o computador dormir conforme atributo.
    palpite = palpite + 1 # conta um ciclo de pensamento do computador e acumula.
    if jogador != computador:
        print(
            '\033[0;31;0m GANHEI! eu pensei no numero \033[0;31;0m{} \033[0;31;0m e não no \033[0;31;0m{}!''\033[m'.format(
                computador, jogador))# computador ganhou.
else:
 print('\033[0;31;0m PARABÉNS! Você conseguiu me vencer em {} palpites!\033[m'.format(palpite))# jogador ganhou.
 print('FIM')# FIM .




