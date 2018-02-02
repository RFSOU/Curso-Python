'''escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
-1 para binario
-2 para octal
-3 para hexadecimal
'''

numero = int(input('Escreva um numero inteiro'))
base = str(input('Para qual base você que converter:-Binario-Octal ou Hexadecimal?')).strip()
if base[:35].upper() == 'BINARIO':
    print('Ok vamos converter para',base,)
    print(bin(numero))
elif base[:35].upper() == 'HEXADECIMAL':
    print('Ok vamos converter para',base)
    print(hex (numero))
elif base[:35].upper() == 'OCTAL':
    print('Ok vamos converter para',base)
    print(oct (numero))
else:
    print('Você só pode escolher 3 opções Binario Hexadecimal e Octal')