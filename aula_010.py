#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus
#programas em Python.
#Veja como aplicar os comandos if: e else: no Python.

n1 = float (input('\033[7;35;40m Digite a primeira nota: \033[m'))
n2 = float (input('\033[7;30;31m Digite a segunda nota: \033[m'))
m = (n1 + n2)/2
print('***'*20)
print('\033[7;35;40m A sua média foi {:.1f}\033[m'.format(m))
if m >= 6.0:
    print('\033[0;30;31m sua média foi boa! PARABENS!\033[m ')
else:
    print('***'*20)
    print('\033[7;30;41m Sua media foi ruim! ESTUDE MAIS!\033[m ')

# \033[0;30;31m  "cria um padrão com estilo cor de texto e cor de fundo".
    # \033[m  "encerra na linha um padrão de cores a ser impressa".