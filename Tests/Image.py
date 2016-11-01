# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:37:29 2016

@author: codeWorm
"""
from scipy.misc import imread, imsave, imresize

img = imread ('cat.jpg')
img_tinted = img * [0.1,0.1,0.5]
imsave('cat_tinted.jpg', img_tinted)