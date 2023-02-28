# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

#源代码此处给的是相对路径，但是运行时读取不到，因此换成了绝对路径
img = imread('D:\Python\Projects\Deep-Learning-WrittingRecognition\dataset\lena.png') #读入图像
plt.imshow(img)

plt.show()