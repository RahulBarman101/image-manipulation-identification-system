# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:13:02 2019

@author: Sayali Badade
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:13:42 2019

@author: Sayali Badade
"""
"""
#RESIZE IMAGE
import matplotlib.pyplot as plt
from PIL import Image
image=Image.open('C:\\Users\\Rahul Barman\\Desktop\\miniproject\\dataset\\original\\1a0zj6.jpg')
print(image.size)
resize_img=image.resize((416,416))
print(resize_img.size)
plt.imshow(resize_img)
plt.show()
"""

#FLIP IMAGE
"""
from PIL import Image
from matplotlib import pyplot
%matplotlib inline
image=Image.open('C:\\Users\\Rahul Barman\\Desktop\\miniproject\\dataset\\original\\1a0zj6.jpg')
hoz_flip=image.transpose(Image.FLIP_LEFT_RIGHT)
ver_flip=image.transpose(Image.FLIP_TOP_BOTTOM)

pyplot.imshow(image)
pyplot.subplot(311)
pyplot.imshow(hoz_flip)
hoz_flip.show()
pyplot.subplot(313)
pyplot.imshow(ver_flip)
ver_flip.show()
"""
'''
from PIL import Image
import os
from tqdm import tqdm

path = 'C:\\Users\\Rahul Barman\\Desktop\\miniproject\\dataset\\original'
savedir = 'C:\\Users\\Rahul Barman\\Desktop\\miniproject\\dataset\\orig'
i = 0
x = os.listdir(path)
for img in tqdm(x[1:5000]):
    try:
        image = Image.open(os.path.join(path,img))
        new_img = image.transpose(Image.FLIP_TOP_BOTTOM)
        new_img.save(os.path.join(savedir,f'{i}_{img}'))
        i+=1
    except:
        continue
'''

"""
#ROTATE IMAGE
from PIL import Image
from matplotlib import pyplot as plt
image = Image.open('C:\\Users\\Rahul Barman\\Desktop\\miniproject\\dataset\\original\\1a0zj6.jpg')
plt.subplot(311)
plt.imshow(image)
plt.subplot(312)
plt.imshow(image.rotate(45))
image.rotate(45)
plt.subplot(313)
plt.imshow(image.rotate(90))
image.rotate(90)
plt.show()
"""
#CROP IMAGE
"""from PIL import Image
image=Image.open('E:\\dataset\\original\\1a0zj6.jpg')
cropped=image.crop((200,200,300,300))
cropped.show()"""

import os
import random
import matplotlib.pyplot as plt
from PIL import Image
#%matplotlib inline
path = 'C:/Users/Rahul Barman/Desktop/miniproject/dataset/original'
x = os.listdir(path)
y = random.choice(x)
img = Image.open(os.path.join(path,y))
plt.imshow(img.rotate(90))
plt.imshow(img)

import os
from PIL import Image

path = 'C:/Users/Rahul Barman/Desktop/miniproject/dataset/original'
savedir = 'C:/Users/Rahul Barman/Desktop/miniproject/dataset/ori'
i = 0
x = os.listdir(path)

for img in x[1:]:
   try:
       imgage = Image.open(os.path.join(path,img))
       new_img = image.rotate(90)
       new_img.save(os.path.join(savedir,img))
   except:
       continue
