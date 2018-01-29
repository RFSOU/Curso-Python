import  math

ângulo = float (input('digite o angulo que você deseja:'))# digitar ângulo para variavel ângulo
seno = math.sin(math.radians(ângulo)) # carrega o metodo sin para o calculo do SENO
print ('O ângulo de {} tem o seno de {:.2f}'.format(ângulo,seno))
cosseno= math.cos(math.radians(ângulo))# carrega o metodo cos para o calculo do COSSENO
print ('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo)) #carrega o metodo tan para o calculo da TANGENTE
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo,tangente))


