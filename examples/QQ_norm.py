# import andmath as am
from andmath.QQ import *

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import time

mu = 0
sigma = 1

n = 10000
x = np.random.normal(mu, sigma, n)

def cdf(v):
    return norm.cdf(v, mu, sigma)

theoretical_quantile, observed_quantile = QQ(x, cdf)

fig, ax = plt.subplots(1, 1)
ax.scatter(theoretical_quantile, observed_quantile)
ax.plot((0, 1), (0, 1), 'b--')
ax.set_xlabel('Theoretical quantile')
ax.set_ylabel('Observed quantile')
ax.set_title('QQ plot')
plt.tight_layout()
plt.show()
