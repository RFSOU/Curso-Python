''' Crie um programa que leia o nome de uma cidade diga se ela começa ou
não com o nome SANTO '''

cid= str(input('Em que cidade você nasceu?')).strip()  # .strip() elimina
# espaços  depois do input
print(cid[:5].upper() == 'SANTO') # No caso [:5] são os caracteres
# a serem impressos
#.upper joga tudo que foi digitado para maiusculo para que elimini
# a possibilidade de erro quando o usuario for digitar











