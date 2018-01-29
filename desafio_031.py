#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma
#viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
#de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('\033[7;30;45mDe quantos Km éa distancia da sua viajem\033[m'))
print('***'*20)
print(' \033[7;30;45mVocê esta prestes a começar uma viagem de {} km.\033[m'.format(distancia))
print('***'*20)
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(' \033[7;30;45mO preço de sua passagem sera de R$ {:.2f}\033[m '.format(preço))



