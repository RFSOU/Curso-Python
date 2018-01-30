'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
 no nome'''

nome = str(input('Qual éo seu nome?')).strip()
print('Seu nome tem silva?{}'.format('silva'in nome.lower()))
# o operador "in" diz se o silva esta dentro da variavel nome eo nome.lower
# coloca tudo
# que for digitado pelo usuario em minusculo para não ter erro de digitação ao
# ser pesquisado.
