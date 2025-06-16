import mysql.connector  

def conectar():  
    try:  
        return mysql.connector.connect(  
            host="localhost",  
            user="root",  
            password="",  
            database="castracao_animal"  
        )  
    except Exception as e:  
        print(f"Erro ao conectar: {e}")  
        return None  

def criar_tabelas():  
    conn = conectar()  
    if conn:  
        cursor = conn.cursor()  
        cursor.execute("""  
            CREATE TABLE IF NOT EXISTS animais (  
                id INT AUTO_INCREMENT PRIMARY KEY,  
                nome VARCHAR(100) NOT NULL,  
                idade INT  
            )  
        """)  
        conn.commit()  
        print("✅ Tabelas criadas!")  
        cursor.close()  
        conn.close()  

if __name__ == "__main__":  
    criar_tabelas()  