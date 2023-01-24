#%%
from pathlib import Path
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
#%%
for i in Path('captchasBaixados/').glob('*.png'):
    image = mpimg.imread(i.absolute().__str__(),'gray')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
    mpimg.imsave('captchasTratados/{}_threshold.png'.format(i.stem),thresh1,cmap='gray')
# %%
