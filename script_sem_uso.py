import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option("detach", True)
#options.headless = True
driver = webdriver.Chrome(options=options)
from time import sleep
#driver.maximize_window()



login_url = 'https://app-auth.pipefy.com/login'
username = 'operacional@bluechipriscos.com.br'
password = 'bluechip25'

wait = WebDriverWait(driver, 60)
driver.get(login_url)

campo_login = wait.until(EC.element_to_be_clickable(
    (By. XPATH, '//*[@id="root"]/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/input'))).send_keys(username)
campo_senha = wait.until(EC.element_to_be_clickable(
    (By. XPATH, '//*[@id="root"]/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div[1]/div/input'))).send_keys(password)
botao_entrar = wait.until(EC.element_to_be_clickable(
    (By. XPATH, '//*[@id="root"]/div/div/form/div/div/div/button/span'))).click()
sleep(5)

report_url = 'https://app.pipefy.com/pipes/303149085/reports_v2/300491935'
driver.get(report_url)


botao_exportar = wait.until(EC.element_to_be_clickable(
    (By. XPATH, '//*[@id="pipe_placeholder"]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div/div/button'))).click()
botao_download =  wait.until(EC.element_to_be_clickable(
    (By. XPATH, '/html[1]/body[1]/div[12]/div[1]/div[2]/footer[1]/button[2]'))).click()
sleep(5)

def encontrar_arquivo_mais_recente(pasta):
    arquivos = os.listdir(pasta)
    arquivos = [os.path.join(pasta, arquivo) for arquivo in arquivos]
    arquivos = [arquivo for arquivo in arquivos if os.path.isfile(arquivo)]
    
    if not arquivos:
        return None
    
    arquivo_mais_recente = max(arquivos, key=os.path.getmtime)
    return arquivo_mais_recente


pasta = 'C://Users/Giovana/Downloads'
arquivo_mais_recente = encontrar_arquivo_mais_recente(pasta)

if arquivo_mais_recente:
    print("O arquivo mais recente é:", arquivo_mais_recente)
else:
    print("A pasta está vazia.")

import shutil

def copiar_arquivo(destino, arquivo_origem):
    shutil.copy2(arquivo_origem, destino)

pasta_destino = 'C://Users/Giovana/Downloads/relatorioMovimentacoes'  
arquivo_origem = arquivo_mais_recente 


if os.path.isfile(arquivo_origem):
    copiar_arquivo(pasta_destino, arquivo_origem)
    print("Arquivo copiado com sucesso.")
else:
    print("O arquivo de origem não existe.")

driver.quit()

'''def copiar_arquivo(destino, arquivo_origem):
    shutil.copy2(arquivo_origem, destino)

pasta_destino = 'C://Users/Giovana/Downloads/relatorioMovimentacoes'
arquivo_origem = arquivo_mais_recente

os.rename(arquivo_mais_recente, 'movimentacoes.xlsx')

if os.path.isfile():
    copiar_arquivo(pasta_destino, 'movimentacoes.xlsx')
    print("Arquivo copiado com sucesso.")
else:
    print("O arquivo de origem não existe.")

driver.quit()'''