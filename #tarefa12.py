#tarefa12

# Tarefa 12: Faça um programa em Python que leia 3 números inteiros positivos e diferentes entre si. Em seguida, o programa deve informar a média aritmética (“truncada”, ou seja, a parte inteira da média) dos mesmos. Informe também o primeiro número que está mais próximo do valor da média. 
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# A função abs() retorno o valor absoluto do valor passado como parâmetro. Por exemplo, abs(30) retorna 30; abs(-30) retorna 30.
# 
# Exemplo 1:
# numero 1 = 30
# numero 2 = 10
# numero 3 = 19
# media truncada = 19
# numero mais proximo da media = 19
# 
# Exemplo 2:
# numero 1 = 15
# numero 2 = 40
# numero 3 = 16
# media truncada = 23
# numero mais proximo da media = 16

import math
num1 = (int(input("numero 1 = ")))
num2 = (int(input("numero 2 = ")))
num3 = (int(input("numero 3 = ")))
medari = (num1 + num2 + num3)//3
print("media truncada = ", medari)

num12 = abs(num1 - medari)
num22 = abs(num2 - medari)
num32 = abs(num3 - medari)

if num12 <= num22 and num12 <= num32:
    print("numero mais proximo da media = ", num1)
elif num22 <= num32:
    print("numero mais proximo da media = ", num2)
else:
    print("numero mais proximo da media = ", num3)

