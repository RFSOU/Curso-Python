'''refaça o desafio 35 dos triamgulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Isoceles: dois lados iguais
- Escaleno: Todos os lados diferentes
'''
a = float(input('Escreva o comprimento da reta 1 ='))
b = float(input('Escreva o comprimento da reta 2 ='))
c = float(input('Escreva o comprimento da reta 3 ='))

if b-c<a and a<b+c:
    if a-c<b and b<a+c:
        if a-b<c and c<a+b:
            print('O comprimento destas retas podem formar um triangulo ')
        else:
            print('O comprimento destas retas não podem ser um triangulo')
if b==c==a:
    print('Este triangulo é equilatero.')
elif b!=a and c!=a and c!=b:
    print('Este triangulo é escaleno.')
else:
    print('Este triangulo é isoceles')

