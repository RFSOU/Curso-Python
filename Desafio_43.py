'''desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5 abaixo do peso
 -Entre 18.5 e 25: peso ideal
 -25 até 30 sobrepeso
 -30 até 40 obesidade
 -acima de 40 obesidade morbida'''
peso = float(input('Qual é o seu peso?'))
altura =float(input('Qual é a sua altura?'))
imc = peso/altura
if imc<=18.5:
    print('Você esta a baixo do peso.')
elif imc>18.5 and imc < 25:
    print('Seu esta peso ideal')
elif imc >25 and imc < 30:
    print('Você esta com sobre peso.')
elif imc > 30 and imc < 40:
    print(' Você esta obeso.')
elif imc > 40:
    print('Você esta com obsidade morbida.')
else:
    print('Obrigado')