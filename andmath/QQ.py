import numpy as np

def QQ(x, cdf):
    a = np.sort(np.reshape(np.array(x), -1))
    n = a.shape[0]
    theoretical_quantile = np.zeros(n)
    observed_quantile = np.zeros(n)
    for i, v in enumerate(a):
        theoretical_quantile[i] = cdf(v)
        observed_quantile[i] = (i + 1) / n
    return theoretical_quantile, observed_quantile
