def calcular_idade(ano_nascimento, ano_atual): 
    return ano_atual - ano_nascimento 
 
nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.")

palavra = input('Digite uma palavra: ')

def contador_palavra(palavra):
    return len(palavra)

print(f'Essa palavra tem {contador_palavra(palavra)} caracteres. ')

def horario(hora):
    if hora <= 12:
      return 'Bom Dia!'
    elif hora >= 13 and hora <= 18:
      return 'Boa Tarde!'
    else:
      return 'Boa Noite!'

horas = int(input('Digite que horas são: '))
print(horario(horas))



def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 


valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 


produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}")


soma = lambda x, y: x + y 

subtrai = lambda x, y: x - y 

multiplica = lambda x, y: x * y 

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 
 
if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida") 


def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       return valor - (valor * (porcentagem / 100))  

   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  

calcular_preco_final = criar_desconto(desconto) 

valor = float(input("Digite o valor da compra: "))  

print(f"Preço final com desconto: {calcular_preco_final(valor)}")


def soma_recursiva(n): 
    if n == 1: 
        return 1 
    return n + soma_recursiva(n - 1) 
 
numero = int(input("Digite um número: ")) 
print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}") 