import requests
from bs4 import BeautifulSoup
import re


URL_UAGS = 'http://comprasnet.gov.br/livre/uasg/Catalogo_Resp.asp'

def pegaPagina(URL):
    pagina = requests.get(URL)
    return pagina

def pegaConteudoHtml(paginaHtml, nomeTag):
    codigos = []
    counteudoHtml = BeautifulSoup(paginaHtml.text, 'html.parser')
    form = counteudoHtml.find(id=nomeTag)
    table = form.find('table')
    tr = table.findAll('tr')
    for i in tr:
        item = i.find('td')
        codigos.append(item)
    return codigos

def removeTagHtml(conteudo):
    tagHtml = re.compile("<[^>]*>")
    conteudoLimpo = re.sub(tagHtml, '', str(conteudo))
    #print(conteudoLimpo[1])
    return conteudoLimpo

def escreveCsv(dados):
    with open('Uags.csv', 'w') as f:
        f.write(dados)

pagina = pegaPagina(URL_UAGS)
conteudoHtml = pegaConteudoHtml(pagina, 'form1')
dados = removeTagHtml(conteudoHtml)
escreveCsv(dados)