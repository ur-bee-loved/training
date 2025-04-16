#Tarefa4

#Tarefa 4: Faça um programa em Python que leia um número inteiro, que deve estar entre 100 e 999, e exiba o mesmo de forma invertida, um dígito por linha da tela.

#Exemplo:        237 ==> 7
#                        3
#                        2

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo 1:
#numero = 123
#3
#2
#1

#Exemplo 2:
#numero = 321
#1
#2
#3

import math
num = (int(input("numero =")))
num1 = num // 100
num_restante = num % 100
num2 = num_restante // 10
num3 = num_restante % 10
print(num3)
print (num2)
print (num1)