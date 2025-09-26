# 🛠️ Automação de Extração e Atualização de Relatório de Incidentes
Este script automatiza o processo de extração, tratamento e atualização de dados de incidentes operacionais da plataforma Unilever. Utiliza Selenium para interagir com a interface web e Pandas para manipulação de dados em Excel.

# 🚀 Funcionalidades
Acessa automaticamente o portal de incidentes da Unilever.

Seleciona filtros de data com base no dia da semana (segunda-feira = últimos dois dias, demais dias = ontem).

Exporta os dados consolidados de incidentes.

Aguarda o download do arquivo e trata os dados:

Filtra apenas casos da sub-região "Latin America" e tipo "Issue".

Renomeia e remove colunas irrelevantes.

Adiciona colunas auxiliares para padronização.

Atualiza a base de dados principal (Incidents 2024.xlsx) com os novos registros.

Exclui o arquivo temporário após o processamento.

Exibe o tempo total de execução.

# 📦 Requisitos
Python 3.8+

Microsoft Edge instalado

WebDriver do Edge compatível com sua versão

Bibliotecas:

selenium

pandas

openpyxl (para salvar arquivos Excel)

Permissões de acesso ao portal da Unilever

# 📁 Estrutura de arquivos
Arquivo baixado: \consolidated incident data.xlsx

Base de dados atualizada: \Incidents 2024.xlsx

# ⏱️ Tempo de execução
O script mede o tempo total de execução e imprime no final, facilitando o monitoramento de performance.