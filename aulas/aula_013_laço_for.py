'''Nesta aula o for inicia um laça de repeticão depois do range (1,10,2)temos entre esses parentes de 1 a 10 uma repiticão de 9 vezes e o 2 significa pulando de 2 em 2 se fosse -1 significaria que a repetição seria decrescente'''
# dessa forma o range conta crescente
'''for c in range(0,10):
    print(c)
print('fim')'''

# dessa forma o range conta decrescente
'''for c in range(10,0,-1):
    print(c)
print('fim')'''
# dessa forma o comando for soma N+1 na entrada que faz o range inteiro porque se você digita 10 no range ele roda até 9 um a menos.
''''n = int (input('Digite um numero:'))
for c in range(0,n+1):
    print(c)
print('fim')'''
# dessa forma o input esta capturando variavel e jogando dentro do range do for
'''i = int (input('inicio'))
p= int (input('passo'))
f = int (input('fim'))
for c in range(i,f+1,p):#range = (inicio,fim+1,passo ou pulo)
    print(c)
print('fim')'''

# dessa forma esta fazendo somatoria
'''s = 0
for c in range(0, 4):
    n=int(input('digite uma valor'))#esse input vai rodar 4 vezes
    s += n # aqui é igua a variavel s recebendo n+1 ( s=n+1 ou s+=n)
print('O somatorio de todos os valores foi {}'.format(s))'''
