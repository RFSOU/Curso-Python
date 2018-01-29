import urllib.request
import json
url = 'https://educacao.dadosabertosbr.com/api/escolas/buscaavancada'
situação = '&energiaInexistente=on&aguaInexistente=on&esgotoInesistente'
resp = urllib.request.urlopen(url+situação).read()
resp = json.loads(resp.decode('utf-8'))
print('Numero de escolas em funcionamento sem energia,agua')
for x in resp[1]:
    print(x['nome'], x['cod'])
    print(x['cidade'],x['estado'], x ['regiao'])
    print()
