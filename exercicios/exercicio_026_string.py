'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
aparece a letra "A", em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez.'''

frase = str (input('escreva uma frase')).upper() .strip() #neste caso foi
# possivel usar o upper na 'str e o strip para eliminar espaços'
print('\033[0;31;0mA letra A aparece {} vezes na frase.'.format(frase.count ('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1)) # find procura da
# esquerda para direta
print ('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #rfind procura
#da direita
#para esquerda


