opcao = 0
while opcao != 5:
    v1 = float(input('Digite um novo valor '))
    v2 = float(input('Digite outro valor '))
    print('Escolha uma opção:')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')

    opcao = float(input('DIGITE A OPÇÃO '))

    if opcao == 1:
        soma = v1+v2
        print('A soma de {:.2f} + {:.2f} é = {:.2f}'.format(v1,v2,soma))
    elif opcao == 2:
        mult = v1*v2
        print('A Multiplicação {:.2f} X {:.2f} é = a {:.2f}'.format(v1,v2,mult))
    elif opcao == 4:
        print('')
    elif opcao == 3 and v1>v2:
        maior = v1
        print('O Maior entre {:.2f} e {:.2f} é {:.2f}'.format(v1, v2, maior))
    elif opcao == 3 and v2>v1:
        maior = v2
        print('O Maior entre {:.2f} e {:.2f} é {:.2f}'.format(v1,v2,maior))

else:
    print('FIM')