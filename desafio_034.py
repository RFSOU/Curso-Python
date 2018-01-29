'''Exercício Python 034: Escreva um programa que pergunte o
salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
salario =float(input('Qual o valor do seu salario?'))
if salario >= 1250.00:
    calculo = salario * 10/100
    print('O valor do salario com aumento é {:.2f}'.format(salario+calculo))
else:
    calculo = salario*15/100
    print('O valor do salario com aumento é {:.2f}'.format(salario+calculo))

