'''Elabore um programa que cacule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
- À vista dinheiro / cheque :10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão preço normal
- 3x ou mais no cartão 20% de juros'''
produto =float(input('Qual o preço do produto? '))
formapag = float(input('Digite uma opção para forma de pagamento:\n''1 pagamento a vista no dinheiro\n''2 pagamento a vista no cartão\n''3 pagamento em 2x no catão\n''4 pagamento em 3x ou mais'))
if(formapag == 1):
    print('OK seu pagamento sera a vista em dinheiro\n'' e você vai pagar  {:.2f}'.format(produto-produto*10/100))
elif (formapag == 2):
    print('OK seu pagamento sera a vista em cartão\n''e você vai pagar    {:.2f}'.format(produto-produto*5/100))
elif (formapag == 3):
    print('OK seu pagamento sera em 2x no cartão\n''e você vai pagar   {:.2f}'.format(produto))
elif (formapag == 4):
    print('OK seu pagamento sera em 3 x ou mais cartão\n''e você vai pagar {:.2f}'.format(produto + produto * 20 / 100))
else:
    print('ok')
