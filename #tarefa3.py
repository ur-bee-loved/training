#tarefa3

#Tarefa 3: Faça um programa em Python que leia a idade de uma pessoa expressa em dias e informe a quantidade correspondente de anos, meses e dias. Quando o programa imprime "total de dias vividos = ", o usuário deve entrar com o número de dias vividos pela pessoa. Então o programa deve imprimir a quantidade de anos, de meses e de dias correspondente ao total de dias que a pessoa já viveu, seguindo os exemplos a seguir. Considere que todos os anos tem 365 dias e que todos os meses tem 30 dias.

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo 1:

#total de dias vividos = 13455
#anos = 36
#meses = 10
#dias = 15

#Exemplo 2:

#total de dias vividos = 2621
#anos = 7
#meses = 2
#dias = 6

total_de_dias_vividos = (int(input("total de dias vividos = ")))
anos = total_de_dias_vividos // 365
dias_restantes = total_de_dias_vividos % 365
meses = dias_restantes // 30
dias = dias_restantes % 30
print("anos =" , anos)
print("meses =" , meses)
print("dias =", dias)