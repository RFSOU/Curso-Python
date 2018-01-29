#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('\033[7;30;0m Qual é a velocidade atual do carro?\033[m'))
if velocidade > 80:
    print('-=-'*20)# Cria uma linha divisoria
    print('\033[7;30;0m MULTADO! Você excedeu o limete permitido que é de 80km/h \033[m')
    multa = (velocidade -80)*7
    print('-=-' * 20)
    print('\033[7;30;31m Você deve pagar uma multa de R$ {:.2f}\033[m'.format(multa))


else:
    print('\033[0;30;31m Tenha um bom dia! Dirija com segurança!\033[m')

 # \033[0;30;31m  "cria um padrão com estilo cor de texto e cor de fundo".
    # \033[m  "encerra na linha um padrão de cores a ser impressa".