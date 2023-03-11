print("OLÁ MUNDO!!!")

x=10
nome = "Teste"
nota = 8.5
flag = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(flag))

nome = input("Digite o seu nome: ")

#usando formatadores de caracteres
print("Olá %s bem vindo(a) a disciplina de programação Python." %nome)

#usando a função format()
print("Olá {} bem vindo(a) a disciplina de programação Python.".format(nome))

#usando formatação de strings Python v3.6
print(f"Olá {nome} bem vindo(a) a disciplina de programação Python.")

if nome :
    print("Nome válido!!!")
else :
    print("Nome vazio.")

#Estrutura Lógica Relacionais '==, !=, >, <, >=, <='
cor = input("Digite uma cor ('verde', 'amarelo', 'vermelho'): ")

if cor == 'verde':
    print('Acelerar')
elif cor == 'amarelo':
    print('Atenção')
elif cor == 'vermelho':
    print('Parar')
else :
    print('Cor Inválida!!!')

#Estrutura Lógica Condicional 'and, or, not'
qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno APROVADO!!! :)")
else:
    print("Aluno reprovado :(")

#Estrutura Lógida de Repetição 'while'
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

#Estrutura Lógida de Repetição 'for'
palavra = "LOOPING"

for c in palavra:
    print(c)

for i,c in enumerate(palavra):
    print(f"Posição = {i}, valor = {c}")

for x in range(5):
    print(x)

#Exemplo de uso do break
print("---------- break ------------")
disciplina = "Linguagem de programação"

for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

print("---------- continue ------------")
#Exemplo de uso do continue
for c in disciplina:
    if c == 'a' or c == 'ã':
        continue
    else:
        print(c)

print("---------- eval() ------------")
a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")

#Definindo funções
def imprimir_mensagem(disciplina, curso):
    print(f"\nMinha primeira função em Python desenvolvida na disciplina: {disciplina} do curso: {curso}.\n")

#chamando a função imprimir_mensagem
imprimir_mensagem("Python", "ADS")


def somar(a, b):
    return a + b

#chamando a função somar e imprimindo o retorno
print(somar(2,3))


#Função com paramêtro default caso não seja informado na chamada da função
def calcular_desconto(valor, desconto = 0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

#chamando a função calcular_desconto com apenas o parâmetro valor
valor1 = calcular_desconto(100)
#chamando a função calcular_desconto passando os 2 parâmetros
valor2 = calcular_desconto(100, 0.25)

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")


#enviando os parâmetros em qualquer ordem precisa identifica o nome e valor
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
#passagem nominal de parâmetros na chamada da função
texto = converter_maiuscula(flag_maiuscula=True, texto="João")
print(f"\n{texto}")

#função com passagem de parâmetros com quantidade não definida
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")
print("\nChamada 2")
imprimir_parametros(10, "São Paulo")

#passagem nominal e não posicional
def imprimir_parametros2(**kwargs):
    print(f"\tTipo de objeto recebido = {type(kwargs)}\n")
    qtda_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtda_parametros}")

    for chave, valor in kwargs.items():
        print(f"Variável = {chave}, valor = {valor}")

print("\nChamada 1:")
imprimir_parametros2(cidade="Porto Alegre", idade=36, nome="Roberta")
print("\nChamada 2")
imprimir_parametros2(desconto=0.50, valor=100)

#expressão lambda
somar = lambda x, y: x + y
result = somar(x=5, y=3)
print(f"\n{result}")