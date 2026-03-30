apples = 15
bananas = 3

if apples > bananas:
  print('As maçãs tiveram as mais vendidas!')
elif apples < bananas:
  print('As bananas tiveram as mais vendidas!')
else:
  print('As vendas foram iguais!')

a_dias = int(input('Informe a quantidade de dias para a atividade A '))
b_dias = int(input('Informe a quantidade de dias para a atividade B '))
c_dias = int(input('Informe a quantidade de dias para a atividade C '))

if a_dias >= 0 and b_dias >= 0 and c_dias >= 0:
  tempo_total = a_dias + b_dias + c_dias
  print(f'O tempo total foi de {tempo_total}')
else:
  print('Erro, os dias não podem ser negativos.')

temperatura = int(input('Digite a temperatura: '))

if temperatura > 25:
  print('Alerta! Servidores sobreaquecendo!')
else:
  print('Tudo aos seus conformes!')

peso = int(input('Digite seu peso: '))
altura = int(input('Digite sua altura: '))

IMC = peso / (altura**2)

if IMC > 25:
  print('Você está acima do peso.')
elif IMC <= 18.5:
  print('Você está abaixo do peso.')
else:
  print('O seu peso está comum.')

despesa_total = float(input('Digite o quanto gastou: '))

if despesa_total <= 3000:
  print('Você está indo bem!')
else:
  print('Você ultrapassou o limite.')

horas = float(input('Digite que horas são em formato de 24H: '))

if  8 <= horas > 18:
  print('Daqui não passarás')
else:
  print('Passarás.')

distancia = float(input('Digite a distância percorrida: '))

if distancia <= 100:
  print('Custará 10 reais.')
elif 100 < distancia <= 200:
  print('Custará 20 reais.')
else:
  print('Custará 30 reais.')

par = int(input('Digite um número: '))

if par % 2 == 0:
  print('É par.')
else:
  print('ímpar.')