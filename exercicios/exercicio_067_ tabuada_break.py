'''Faça um programa que mostre a tabuada de varios numeros,
um de cada vez, para cada valor digitado pelo usuario.
O programa será interrompido quando o numero solicitado
for negativo.'''
cont =0
while True:
    cont = cont+1
    t = int(input('Qual o numero da tabuada você quer?'))
    if t < 0:
        break
    for c in range(1,11):
        print(' {} x {} = {}'.format(t, c, (t * c)))
print('FIM')

