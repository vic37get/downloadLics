from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re
from tqdm import tqdm

class Registro:
    def __init__(self, noLicitacao, codUasg, nomeUasg, data):
        self.noLicitacao = noLicitacao
        self.codUasg = codUasg
        self.nomeUasg = nomeUasg
        self.data = data
        
def getUags(filename):
    uags = pd.read_csv(filename, encoding='utf-8')
    listaUags = []
    for item in uags.values:
        listaUags.append(item[0])
    return listaUags

def removeTagHtml(listaConteudo):
    tagHtml = re.compile("<[^>]*>")
    for item in range(len(listaConteudo)):
        listaConteudo[item] = re.sub(tagHtml, '', str(listaConteudo[item]))
        listaConteudo[item] = listaConteudo[item].strip().replace('\n (Pregão)', '')
    return listaConteudo

def getProcessos(URL, codUag):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
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
        itensLicitacao = tr.find_all("td")
        itensLicitacao = removeTagHtml(itensLicitacao)
        codigosLicitacao.append(Registro(itensLicitacao[0], itensLicitacao[1], itensLicitacao[2], itensLicitacao[3]))
    return codigosLicitacao

def main():
    URL = "http://comprasnet.gov.br/livre/Pregao/ata0.asp"
    todosUags = getUags('Uags.csv')
    
    df = pd.DataFrame(columns=['noLicitacao', 'codUasg', 'nomeUasg', 'data'])
    uagsErros = []
    barraProgresso = tqdm(total=len(todosUags))
    for codUag in todosUags:
        codigosLicitacao = pegaConteudoHtml(getProcessos(URL, str(codUag)))
        for licitacao in codigosLicitacao:
            try:
                df = df.append({'noLicitacao': licitacao.noLicitacao, 'codUasg': licitacao.codUasg, 'nomeUasg': licitacao.nomeUasg, 'data': licitacao.data}, ignore_index=True)
            except:
                uagsErros.append([codUag, licitacao.noLicitacao])
        barraProgresso.update()
    with open('uagsComErro.txt', 'w') as f:
        for erro in uagsErros:
            f.write(erro)
    f.close()
    df.to_csv('processosComprasNet.csv', index=False, encoding='utf-8')
main()
    