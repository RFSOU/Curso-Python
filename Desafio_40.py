'''Crie um programa que leia 2 notas de um aluno e calcule sua média.mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0:
reprovado
-Média entre 5.0 e 6.9:
Recuperação
- Média entre 5.0 e 6.9:
recuperação
_Média 7'''
nota1 = float (input('Qual a primeira nota?'))
nota2 = float (input('Qual a segunda nota?'))
media = (nota1+nota2)/2
if media<5:
    print('Você foi reprovado')
elif media>=5.0and media<= 6.9:
    print('Você esta de recuperação')
else:
    print('Você foi aprovado!')