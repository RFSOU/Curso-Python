'''aula 12 condições aninhadas dentro dessa estrutura pode ser usado
quantos elif forem precisos else 1 ou nenhum e 1 if no inicio'''


#if (carro.esquerdo()):
#elif (carro.direito()):
#else:()

'''nome = str(input('Qual é seu nome?'))
if nome == 'Rodrigo':
    print('Que bonito nome!')# até estrutura simples
else:
    print('Seu nome é bem normal.')
    print('Tenha um  bom dia, {}!'.format(nome)) # estrutura composta
    print()'''

n = str(input('Qual é seu nome?')).strip()
nome = n.capitalize()
if nome == 'Rodrigo':
    print('Que bonito nome!')# até estrutura simples
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.') #estrutura CONDICIONAL aninhada
else:
    print('Seu nome é bem normal.')
    print('Tenha um  bom dia, {}!'.format(nome)) # estrutura composta
    
