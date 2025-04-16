#tarefa8

# Tarefa 8: Faça um programa em Python que leia os 4 lados A, B, C e D de um quadrilátero (valores inteiros) e diga se o mesmo é um quadrado, um retângulo ou um quadrilátero qualquer. Considere que os lados A e C são opostos, bem como os lados B e D.
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# Exemplo 1:
# lado A = 10
# lado B = 10
# lado C = 10
# lado D = 10
# QUADRADO
# 
# Exemplo 2:
# lado A = 10
# lado B = 20
# lado C = 10
# lado D = 20
# RETANGULO
# 
# Exemplo 3:
# lado A = 10
# lado B = 20
# lado C = 30
# lado D = 20
# QUADRILATERO

lado1 = int(input("lado A = "))
lado2 = int(input("lado B = "))
lado3 = int(input("lado C = "))
lado4 = int(input("lado D = "))

if lado1==lado2 and lado1==lado3 and lado1==lado4:
    print("QUADRADO")
elif lado1==lado3 and lado2==lado4 and lado1!=lado2:
    print("RETANGULO")
else:
    print("QUADRILATERO")