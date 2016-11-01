# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:43:28 2016

@author: codeWorm
"""

import numpy as np 
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)
y_sin = np.sin(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()