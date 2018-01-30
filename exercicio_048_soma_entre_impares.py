'''faça um programa que calcula a soma entre todos os numeros impares que são multiplos de três e que se encontram no intervalo de 1 até 500'''
soma = 0
cont = 0
for c in range(1,501,2):
    if c %3 == 0:#se divisivel por 3 é multiplo de 3 sendo resto =0 então é multiplo de 3
        soma += c # no caso aqui é um acumulador soma recebe c + soma a cada repitição
        cont += 1# no caso contador cont recebe cont +1 em cada repetição
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
