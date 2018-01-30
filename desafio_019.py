from random import choice # carrega o metodo choice do modulo random
n1 = str (input ('primeiro aluno:'))
n2= str (input('segundo aluno'))
n3= str (input('terceiro aluno'))
n4= str (input('quarto aluno'))
lista = [n1,n2,n3,n4] # cria uma lsita com as variaveis n1,n2,n3,n4
escolhido = choice(lista) #aplica o metodo choice na lista e insere na
# variavel escolhido
print ('O aluno escolhido foi:{}'.format(escolhido))

