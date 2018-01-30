import random # carrega o metodo choice do modulo random
n1 = str (input ('primeiro aluno:'))
n2= str (input('segundo aluno'))
n3= str (input('terceiro aluno'))
n4= str (input('quarto aluno'))
lista = [n1,n2,n3,n4] # cria uma lsita com as variaveis n1,n2,n3,n4
random.shuffle(lista) # mistura o coteudo da lista.
print ('A ordem de apresentação sera')
print (lista)
