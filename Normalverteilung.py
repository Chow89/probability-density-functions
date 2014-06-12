__author__ = 'Christian'

import matplotlib.pyplot as plt
import numpy as np
import math


def normal(m, s):
    return (1 / (math.sqrt(2 * np.pi * s ** 2))) * np.exp(-(x - m) ** 2 / (2 * s ** 2))


x = np.linspace(-7, 7, 280)
y = normal(0, 1)
y2 = normal(0, 0.5)
y3 = normal(0, 1.5)
y4 = normal(0, 2)

plt.title("Normalverteilung")
plt.xlim(-7, 7)
plt.ylim(-0.05, max(y.max(), y2.max(), y3.max(), y4.max())*1.1)
plt.plot(x, y4, label=r'$\sigma$'+" = 2")
plt.plot(x, y3, label=r'$\sigma$'+" = 1.5")
plt.plot(x, y, label=r'$\sigma$'+" = 1")
plt.plot(x, y2, label=r'$\sigma$'+" = 0.5")
plt.grid(True)
plt.legend(loc='upper left')
plt.show()