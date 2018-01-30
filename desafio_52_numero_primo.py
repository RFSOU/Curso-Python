'''Faça um programa que leia um numero inteiro e diga se ele é ou não um numero
primo '''
np = int(input('digite um numero inteiro'))

if np == 0:
    print('não é primo')
elif np == 1:
    print('não é primo')
elif np%2==0 and np!=2:
    print('não é primo')
elif np/1!=np and np/np!=1:
    print('não é primo')
elif np%5==0 and np!=5:
    print('não é primo')
else:
    print('é primo')























