#EXERCISE 5 IMAGES

from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

# read image RGB image and convert to grayscale
im = rgb2gray(imread('input.jpg'))
imF = dct2(im)
im1 = idct2(imF)

plt.gray()
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original image', size=10)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=10)
plt.show()