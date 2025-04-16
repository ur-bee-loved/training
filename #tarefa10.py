#tarefa10

# Tarefa 10: Faça um programa em Python que leia 2 números float e um operador aritmético (+, -, *, /) e informe o resultado da operação sob os dois números.
# 
# Exemplo de formatação com duas casas decimais: print(f'valor = {valor:.2f}')
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# Exemplo 1:
# operando 1 = 10
# operador (+, -, *, /) = +
# operando 2 = 10
# resultado = 20.00
# 
# Exemplo 2:
# operando 1 = 9.5
# operador (+, -, *, /) = /
# operando 2 = 2
# resultado = 4.75

num1 = float(input("operando 1 = "))
operador = input("operador (+, -, *, /) = ")
num2 = float(input("operando 2 = "))
if operador == "+":
    print("resultado = ",  (f'{num1 + num2:.2f}'))
elif operador == "-":
    print ("resultado = ", (f'{num1-num2:.2f}'))
elif operador == "*":
    print ("resultado = ", (f'{num1 * num2:.2f}'))
else:
    print ("resultado = ", (f'{num1 / num2:.2f}'))
    