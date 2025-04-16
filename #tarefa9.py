
#Tarefa 9: Faça um programa em Python que leia um número inteiro e imprima uma mensagem indicando se é par ou ímpar e também se é positivo ou negativo. Considere que o número zero é par, mas não é nem positivo nem negativo.

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo 1:
#numero = 10
#PAR
#POSITIVO

#Exemplo 2:
#numero = -10
#PAR
#NEGATIVO

import math
num = int(input("numero = "))
if num % 2 == 0:
    print("PAR")
else:
    print("IMPAR")

if num > 0:
    print("POSITIVO")
elif num<0:
    print("NEGATIVO") 