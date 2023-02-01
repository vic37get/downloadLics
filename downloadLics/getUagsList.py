import requests
from bs4 import BeautifulSoup
import re


URL_UAGS = 'http://comprasnet.gov.br/livre/uasg/Catalogo_Resp.asp'

def pegaPagina(URL):
    pagina = requests.get(URL)
    return pagina

def pegaConteudoHtml(paginaHtml):
    counteudoHtml = BeautifulSoup(paginaHtml.text, 'html.parser')
    tabela = counteudoHtml.find(id='form1')
    conteudos = tabela.findAll('tr')
    print(conteudos)

def removeTagHtml(conteudo):
    tagHtml = ("<[^>]*>", "")
    conteudoLimpo = re.sub(tagHtml, '', conteudo)
    return conteudoLimpo


pagina = pegaPagina(URL_UAGS)
pegaConteudoHtml(pagina)



