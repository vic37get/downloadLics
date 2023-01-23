import urllib.request

def downloadImgCaptcha(URL, quantidade):
    for i in range(quantidade):
        try:
            urllib.request.urlretrieve(URL, "captchas/foto_"+str(i)+".png")
            print("Imagem {} salva!".format("foto_"+str(i)+".png"))
        except:
            print("Ocorreu um erro:")
    return


URL = "http://www.comprasnet.gov.br/scripts/srf/intercepta/captcha.aspx?opt=image"
quantidade = 20
downloadImgCaptcha(URL, quantidade)