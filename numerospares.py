fim = int(input('Digite o mumero final para impressão'))
x=0 # o valor aqui é 0 porque ele é o primeiro numero par

while x <= fim:
    if x%2==0:
        print(x)
    x=x+1
