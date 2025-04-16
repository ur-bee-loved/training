#tarefa14

# Tarefa 14: Uma casa de câmbio vende diferentes moedas para brasileiros que desejam viajar para o exterior. O cliente informa a moeda desejada e dá um valor em reais para a compra. O operador do caixa acessa o sistema, informa a letra inicial da moeda a ser comprada, entra com o valor a ser convertido e o sistema informa o valor de conversão para a nova moeda.
# Faça um programa em Python que simula o sistema da casa de câmbio. O cliente fornece a letra correspondente à moeda e o valor em reais, e o programa retorna o valor convertido. Considere que, se mais de uma conversão precise ser realizada, o operador do caixa executa o programa novamente. Utilize a tabela a seguir para realizar as conversões disponíveis.
# 
# Tabela de conversão de moedas
# 
# Letra	Moeda	Moeda
# E	Euro	0.18
# D	Dólar	0.19
# M	Peso Mexicano	5.13
# A	Peso Argentino	40.43
# F	Franco Suíço	0.17
# Exemplo de formatação com duas casas decimais: print(f'valor = {valor:.2f}')
# 
# O texto de entrada e de saída tem que estar EXATAMENTE como aparece nos exemplos abaixo. A entrada que deve ser fornecida pelo usuário está destacada em itálico.
# 
# Exemplo 1:
# digite a moeda (E,D,M,A,F) = D
# digite o valor em reais = 300.00
# valor convertido = 57.00
# 
# Exemplo 2:
# digite a moeda (E,D,M,A,F) = E
# digite o valor em reais = 150.00
# valor convertido = 27.00


moeda = input("digite a moeda (E,D,M,A,F) = ")
real = float(input("digite o valor em reais = "))

if moeda == "E":
    print(f"valor convertido = {real*0.18:.2f}")
elif moeda == "D":
    print(f"valor convertido = {real*0.19:.2f}")
elif moeda == "M":
    print(f"valor convertido = {real*5.13:.2f}")
elif moeda == "A":
    print(f"valor convertido = {real*40.43:.2f}")
elif moeda == "F":
    print(f"valor convertido = {real*0.17:.2f}")
    
f"valor convertido = {real*0.18:.2f}"