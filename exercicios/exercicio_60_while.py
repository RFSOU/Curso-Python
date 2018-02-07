'''
Faça um programa  que leia um numero qualquer e mostre seu fatorial'''
n = int(input('Digite um numero.'))
c = n
f = 1
print('Caculando {}! ='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
