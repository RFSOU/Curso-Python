'''Desenvolva uma programa que  leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
a1=0
a1 = int(input('Qual o primeiro termo da PA'))
r = int(input('Qual é a razão da PA'))
print(' PA DE RAZÃO {} = {}'.format(r,a1))
for c in range(0,9):
    if c <=11:
        a1=a1+r
        print((' PA DE RAZÃO {} = {}').format(r,a1))
print('fim')
















