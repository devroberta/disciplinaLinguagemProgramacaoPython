# função in busca dentro de uma estrutura de dados linear
lista = 'Roberta Getulio Olavo João Maria'
print('Olavo' in lista)

# Algoritmo de bunca linear
def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

# posição de um caracter
vogais = 'aeiou'
resultado = vogais.index('i')
print(resultado)

# funções de estrutura de dados
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"\nTamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 9 primeiras letras são: {texto[0:10]}\n")

# função split()
palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}\n")

# estrutura de repetição
vogais = ['a', 'e', 'i', 'o', 'u']
for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

# listas
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("\nAntes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp = ", linguagens)

# função map() e filter()
print("\nExemplo map()")
linguagens1 = '''Python,Java,JavaScript,C,C#,C++,Swift,Go,Kotlin'''.split(',')
nova_lista = list(map(lambda x : x.lower(), linguagens1))
print(f"A nova lista é = {nova_lista}\n")

print("\nExemplo filter()")
numeros = list(range(0,21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# tupla - tupla = () ou tupla = ('a','b','c') ou tuple()
vogais = ('a', 'e', 'i', 'o','u')
print(f"\nTipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

# set exemplo: len(s) - x in s - x not in s
s = 'exemplo set'
print(f"\nSet usando len = {len(s)}")
print(f"Set contem o character 'x' = {'x' in s}")
print(f"Set não contem o character 'a' = {'a' not in s}")

# objeto mapping (chave, valor) chamado de dict(dicionário)
# construtor dicionario = {} ou dicionario = {'one':1, 'two':2, 'three':3} ou dict()
# Exemplo 1
dici_1 = {}
dici_1['nome'] = 'João'
dici_1['idade'] = 30
print('\nExemplo 1: ', dici_1)

# Exemplo 2
dici_2 = {'nome':'João', 'idade':30}
print('Exemplo 2: ', dici_2)

# Exemplo 3
dici_3 = dict([('nome','João'), ('idade',30)])
print('Exemplo 3: ',dici_3)

# NumPy
import numpy

matriz_1_1 = numpy.array([1,2,3]) #cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1,2], [3,4]]) #cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1,2], [3,4], [5,6]]) #cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1,2,3],[4,5,6]]) #cria matriz 2 linhas e 3 colunas

print('\n', type(matriz_1_1))
print('\n matriz_1_1 = \n', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)

# Busca Binária
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista -1)

    while minimo <= maximo:
        #Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        #Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1       
        else:
            return True #Se o valor for encontrado para aqui
        
    return False #Se chegar até aqui, significa que o valor não foi encontrado

# Algoritmos de Ordenação
lista = [10,4,1,15,-3]
print('\nlista = ',lista, '\n')
lista_ordenada1 = sorted(lista)
lista.sort()
print('lista_ordenada1 = ', lista_ordenada1)
print('lista = ', lista)

# ordenação por comparação
lista = [7,4]
print('\n',lista)
if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux
print('\n',lista)

# outra forma de ordenação
lista = [5,-1]
print('\n', lista)
if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
print('\n', lista)

# Selection sort
def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0,n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
            lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista
lista = [10,9,5,8,11,3]
print('\nLista Original = ', lista)
print('Lista Ordenada = ', executar_selection_sort(lista))

# Bubble sort (algoritmo da bolha)
def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
lista = [10,9,5,8,11,3]
print('\nLista Original = ', lista)
print('Lista Ordenada = ', executar_bubble_sort(lista))

