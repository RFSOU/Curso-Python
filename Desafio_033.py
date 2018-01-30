#Exercício Python 033: #Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

a= int(input('primeiro valor'))
b= int(input('segundo valor'))
c= int(input('terceiro valor'))
if a<b and a<c:
    menor= a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor = c

print('O menor valor digitado foi {}'.format(menor))
