'''
Refazer o desafio 051 lendo primeiro termo e a razão de uma PA,mostrando os 10 primeiros termos da progressão usando a estrutura while
'''
a1=0
n=1
a1 = int(input('Qual o primeiro termo da PA'))
r = int(input('Qual é a razão da PA'))
print(' PA DE RAZÃO {} = {}'.format(r,a1))
while n < 10:
        a1=a1+r
        n = n+1
        print((' PA DE RAZÃO {} = {}').format(r,a1))
print('fim')