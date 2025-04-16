#tarefa6

#Tarefa 6: Faça um programa em Python para calcular e imprimir o dígito verificador de uma conta bancária. O usuário deve informar o número da conta que deve ser um número inteiro com 4 dígitos. O dígito verificador será calculado como segue:

#Somar todos os quatro dígitos.
#Multiplicar todos os quatro dígitos.
#Subtrair o resultado da soma (passo 1) do resultado da multiplicação (passo 2).
#O dígito verificador será o resto da divisão do resultado da subtração (passo 3) por 9.
#Por exemplo, se o usuário informar o número 5678 como entrada, o programa deverá somar os quatro dígitos (5+6+7+8 = 26) e multiplicar os quatro dígitos (5*6*7*8 = 1680). Em seguida deverá diminuir a soma da multiplicação (1680-26 = 1654). Por último obter o resto da divisão da subtração por 9, que será o dígito verificador (1654%9 = 7).

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo 1:
#numero da conta (4 digitos) = 5678
#digito verificador = 7

#Exemplo 2:
#numero da conta (4 digitos) = 4444
#digito verificador = 6

import math
num = (int(input("numero da conta (4 digitos) = ")))
num1 = num // 1000
num_restante = num % 1000
num2 = num_restante // 100
temp = num_restante % 100
num3 = temp // 10
num4 = temp % 10
soma = int(num1 + num2 + num3 + num4)
mult = int(num1 * num2 * num3 * num4)
sub = mult - soma
resto = sub % 9
print ("digito verificador =" , resto)