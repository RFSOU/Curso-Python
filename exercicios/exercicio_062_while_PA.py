a1 = int(input('Qual o primeiro termo da PA'))
r = int(input('Qual é a razão da PA'))
print(' PA DE RAZÃO {} = {}'.format(r,a1))
n = 1
total = 0
mais = 10
while mais != 0:
    total = total+mais
    while n < total:
        a1 = a1+r
        n = n+1
        print((' PA DE RAZÃO {} = {}').format(r, a1))
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?'))
print('O total de PA solicitado foi {}, obrigado.'.format(total))







