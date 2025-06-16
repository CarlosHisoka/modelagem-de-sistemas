import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="castracao_animal"
)
cursor = conexao.cursor()

# Função para cadastrar animal
def cadastrar_animal():
    nome = input("Nome do animal: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    cursor.execute("INSERT INTO animais (nome, idade, peso) VALUES (%s, %s, %s)", (nome, idade, peso))
    conexao.commit()
    print("Animal cadastrado!")

# Menu interativo
while True:
    print("\n1 - Cadastrar animal\n2 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar_animal()
    else:
        break
