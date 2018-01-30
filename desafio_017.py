from math import floor,ceil,sqrt
cateto_op = float(input('entre com o valor do cateto oposto'))
cateto_ad = float(input('entre com o valor do cateto adjacente'))
soma_dos_lados_do_triangulo_retangulo_ao_quadrado = ((cateto_op**2)+(cateto_ad**2))
Raiz_quadrada_da_soma_dos_Lados_ao_quadrado = sqrt(soma_dos_lados_do_triangulo_retangulo_ao_quadrado)
print ('O valor da ipotenusa é {:.2f}'.format(Raiz_quadrada_da_soma_dos_Lados_ao_quadrado))





