'''Nessa aula 06, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras
operações com a função print() do Python.
int = 7 -4 0 9875 numeros inteiros
float = 4.5 0.0075 -15.223 7.0 numeros reais
bool = true e false
str. "Olá" '7.5' são considerados escritas para impressão.
metodo format é constituido por {} dentro do print que espera do .format(s)
o ewsultado da variavel s no caso.
'''

n1 = int (input ('digite um valor:'))
n2 = int (input ('digite uoutro:'))
s= n1+n2
#print ('A soma entre ',n1, 'e', n2, 'vale', s)
print ('a soma entre {} e {} vale {}' .format(n1,n2,s))
