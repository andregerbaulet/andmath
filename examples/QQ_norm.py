# import andmath as am
from andmath.QQ import *

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import time

# HOW MANY POINTS SHOULD BE GENERATED
n = 1000

# GENERATE DATA FROM DIFFERENT DISTRIBUTIONS
selector = 3
if selector == 1:
    mu = 0
    sigma = 1
    x = np.random.normal(mu, sigma, n)
elif selector == 2:
    df = 10
    x = np.random.standard_t(df, n)
elif selector == 3:
    a = 1
    b = 2
    x = np.random.beta(a, b, n)

# SELECT SCIPY DISTRIBUTION TO USE FOR THEORETICAL QUANTILES
scipy_distribution = stats.norm

fig, ax = plt.subplots(1, 1)
# GENERATE QQ-VALUES AND PLOT ON ax
theoretical_quantile, observed_quantile = QQ(x, scipy_distribution, ax=ax)
plt.tight_layout()
plt.show()
