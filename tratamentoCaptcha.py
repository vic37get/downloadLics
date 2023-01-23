from pathlib import Path
import cv2
import matplotlib.pyplot as plt

for i in Path('captchasBaixados/').glob('*.png'):
    print(i)
    image = plt.imread(i.absolute().__str__(),0)
    ret,thresh1 = cv2.threshold(image,5,255,cv2.THRESH_BINARY)
    plt.imshow(thresh1)
    plt.imsave('captchasTratados/{}_threshold.png'.format(i.stem),thresh1)