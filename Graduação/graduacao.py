#Vairável INT = Aceita somente número inteiro

#Variável FLOAT = Aceita números inteiros e flutuantes (decimais)

#MOD (%) = Resto de uma divisão inteira

#DIV INT (//) = Quociente inteiro da divisão

#DIV FLOAT (/) = Quociente inteiro ou decimal da divisão

#IMPORT = Importação de biblioteca externa




####### CALCULADORA ###########



valor = int(input("Digite um valor: "))

valor = valor + 2

print("Resultado = " , valor)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

valor1 = ((((valor1 + 2) - 6) * 4) / 2)
valor2 = valor2 + 3 - 5 + 10 / 5
valor3 = valor2 - valor1
valor4 = valor1 + valor2

print('Resultado intermediário = ' , valor1)
print('Resultado intermediário 2 = ' , valor2)
print('Resultado final 1 = ' , valor3)
print('Resultado final 2 = ' , valor4)

import math

numero = int(input('Valor: '))

#numero = numero ** 0.5

raiz_quadrada = math.sqrt(numero)

print('Raíz quadrada = ', raiz_quadrada)

valor_final = valor + valor3 + valor4 + raiz_quadrada

print('Conclusão = ' , valor_final)



####### CÁLCULO DE ÁREA ###########



print('Cálculo do volume do cone')

raio = int(input('Valor do raio = '))
altura = int(input('Valor da altura = '))
pi = 3.14

volume = (pi * (raio ** 2) * altura) / 3

print('Volume do Cone = ' ,volume , 'cm³')



####### EXPRESSÕES ARITIMÉTICAS LÓGICAS E RELACIONAIS EM PYTHON ###########



#Atividade 1:

print('***Atividade 1: ***')

X = int(input('Valor de x = '))

X_quadrado = (X ** 2)

print('O valor de x² = ', X_quadrado)





#Atividade 2:


print('***Atividade 2: ***')

horas = int(input('Valor em horas = '))
minuto = int(input('Valor em minutos = '))
segundo = int(input('Valor em segundos = '))

grau = (horas * 15) + (minuto / 60) + (segundo / 3600)

print('Valor em graus = ', grau)








#Atividade 3:

print('***Atividade 3: ***')

C = int(input('Medida em C° = '))

F = (9/5) * C + 32

print('Temperatura em Fahrenheit = ', F)








#Atividade 4:

print('***Atividade 4: ***')

salario_minimo = 1621
salario_pessoal = int(input('Valor do seu salário = '))

resultado = (salario_pessoal / salario_minimo)

print('Você recebe', resultado, 'salários mínimos')





# Atividade 5:

print('***Atividade 5: ***')

dolar = float(input('Valor atual do dólar = '))
reais = float(input('Quantos reais disponíveis?'))

resultado2 = reais / dolar

print(reais, 'reais equivale a', resultado2, 'dólares na cotação atual')





#Atividade 6:

print('***Atividade 6: ***')

A = float(input('Nota A = '))
B = float(input('Nota B = '))
C = float(input('Nota C = '))

media_final = (A * 2 + B * 3 + C * 5) / 3

print('Sua média vale ', media_final)





#Atividade 7:

print('***Atividade 7: ***')

import math

Xa = int(input('Valor de Xa = '))
Xb = int(input('Valor de Xb = '))
Ya = int(input('Valor de Ya = '))
Yb = int(input('Valor de Yb = '))

D = math.sqrt(((Xb - Xa) ** 2) + ((Yb - Ya) ** 2))

print('A distância do ponto A ao ponto B é ', D, 'metros')





#Atividade 8:

print('***Atividade 8: ***')

nome = input('Qual seu nome? ')
horas = int(input('Quantas horas trabalhadas? '))
valor_hora = int(input('Quanto você recebe por hora? '))

resultado = horas * valor_hora

print(nome, 'recebe', resultado, 'reais')





#Atividade 9:

print('***Atividade 9: ***')

km = float(input('Quantos quilômetros rodados? ')) * 0.15
dias = float(input('Por quantos dias o carro foi alugado? ')) * 70

aluguel = km * dias

print('Você deve pagar ', aluguel, 'reais')





#Atividade 10:

print('***Atividade 10: ***')

vendedor = input('Qual seu nome? ')
salario_fixo = int(input('Qual seu salário fixo? '))
comissao = int(input('Quantas vendas efetuadas esse mês? ')) * (15/100)

total = salario_fixo + comissao

print('vendedor, você recebe ', total, 'no fim do mês')





#Atividade 11:

print('***Atividade 11: ***')

gasto_cliente = int(input('Valor gasto = '))
gorjeta = int((10 / 100) * gasto_cliente)

total = gasto_cliente + gorjeta

print('O valor total a ser pago é', total)





#Atividade 12:

print('***Atividade 12: ***')

total_vendas = int(input('Total de vendas = '))
sapatos_vendidos = int(input('Sapatos vendidos = '))

valor_recebido = (total_vendas * (20/100) + (5 * 2 * sapatos_vendidos))

print('O valor recebido no fim do mês é', valor_recebido)





#Atividade 13:

print('***Atividade 13: ***')

troco = int(input('Quantidade em reais = '))
cinquenta = int(troco * 2)
vinte_cinco = int(troco * 4)
dez = int(troco * 10)
cinco = int(troco * 20)
um = int(troco * 100)

print('50 =', cinquenta,';' ,   '25 =', vinte_cinco,';' ,   '10 =', dez,';' ,   '5 =', cinco,';' ,  '1 =', um)







###############  ##############

#nome = 'Matheus'
#idade = 21
#altura = 1.78

#if idade == 21 :
# print(f'O nome é {nome}, tem {idade} anos e {altura:.3f} cm²')




x = 55
y = 55

if x > 0 and y == x :
    print(f'Valor de x = {x} e valor de y = {y}')
else :
  print('falha')


if x < 0 :
     print('IF armazenou')
elif x > 4 :
  print('ELIF armazenou')
else:
  print('ELSE armazenou')


print('=============\n=============\n=============\n=============\n=============\n=============\n=============\n=============')



nota = int(input('Digite o valor da nota (Valor entre 0 e 100) '))
freq = int(input('Digite o valor da frequência (Valor entre 0 e 100)'))

if nota > -1 and nota < 101 and freq > -1 and freq < 101 :
  if freq > 74 :
    if nota > 65 :
      print('Parabéns, aprovação!!!')
    elif nota > 35 :
      print('Infelizmente, recuperação para você')
    else:
      print('Reprovado por nota!')
  else:
    print('Reprovado por falta!')
else:
  print('Ponha os valores solicitados!!')
