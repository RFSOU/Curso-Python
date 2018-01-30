'''A confederação nacional de natação prescisa de um programa que leia o ano de nacimento de um atleta e mostre sua categoria de acordo com sua idade:
-até 9 anos:mirim
-até 14 anos: infantil
-até 19 anos: junior
-até 20 anos: senior
_ Acima:master'''

from datetime import date

nascimento = int(input('Qua o ano do seu nascimento?'))
idade = date.today().year - nascimento
if idade <= 9:
    print('Sua categoria éa Mirim')
elif idade > 9 and idade <=14:
    print('Sua categoria éa Infantil')
elif idade > 14 and idade <= 19:
    print('Sua categoria éa Junior')
elif idade > 18 and idade <=20:
    print('Sua categoria éa Senior')
else:
    print('Sua categoria éa Master')

