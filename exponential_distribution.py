__author__ = 'Christian'

import matplotlib.pyplot as plt
import numpy as np


def exp(l):
    return l*np.exp(-l*x)

x = np.linspace(0, 5, 100)
y = exp(1)
y2 = exp(0.5)
y3 = exp(5)
y4 = exp(2)

plt.title("Exponentialverteilung")
plt.xlim(0, 5)
plt.ylim(-0.05, 1)
plt.plot(x, y3, label=r'$\lambda$'+" = 5")
plt.plot(x, y4, label=r'$\lambda$'+" = 2")
plt.plot(x, y, label=r'$\lambda$'+" = 1")
plt.plot(x, y2, label=r'$\lambda$'+" = 0.5")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()