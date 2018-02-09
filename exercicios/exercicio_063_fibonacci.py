'''
Faça um programas que leia o numero de termos que você quer e mostre em sequencia fibonacci.
'''
n = float(input('Qual o numero de termos fibonacci você deseja ver '))
t1 = 0
t2 = 1
if n == 1:
    print(t1)
else:
    print('{},{},'.format(t1,t2),end='')
cont = 3
while cont <= n:
    cont = cont + 1

    print('{},'.format(t1+t2),end='')
    t3=t1+t2
    t1=t2
    t2=t3


