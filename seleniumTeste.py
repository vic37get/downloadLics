URL = "http://www.comprasnet.gov.br/ConsultaLicitacoes/Download/Download.asp?coduasg=153036&numprp=302018&modprp=5&bidbird=N"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# especificando o caminho para o arquivo msedgedriver.exe
path = 'msedgedriver.exe'
edge = "'/mnt/c/Program Files (x86)/Microsoft/Edge/msedge.exe'"

# iniciando o Edge
driver = webdriver.Edge(executable_path=path)

# usando o driver para abrir uma página web
driver.get(URL)

field = driver.find_element(By.ID,'idLetra')

field.send_keys('Teste')


captcha = driver.find_element(By.XPATH,"//img[@src='/scripts/srf/intercepta/captcha.aspx?opt=image']")

image = captcha.screenshot_as_png

# salvando a imagem em um arquivo
with open("example-image.png", "wb") as file:
    file.write(image)
time.sleep(10)

driver.quit()


