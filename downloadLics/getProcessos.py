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
    uagsErros = []
    for codUag in todosUags:
        print('UAG ATUAL: ', codUag)
        codigosLicitacao = pegaConteudoHtml(getProcessos(URL, str(codUag)))[0]
        for licitacao in codigosLicitacao:
            print('UAG: ', codUag,'LICITACAO: ', licitacao)
            try:
                df = df.append({"UAG": codUag, "codLicitacao": licitacao}, ignore_index=True)
            except:
                uagsErros.append([codUag, licitacao])
                print('ERRO!')
    with open('uagsComErro.txt', 'w') as f:
        for erro in uagsErros:
            f.write(erro)
    f.close()
    df.to_csv('processosComprasNet.csv', index=False, encoding='utf-8')
main()
    