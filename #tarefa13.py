#tarefa13

# Tarefa 13: Faça um programa em Python que leia uma data (dia e mês) e diga se esta data está correta ou não. Para o mês de fevereiro podem ser aceitos 28 ou 29 dias.
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# Exemplo 1:
# dia = 30
# mes = 10
# data correta
# 
# Exemplo 2:
# dia = 32
# mes = 10
# data incorreta

dia= int(input("dia = "))
mes= int(input("mes = "))

if mes<1 or dia<1:
    print ("data incorreta")
elif mes>=13:
    print("data incorreta")
elif mes==2 and dia>=30:
    print("data incorreta")
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>=31:
    print("data incorreta")
elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>=32:
    print("data incorreta")
else:
    print("data correta")
