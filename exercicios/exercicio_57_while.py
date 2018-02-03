'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = 'a'


while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual éo sexo?[M/F]')).upper()
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print('Seu sexo é:{}'.format(sexo))

