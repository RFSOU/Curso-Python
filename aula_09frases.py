#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender
# são o Fatiamento de String, Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(), capitalize(), title(),
# strip(), junção com join().

# para imprimir um texto inteiro longo basta digitar ''' no começo e no fim da frase.
#fatiamento
# colchete no python é o identificado de uma estrutura de dados chamada
# de lista
frase = ('curso em video python')
'''print(frase[0:5])
print(frase[:5])
print(frase[0:])
print(frase[9::3])
print(frase[15:])
print(len(frase)) #analisa o tamanho da frase'''
#print(frase.count('o')) # conta quantas letras o tem na variavel frase
#print(frase.count('o',0,13))# mostra quantas letras "o" tem entre a posição
#0,13
#print(frase.find('deo'))# indica onde começa "deo" na frase
#print(frase.find('joão'))# respode com -1 quando não encontra a string.
print('video' in frase)
#print(frase.replace('python','android'))# substitui python por android.
#print(frase.upper()) # upper trasforma tudo que é minusculo em maiusculo
#print(frase.lower()) # lower trasforme tudo que é maisculo em minusculo.
#print(frase.capitalize())# capitalize trasfoma só a primeira palavra em
# maiusculo
#print(frase.title()) # coloca todas as palavras da frase com começo em
# maiusculo
#print(frase.strip()) # remove espaços no começo e no fim desneceçario
#print(frase.rstrip())# remove espaços na direita
#print(frase.lstrip())# remove espaços na esquerda
#print(frase.split()) # faz a divisão da frase fazendo com  que ela tenha
                     # indices novos
print(''.join(frase))




