#tarefa 1

#Tarefa 1: Faça um programa em Python que leia um valor inteiro que representa o comprimento de um lado de um quadrado e imprima a área e o comprimento da diagonal deste quadrado. Lembre que diagonal2 = lado2 + lado2
#Quando o programa imprime "lado = ", o usuário deve entrar com o valor do lado do quadrado. Então o programa deve imprimir a área e o comprimento da diagonal, com duas casas decimais, seguindo os exemplos a seguir.

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo de formatação com duas casas decimais: print(f'area = {area:.2f}')

#Exemplo 1:

#lado = 10
#area = 100.00
#diagonal = 14.14

#Exemplo 2:

#lado = 5
#area = 25.00
#diagonal = 7.07

import math
lado_quadrado = (int(input("lado =  ")))
area_quadrado = lado_quadrado * lado_quadrado
print(f'area =  {area_quadrado:.2f}')
diagonal_quadrado = math.sqrt(lado_quadrado**2 + lado_quadrado**2)
print (f'diagonal =  {diagonal_quadrado:.2f}')