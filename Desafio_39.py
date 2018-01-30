''' faça um programa que leia o ano de nascimento de um jovem  e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
_Se éa hora de se alistar
-Se ja passou o tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''


from datetime import date #modulo de data e tempo

'''anonasc = int(input('Qual o seu ano de nascimento?'))
anoatual = date.today().year #função que coloca o ano atual na variavel de forma para fazer calculo de diferença c/ date
idade = anoatual - anonasc


if idade >= 19:
    print('Sua idade é:', idade,'anos')
    print('Já passou o tempo do seu alistamento!')
    print('ja se passaram',idade - 18, 'anos')

elif idade <= 17:
    print('Sua idade é:', idade,'anos')
    print('Você ainda vai se alistar.')
    print('faltam',18-idade,'anos')


elif idade == 18:
    print('Sua idade é:', idade,'anos')
    print('É hora de se alistar!')
else:'''
dia = int(input('Digite o dia do seu nacimento.'))
mes = int(input('Digite o mês do seu nacimento.'))
ano = int(input('Digite o ano do seu nacimento.'))


print('Faltam para',date.today().year-(ano),'anos')
print(date.today().month-(-mes+2),'mesês')
print(date.today().day-(dia),'dias')

ano=((date.today().year-ano)*365)
mes=((date.today().month-mes)*30)
dia=(date.today().day-dia)
ano= ano+mes+dia

print('Você tem',(ano//366),'anos')
if mes<0:
    print(((mes)+360)//30,'mesês')
else:
    print((mes)//30,'mesês')
print((dia),'dias')



