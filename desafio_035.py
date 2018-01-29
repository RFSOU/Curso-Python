'''Exercício Python 035: Desenvolva um programa que leia o comprimento de
 três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

a = float(input('Escreva o comprimento da reta 1 ='))
b = float(input('Escreva o comprimento da reta 2 ='))
c = float(input('Escreva o comprimento da reta 3 ='))

if b-c<a and a<b+c:

    if a-c<b and b<a+c:

        if a-b<c and c<a+b:
            print('O comprimento destas retas podem formar um triangulo ')
        else:
            print('O comprimento destas retas não podem ser um triangulo')

