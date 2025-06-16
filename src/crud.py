import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="castracao_animal"
    )

def menu():
    print("\n--- MENU ---")
    print("1. Cadastrar animal")
    print("2. Listar animais")
    print("3. Sair")

def cadastrar_animal():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Nome do animal: ")
    idade = int(input("Idade: "))
    cursor.execute("INSERT INTO animais (nome, idade) VALUES (%s, %s)", (nome, idade))
    conexao.commit()
    print("✅ Animal cadastrado!")
    cursor.close()
    conexao.close()

def listar_animais():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM animais")
    for (id, nome, idade) in cursor:
        print(f"ID: {id}, Nome: {nome}, Idade: {idade}")
    cursor.close()
    conexao.close()

while True:
    menu()
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar_animal()
    elif opcao == "2":
        listar_animais()
    else:
        break
