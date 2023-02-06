from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re

def getUags(filename):
    uags = pd.read_csv(filename, encoding='utf-8')
    listaUags = []
    for item in uags.values:
        listaUags.append(item[0])
    return listaUags

def removeTagHtml(conteudo):
    tagHtml = re.compile("<[^>]*>")
    conteudoLimpo = re.sub(tagHtml, '', str(conteudo))
    return conteudoLimpo

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

def pegaConteudoHtml(paginaHtml):
    codigosLicitacao = []
    counteudoHtml = BeautifulSoup(paginaHtml, 'html.parser')
    allTr = counteudoHtml.find_all("tr", {"class": "tex3"})
    for ind, tr in enumerate(allTr):
        noLicitacao = tr.find_all("a")
        noLicitacao = removeTagHtml(noLicitacao[0]).strip()
        codigosLicitacao.append(noLicitacao)
    return codigosLicitacao, 

def main():
    URL = "http://comprasnet.gov.br/livre/Pregao/ata0.asp"
    todosUags = getUags('Uags.csv')
    df = pd.DataFrame(columns=['UAG', 'codLicitacao'])
    for codUag in todosUags:
        codigosLicitacao = pegaConteudoHtml(getProcessos(URL, str(codUag)))
        uags = [codUag]*len(codigosLicitacao)
        df = df.append({"UAG": uags, "codLicitacao": codigosLicitacao}, ignore_index=True)
        break
    print(df)
main()
    