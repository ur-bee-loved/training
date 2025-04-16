#tarefa11

# Tarefa 11: Faça um programa em Python que leia as três notas de um aluno (números float). O programa deve calcular a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes seja 2. Imprima uma mensagem 'Aprovado' se a média for maior ou igual a 5.75 e 'Reprovado' se a média for menor que 5.75. Não utilize as funções max() ou min().
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# Exemplo 1:
# nota 1 = 4
# nota 2 = 4
# nota 3 = 7
# Reprovado
# 
# Exemplo 2:
# nota 1 = 5
# nota 2 = 6
# nota 3 = 6
# Aprovado

nota1 = float(input("nota 1 = "))
nota2 = float(input("nota 2 = "))
nota3 = float(input("nota 3 = "))
nota = 0
if nota1>=nota2 and nota1>=nota3:
    nota = (nota1 * 4 + nota2 * 2 + nota3 * 2)/8
elif nota2>=nota1 and nota2>=nota3:
    nota = (nota1 * 2 + nota2 * 4 + nota3 * 2)/8
elif nota3>=nota1 and nota3>=nota2:
    nota = (nota1 * 2 + nota2 * 2 + nota3 * 4)/8
    
if nota>=5.75:
    print("Aprovado")
else:
    print("Reprovado")