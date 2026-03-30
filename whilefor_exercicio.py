clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for i in clientes:
  print(i)

contador = 0

while contador < 10:
  print("Processando dados...")
  contador += 1

buscantes = 0

while buscantes < 5:
  print('Bem-vindo ao Buscante!')
  buscantes += 1

buscante = 'Bem-vindo ao Buscante!'

for i in range(5):
  print(buscante)

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma total das receitas é: {soma}")

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i in projetos:
  if i == None:
    print('Projeto Ausente')
  else:
    print(i)

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for i in livros:
  if i is "O Hobbit":
    print('Livro: hobbit encontrado')
    break
  else:
    continue

estoque = 5

while estoque > 0:
    estoque -= 1 
    print(f"Venda realizada! Estoque restante: {estoque}")

print("Estoque esgotado")

diferencinha = 1

for segundos in range(10, 0, -1):
  segundos -= diferencinha
  if segundos % 2 == 0:
    print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
  else:
    print(f'A contagem continua: {segundos} segundos restantes.')

print('Aproveite a promoção agora!')
    
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break