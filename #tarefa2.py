#tarefa2

#Tarefa 2: Faça um programa em Python que leia o número de horas trabalhadas por um funcionário durante um mês, o valor que recebe por hora, o número de horas extras trabalhadas e o número de dependentes. O número de horas trabalhadas durante um mês não inclui o número de horas extras. O programa deve calcular e imprimir o salário deste funcionário, sabendo-se que para cada hora extra o valor recebido é o dobro do valor normal e que cada dependente acrescenta 5% ao salário normal (sem contabilizar horas extras).

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo de formatação com duas casas decimais: print(f'valor = {valor:.2f}')

#Exemplo 1:

#numero de horas trabalhadas no mes = 100
#valor recebido por hora = 20
#numero de horas extras trabalhadas = 10
#numero de dependentes = 2
#valor total do salario = 2600.00

#Exemplo 2:

#numero de horas trabalhadas no mes = 160
#valor recebido por hora = 40
#numero de horas extras trabalhadas = 8
#numero de dependentes = 4
#valor total do salario = 8320.00

numero_de_horas_trabalhadas = (int(input("numero de horas trabalhadas no mes = ")))
valor_que_recebe_por_hora = (int(input("valor recebido por hora = ")))
numero_de_horas_extras_trabalhadas = (int(input("numero de horas extras trabalhadas = ")))
numero_de_dependentes = (int(input("numero de dependentes = ")))
salario1 = (valor_que_recebe_por_hora * numero_de_horas_trabalhadas) 
salario2 = (salario1) + (numero_de_horas_extras_trabalhadas * (valor_que_recebe_por_hora * 2)) + (numero_de_dependentes * (salario1 * 0.05))
print (f'valor total do salario = {salario2:.2f}')