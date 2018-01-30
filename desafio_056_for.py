'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final  do programa mostre:
A média de idade do grupo
Qual é o nome do homem mais velho do grupo
Quantas mulheres tem menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
menoridademulher = 0
nomevelho =''
for p in range(1,5):
 nome = str(input('Qual o nome {} pessoa?'.format(p)))
 idade = int(input('Qual a idade da {} pessoa?'.format(p)))
 sexo = str(input('qual o sexo da {} pessoa?'.format(p)))
 somaidade += idade
 if p == 1 and sexo in 'Mm':
     maioridadehome = idade
     nomevelho = nome
 if sexo in'Mn' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
 if sexo in 'Ff' and idade < 20:
    menoridademulher += 1

médiaidade = somaidade/4
print('A média da idade do grupo é:{}'.format(médiaidade))
print('O homem mais velho do grupo é: {} '.format(nomevelho))
print('{} mulheres são menores de 20 anos'.format(menoridademulher))






