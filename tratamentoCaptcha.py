from pathlib import Path
import cv2
import matplotlib

'''for i in Path('captchasBaixados/').glob('*.png'):
    print(i)
    image = plt.imread(i.absolute().__str__(),0)
    #print(image)
    #plt.imshow(image)
    ret,thresh1 = cv2.threshold(image,50,255,cv2.THRESH_BINARY)
    plt.imshow(thresh1)
    plt.imsave(i.parent.joinpath(i.stem+'_threshold'+'.png').__str__(),thresh1)
    #show()
    #break'''