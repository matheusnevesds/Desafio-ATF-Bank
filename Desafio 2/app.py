from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Habilita o Cross-Origin Resource Sharing (CORS) para todas as rotas
CORS(app)

# Configurações de conexão com o banco de dados
DATABASE_FILE = 'C:caminho-do-seu-data-base/Database.accdb'
DRIVER = '{Microsoft Access Driver (*.mdb, *.accdb)}'

# Função para obter a conexão com o banco de dados
def get_db_connection():
    conn_str = f'DRIVER={DRIVER};DBQ={DATABASE_FILE}'
    return pyodbc.connect(conn_str)

# Rota para adicionar dados via método POST
@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # Obtém os dados da requisição enviada pelo cliente
        data = request.get_json()
        print(f"Dados recebidos:{data}")
        emails = data.get('email')
        percentuais = data.get('percentual')
        print(f"Dados recebidos1:{emails}")
        print(f"Dados recebidos2:{percentuais}")

        # Estabelece conexão com o banco de dados
        conn = get_db_connection()

        # Insere cada registro (email e percentual) no banco de dados
        cursor = conn.cursor()
        for email, percentual in zip(emails, percentuais):
            email = str(email)
            percentual = str(percentual)
            print(f"Inserindo no banco de dados: {email}, {percentual}%")  # Imprime os dados a serem inseridos no console
            cursor.execute('INSERT INTO Vendedores (email, percentual) VALUES (?, ?)', (email, percentual))

        # Confirma as transações e fecha a conexão
        conn.commit()
        cursor.close()
        conn.close()

        print("Dados salvos com sucesso")  # Imprime mensagem de sucesso no console
        return jsonify({'message': 'Dados salvos com sucesso'}), 200
    except Exception as e:
        conn.rollback()
        print("Erro ao salvar os dados:", e)  # Imprime o erro no console
        return jsonify({'message': 'Erro ao salvar dados '}), 500

# Inicia a aplicação Flask quando o script é executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
