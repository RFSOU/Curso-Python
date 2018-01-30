n1 = int (input('um Valor'))
n2 = int (input('outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2 # ou pow(4,3)
print('A soma é {}, o produto é {}' .format(s, m, d), end=' ')
# o format pega as chaves {} vazias e coloca as variaveis dentro
# na sequencia apresentada.
# % == a sobra de uma divisão
# calcular a raiz quadrada de um numero é o mesmo que calcular a potência
# dele por **1/2 no caso  raiz cubica **(1/3)
# Dentro do print tambem temos no metodo 'print{}' .format  {:=^20} que
# coloca o nome no meio entre 20 sinais de igual de cada lado.
# Tambem pode se ser usado {:.3F} que da só o resultado de 3 casas após a virgula.
# Para continua a resta de  um print de outra linha na mesma linha se usa
# and='' no final do primeiro print e para quebrar \n onde desejar a quebra.


print ('Divisão inteira {} e potência {}' .format (di,e))
# o end ='' junta os dois print. /n quebra linha.




#	ORDEM DE PRECEDENCIA NO PYTHON:
# 1 (...) PARENTESES
# 3  * --/-- //-- %
# 4  + -
# 5 pow COMANDO PARA POTENCIA pow(3,4) = 64
# __________________________________________
# // DIVISÃO INTEIRA
# / DIVISÃO NORMAL
# % SOBRA DA DIVISÃO
# Criar a raiz quadrada de um numero é o mesmo que criar a potência do mesmo por 1/2 entre parenteses no Python.

