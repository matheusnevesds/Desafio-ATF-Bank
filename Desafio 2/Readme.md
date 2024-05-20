# Desafio 2 - Salvando dados em um database com POST

Este repositório contém dois códigos que funcionam em conjunto: `app.py` e `index.html`. O primeiro é um servidor Flask que lida com requisições POST para adicionar dados a um banco de dados Microsoft Access. O segundo é uma página HTML com um formulário que permite inserir emails e percentuais.

## Pré-requisitos

Antes de executar os códigos, certifique-se de ter o seguinte instalado:

1. **Python**: Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em python.org.

2. **Banco de Dados Microsoft Access**: Você deve ter um arquivo `.accdb` (ou `.mdb`) com a estrutura de tabela correta para armazenar os dados. Certifique-se de que o caminho para o arquivo esteja correto no código `app.py`.

## Configuração

1. Clone este repositório para o seu computador:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu-repositorio
    ```

3. Instale as dependências Python (Flask e pyodbc):

    ```bash
    pip install flask pyodbc
    ```

4. Abra o arquivo `app.py` e configure o caminho para o seu arquivo de banco de dados:

    ```python
    DATABASE_FILE = 'C:\Programação\Desafio ATF Bank\Desafio 2\Database.accdb'
    ```

## Executando o Servidor Flask

1. Execute o servidor Flask:

    ```bash
    python app.py
    ```

2. O servidor estará disponível em http://127.0.0.1:5000/.

## Testando o Formulário HTML

1. Abra o arquivo `index.html` em um navegador.

2. Preencha os campos de email e percentual e clique no botão "Salvar".

3. Os dados serão enviados para o servidor Flask e inseridos no banco de dados.

## Considerações Finais

Certifique-se de ajustar os caminhos e configurações conforme necessário para o seu ambiente. 

Se precisar de mais ajuda ou tiver outras dúvidas, estou à disposição no nosso proximo encontro! 
