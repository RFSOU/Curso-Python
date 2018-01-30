'''crie um programa que leia uma frase qualquer e diga se ela é um palindromo
desconsidenrando os espaços'''

frase = str(input('Escreva uma frase.')).strip().upper()# nesta entrada tiramos os espaços com strip e mudamos tudo para maisculo com upper
palavras = frase.split()#palavras recebe frase splitada
junto = ''.join(palavras)# junto recebe palavras todas juntas sem espaço

#for letra in range (len(junto)-1,-1,-1): '''esse for conta os caracteres na variavel junto,,, letra vai correr todas as letras de junto o atributo -1 quer dizer se tem 20 letras vai contar - uma e -1 por que vai contar até 0 e -1 porque vai ser contagem regressiva essa é uma forma de analisar uma palavra do final para começo utilizando o for'''


inverso = junto[::-1]# atributo de fatiamento ::-1 pega o conteundo davariavel junto do começo ao final e joga do final para o começo na variavel inverso
if inverso == junto: # compara
    print('{} e {} são iguais'.format(inverso,junto))
    print('É um Palindromo')
else:
    print('{} e {} não são iguais'.format(inverso, junto))
    print('Não é um Palindromo')


'''if (frase.find('joão paulo'))== 0: #retorna um -1 se a frase não for encontrada
    print('ok')
else:
    print('errado')'''