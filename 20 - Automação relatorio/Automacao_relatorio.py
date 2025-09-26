from selenium import webdriver #para definir um navegador
from selenium.webdriver.support.ui import WebDriverWait #para aguardar um tempo antes de realizar uma ação
from selenium.webdriver.support import expected_conditions as EC #para determinar uma condição antes de clicar em um elemento
from selenium.webdriver.common.by import By #para selecionar elementos especificos
from datetime import datetime, timedelta #para tratar e manipular datas
import time
import os

hoje = (datetime.today()).date()

i = time.time()
print("Abrindo navegador...")
navegador = webdriver.Edge()
navegador.maximize_window()
navegador.get('https://<extrairdados>.com/ops-reporting/issue-reporting/issue')

esperando = WebDriverWait(navegador, 20)

botao_it = esperando.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hscroll_31"]/div[2]/div/div[5]/button'))).click()
botao_consolidated = esperando.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div/div/app-issue-root/app-ops-page-root/div/div[2]/ejs-tab/div[1]/div/div[4]/div/div/div'))).click()
botao_dateopened = esperando.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div/div/app-issue-root/app-ops-page-root/div/app-filter-panel/div/div/form/div[2]/div[2]/app-select-date-range/div/div[1]/div[1]/div/ejs-toolbar/div/div[3]/div[1]/div/label'))).click()

#Checa se hoje é segunda-feira
if hoje.weekday() == 0:
    botao_month = esperando.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div/div/app-issue-root/app-ops-page-root/div/app-filter-panel/div/div/form/div[2]/div[2]/app-select-date-range/div/div[1]/div[1]/button[4]'))).click()
else:
    botao_yesterday = esperando.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div/div/app-issue-root/app-ops-page-root/div/app-filter-panel/div/div/form/div[2]/div[2]/app-select-date-range/div/div[1]/div[1]/button[2]'))).click()

#exporta dados
print("Exportando dados...")
try:
    time.sleep(2)
    botao_export = esperando.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-page-header/div/div[1]/div[1]/div/div[2]/div/ejs-tooltip/button"))).click()
except:
    time.sleep(2)
    botao_export = navegador.find_element(By.XPATH, "/html/body/app-root/div/app-page-header/div/div[1]/div[1]/div/div[2]/div/ejs-tooltip/button")
    navegador.execute_script("arguments[0].scrollIntoView({block : 'center'})", botao_export)
    botao_export.click()

esperando = WebDriverWait(navegador, 300)
botao_download = esperando.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Download']"))).click()

caminho_tabela_ext = r"caminho\do\arquivo\consolidated incident data.xlsx" #r'<string>' -> rawstrigs que ignora comandos especificos que podem estar dentro da string
t_limite = 30
t_inicio = time.time()
while not os.path.exists(caminho_tabela_ext):
    if time.time() - t_inicio > 30:
        raise TimeoutError('Arquivo não encontrado dentro de 30 segundos')

#tratando e filtrando dados
print("Tratando e Filtrando dados...")
import pandas as pd
tabela_extraida = pd.read_excel(caminho_tabela_ext, skiprows=9) #skiprows ignora 9 primeiras linhas
tabela_extraida = tabela_extraida[
    (tabela_extraida['SubRegion'] == 'Latin America') &
    (tabela_extraida['Case Type'] == 'Issue')
]

tabela_extraida.rename(columns={'Total Pending Minutes' : 'Pending Minutes', "SubCategory/Opening code" : 'SubCategory'}, inplace=True)
tabela_extraida.drop(columns=['User Pending Minutes','Business Elapse Time', 'Elapsed Time (hh:mm:ss)', 'Resolution Code', 'Customer Business Group', 'Is Escalated'], inplace=True)
tabela_extraida['Service Line'] = '-'
tabela_extraida['Platform/Sub-Service Line'] = tabela_extraida['Service Line']

if hoje.weekday() == 0:
    dois_dias_atras = (hoje - timedelta(days=2))
    tabela_extraida['Opened'] = pd.to_datetime(tabela_extraida['Opened'])
    tabela_extraida = tabela_extraida[
        (tabela_extraida['Opened'].dt.date >= dois_dias_atras) &
        (tabela_extraida['Opened'].dt.date < hoje)
    ]

caminho_tabela_report = r"caminho\do\arquivo\Incidents 2024.xlsx"

#adicionando dados extraidos na base de dados
tabela_report = pd.read_excel(caminho_tabela_report)
tabela_extraida = tabela_extraida[tabela_report.columns] #.columns filtra as colunas que só tem em tabela_report
print("Adicionando dados...")
tabela_report = pd.concat([tabela_report, tabela_extraida], ignore_index=True)
tabela_report.to_excel(caminho_tabela_report, index=False, sheet_name='All')
print("Tabela atualizada! Concluido.")
os.remove(caminho_tabela_ext) #excluindo tabela extraida

f = time.time()
tempot = f - i
print(tempot, 'segundos')