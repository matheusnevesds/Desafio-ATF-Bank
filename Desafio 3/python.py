import requests
from openpyxl import Workbook
import os

# Faz a requisição à API do GitHub
url = "https://api.github.com/repositories"
response = requests.get(url)
data = response.json()

# Cria um novo arquivo Excel
workbook = Workbook()
sheet = workbook.active
sheet.title = "Repositórios"

# Adiciona cabeçalhos às colunas
sheet.append(["Contém JSON na descrição", "Repositórios"])

# Contadores para repositórios com e sem a palavra "JSON" na descrição
com_json = 0
sem_json = 0

# Preenche o arquivo Excel com os dados dos repositórios
for repo in data:
    name = repo["name"]
    description = repo["description"]

    # Verifica se a descrição não é nula
    if description:
        # Verifica se a descrição contém a palavra "JSON"
        if "json" in description.lower():
            com_json += 1
        else:
            sem_json += 1

# Adiciona as informações à tabela
sheet.append(["Sim", com_json])
sheet.append(["Não", sem_json])

# Obtém o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Salva o arquivo Excel na mesma pasta do script
caminho_arquivo = os.path.join(diretorio_atual, "repositorios_github.xlsx")
workbook.save(caminho_arquivo)

# Printa no console o resultado final
print(f"Total de repositórios com 'JSON' na descrição: {com_json}")
print(f"Total de repositórios sem 'JSON' na descrição: {sem_json}")

