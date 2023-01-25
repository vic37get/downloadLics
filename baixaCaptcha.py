import urllib.request
URL = "http://www.comprasnet.gov.br/scripts/srf/intercepta/captcha.aspx?opt=image"

def downloadImgCaptcha(URL, quantidade):
    for i in range(quantidade):
        try:
            urllib.request.urlretrieve(URL, "captchasBaixados/foto_"+str(i)+".png")
            print("Imagem {} salva!".format("foto_"+str(i)+".png"))
        except:
            print("Ocorreu um erro:")
    return


quantidade = 5
downloadImgCaptcha(URL, quantidade)