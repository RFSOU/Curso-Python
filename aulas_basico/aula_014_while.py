'''
Aula 14.
O laço for e o laço while pode ser usado em alguns semalhantes casos a diferença é que o laço for só pode ser usado quando temos o parametro incial eo final, já o laço while e deteminado somente 1 parametro de parada.
Exemplo:
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor.'))
    r = str(input('Quer continuar?[S/N]')).upper()
print('Fim')
'''
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('FIM!')

