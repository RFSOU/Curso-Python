'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o'''

n=0
soma=0
for c in range(0,6):
    n = int(input('Digite um numero.'))
    if n%2==0:
        soma = n+soma
print('A soma dos numeros pares é:',soma)




