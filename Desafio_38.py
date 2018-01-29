'''Esceva um programa que leia 2 numeros inteiros  e compare-os mosntrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior os dois são iguais'''

valor1 = int(input('Escreva o primeiro numero'))
valor2 = int(input('Escreva o segundo numero'))
if valor1 > valor2:
    print('O primeiro valor é maior que o  segundo')
elif valor2>valor1:
    print('O segundo valor é maior que o primeiro')
else:
    print('Não existe valor maior os dois são iguais. ')


