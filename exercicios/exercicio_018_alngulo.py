from math import radians, sin, cos,tan # escrever cada metodo nesta linha faz com que não precise ser mecionado o math (modulo) no codigo
ângulo = float (input('digite o angulo que você deseja:'))# digitar ângulo para variavel ângulo
seno = sin(radians(ângulo)) # carrega o metodo sin para o calculo do SENO
print ('O ângulo de {} tem o seno de {:.2f}'.format(ângulo,seno))
cosseno= cos(radians(ângulo))# carrega o metodo cos para o calculo do COSSENO
print ('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = tan(radians(ângulo)) #carrega o metodo tan para o calculo da TANGENTE
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo,tangente))


