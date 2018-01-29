n=10
soma = 0
while n <= 10:
    x = int(input('Digite o %d numero:'%n))
    soma = soma + x
    n = n + 1
print('A soma é %d'%soma,('A média é: %d'%int(soma/10)))
