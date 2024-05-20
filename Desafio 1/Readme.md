# Executando o Formulário com Repeater

Este repositório contém um formulário HTML chamado `index.html` que utiliza um "repeater" para adicionar dinamicamente campos de participantes. O formulário permite que os usuários insiram seus emails e percentuais de participação.

## Pré-requisitos

Antes de executar o código, certifique-se de ter o seguinte instalado:

1. **Navegador Web**: Você precisará de um navegador web (como Google Chrome, Mozilla Firefox, etc.) para testar o formulário.

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

## Testando o Formulário HTML

1. Abra o arquivo `index.html` em um navegador.

2. Preencha os campos:
    - **Email**: Insira um endereço de email válido.
    - **Percentual**: Insira um valor numérico representando o percentual de participação.

3. Clique no botão "+ Adicionar Participante" para criar um novo campo de participante (repetir o campo).

4. Preencha os campos adicionais conforme necessário.

5. Clique no botão "Salvar" para enviar o formulário.

6. Os dados serão validados.

## Validações

O formulário inclui as seguintes validações:

- **Formato de Email**: O campo de email é validado usando uma expressão regular para garantir que seja um endereço de email válido.
- **Soma dos Percentuais**: A soma dos percentuais inseridos deve ser igual a 100%. Caso contrário, um aviso será exibido.

