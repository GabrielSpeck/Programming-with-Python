import os
# O "os" é uma biblioteca que permite mexer no console.

restaurant = []
# Lista.

def clear():
  # Definir função 'clear'.
  os.system('cls')
  # Função limpar o terminal.

def show_title():
  print('Sabor Express\n')


def show_option():
  print('1. Cadastrar Restaurante')
  print('2. Listar Restaurantes')
  print('3. Ativar Restaurante')
  print('4. Sair\n')

def go_back():
  input('\nDigite algo para voltar para o menu principal: ')
  # :linha_91: Antes de voltar para o menu principal, esse código é executado como uma pausa.
  
def close_app():
  clear()
  print('Finalizando APP.\n')

def register_restaurant():
  # definir função "registrar restaurante".
  clear()
  print('Cadastrar um novo restaurante:\n')
  name = input('Escreva o nome do restaurante: ')
  category = input('Escreva a categoria do restaurante: ')
  dados = {
    'Nome': name,
    'Categoria': category,
    'Ativo?': False
  }
  # Um dicionário organizando as informações.
  restaurant.append(dados)
  # O dicionário Dados sendo empurrado através do append para dentro da lista Restaurante.
  print(f'O restaurante, {name}, foi cadastrado com sucesso!')
  go_back()

def list_restaurant():
  # Definir uma função "Lista Restaurante".
  clear()
  text = "Lista dos Restaurantes:\n"
  # Variável que traz o subtítulo.
  print(text)
  # Imprimir a variável.
  print('-' * len(text))
  # Para cada caractere da variável através do len(), imprimir '-'
  for i in restaurant:
    print(f'- {i}')
    # Para cada índice na lista de restaurante, imprimir '-' e o índice.
  go_back()

def activate_restaurant():
  clear()
  name = input('Digite o nome do restaurante para solicitar a ativação: ')
  restaurant_found = False
  for i in restaurant:
    if name == i['Nome']:
      restaurant_found = True
      i['Ativo?'] = not i['Ativo?']
      # O código inverte o valor, possibilitando ativar e desativar. (not) serve para inverter.
      mensagem = f'O restaurante {name} foi ativado com sucesso.' if i['Ativo?'] else f'O restaurante {name} foi desativado com sucesso.'
      print(mensagem)
      go_back()
  if not restaurant_found:
    print('O restaurante não foi encontrado')
    go_back()

def choose_option():
  chosen_option = int(input('Escolha uma opção: '))
  
  if chosen_option == 1:
    register_restaurant()
  elif chosen_option == 2:
    list_restaurant()
  elif chosen_option == 3:
    activate_restaurant()
  elif chosen_option == 4:
    close_app()
    exit()
  else:
    print('Valor inserido errado.')
    go_back()
  # O (go_back) está por último fora do if/else para que ele seja o último.
  


def main():
  while True:
    # Permite que o main sempre repita quando o código encerrar.
    clear()
    show_title()
    show_option()
    choose_option()

if __name__ == '__main__':
  main()
  # __name__ é o arquivo principal, aqui nomeia-se como __main__ mesmo para uma leitura lisa.