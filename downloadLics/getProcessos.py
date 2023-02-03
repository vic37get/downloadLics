from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

def getUags(filename):
    uags = pd.read_csv(filename, encoding='utf-8')
    listaUags = []
    for item in uags.values:
        listaUags.append(item[0])
    return listaUags

def getProcessos(URL, codUag):
    options = Options()
    #options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    campoUasg = driver.find_element('name', 'co_uasg')
    campoUasg.send_keys(codUag)
    botaoConfirmar = driver.find_element('name', 'ok')
    botaoConfirmar.click()
    driver.implicitly_wait(20) 
    conteudoHtml = driver.page_source
    return conteudoHtml

def main():
    URL = "http://comprasnet.gov.br/livre/Pregao/ata0.asp"
    todosUags = getUags('Uags.csv')
    for codUag in todosUags:
        print(getProcessos(URL, str(codUag)))

main()
    