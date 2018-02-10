'''
Crie um programa que leia a idade e o sexo de varias pessoas.
a cada pessoa cadastrada. o programa  devera perguntar se o
usuario quer ou não continuar no final mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 30 anos
'''

cont18 = 0
cont30 = 0
conth = 0
while True:
    sexo =' '
    opçao = ' '
    while sexo not in 'MF':
        idade = int(input('Qual a idade '))
        sexo  = str(input('Qual o sexo[M/F] ')) .strip() .upper()
        if idade > 18:
            cont18 += 1
        if idade < 30 and sexo == 'F':
            cont30 += 1
        if sexo == 'M':
            conth  += 1
        print(f'A idade é {idade} e o sexo é {sexo}.')
        while opçao not in 'SN':
            opçao = str(input(f'Você quer digitar mais algum usuario[S/N] ')).strip().upper()
            if opçao == 'S':
                break
            else:
                    print(f'A quantidade de pessoas maior de 18 é: {cont18}')
                    print(f'Mulheres com idade menor de 30 é {cont30}')
                    print(f'Quantidade de homens cadastrados é {conth}')
            exit()














