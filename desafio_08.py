'''Desafio 08 Escreva um programa  que leia um valor em metros eo
exiba convertido em centimetros'''

n1 = int (input ('Entre com  o valor em metros .'))


print ('O Valor dado em metros é {} centimetros'.format(n1*100), end=' ')
print ('ou {} milimetros'.format(n1*1000))