#tarefa7

#Tarefa 7: Faça um programa em Python que solicite a quantidade de quilômetros percorridos em uma corrida (km), o peso da pessoa que correu (kg) e o tempo (min) que a corrida demandou. O programa deve imprimir o total de calorias gastas, considerando o cálculo de calorias abaixo:

#Total Gasto de Calorias = Velocidade (em km/h) x Peso (em kg) x 0,00175 x Tempo (em min)

#Observe que a velocidade está em km/h e o tempo fornecido como entrada está em minutos.

#O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.

#Exemplo de formatação com duas casas decimais: print(f'valor = {valor:.2f}')

#Exemplo 1:
#distancia percorrida (em km) = 4
#tempo da corrida (em min) = 30
#peso da pessoa (em kg) = 50
#total gasto de calorias = 21.00

#Exemplo 2:
#distancia percorrida (em km) = 1
#tempo da corrida (em min) = 6
#peso da pessoa (em kg) = 80
#total gasto de calorias = 8.40
    
import math

km = (int(input()))
minuto = (int(input()))
kg = (int(input()))


hora = minuto / 60
velocidade = km / hora
cal = (velocidade * kg * 0.00175 * minuto)

print("distancia percorrida (em km) = ")
print("tempo da corrida (em min) = ")
print("peso da pessoa (em kg) = ")
print(f'total gasto de calorias = {cal:.2f}')
