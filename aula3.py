# Python Orientado a Objetos

# minha primeira classe
class PrimeiraClasse:

    def imprimir_mensagem(self, nome): #Criando um método
        print(f"Olá {nome}, seja bem vindo!")

objeto1 = PrimeiraClasse() # Instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('João') # Invocando o método

objA = PrimeiraClasse()
objA.imprimir_mensagem('Roberta')

# Construtor da classe __init__()
class Televisao:
    def __init__(self):
        self.volume = 10
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()
print("\nVolume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)

# Classes com métodos privados
class ContaCorrente:
    def __init__(self):
        self._saldo = None
    def depositar(self, valor):
        self._saldo += valor
    def consulta_saldo(self):
        return self._saldo
    
# Herança
class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
    def bater_ponto(self):
        #Código aqui
        print("Ponto Aceito!")
        pass
    def fazer_login(self):
        #Código aqui
        print("Logado!")
        pass

class Cliente(Pessoa):
    def __init__(self):
        self.telefone = None

f1 = Funcionario()
f1.nome = "Funcionario A"
print("\n",f1.nome)

c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)

# Métodos mágicos método dir() chama todos os recursos da classe-base chamada object
print(dir(Pessoa()))

# Acesso banco de dados PostgreSQL
import sqlite3
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

ddl_create = """
CREATE TABLE fornecedor (
id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome_fornecedor TEXT NOT NULL,
cnpj VARCHAR(18) NOT NULL,
cidade TEXT,
estado VARCHAR(2) NOT NULL,
cep VARCHAR(9) NOT NULL,
data_cadastro DATE NOT NULL
);
"""

cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))
print("Tabela criada!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
