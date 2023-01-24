URL = "http://www.comprasnet.gov.br/ConsultaLicitacoes/Download/Download.asp?coduasg=153036&numprp=302018&modprp=5&bidbird=N"

from selenium import webdriver

# especificando o caminho para o arquivo msedgedriver.exe
path = 'msedgedriver.exe'
edge = "'/mnt/c/Program Files (x86)/Microsoft/Edge/msedge.exe'"

# iniciando o Edge
driver = webdriver.Edge(executable_path=path)

# usando o driver para abrir uma página web
driver.get("https://www.google.com")
