'''Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente'''
n = str (input('\033[07;30;44mEscreva o seu nome completo. \033[m')) .strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
# a funão len conta os nomes e pode ser determinado apartir da onde começa
#  no caso -1 para iniciar no zero o primeiro nome ja que a contagem
# dos caracteres começa em o então -1= 0 e 0 =1.


