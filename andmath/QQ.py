import numpy as np
import numpy.typing as npt

from scipy.stats import rv_continuous
from matplotlib.pyplot import axis

def QQ( x: npt.ArrayLike,
        scipy_distribution: rv_continuous,
        parameters: tuple[float]=None,
        ax: axis=None) -> (np.ndarray, np.ndarray):
        
    '''Takes an array x as input and will return observed and theoretical
    quantiles given a scipy distribution. If no parameters are given
    scipy.stats.rv_continuous.fit will be used to estimate parameters.
    If pyplot axis is given the quantiles will be plotted.'''

    if parameters is None:
        parameters = scipy_distribution.fit(x)
    a = np.sort(np.reshape(np.array(x), -1))
    n = a.shape[0]
    theoretical_quantile = np.zeros(n)
    observed_quantile = np.zeros(n)
    for i, v in enumerate(a):
        theoretical_quantile[i] = scipy_distribution.cdf(v, *parameters)
        observed_quantile[i] = (i + 1) / n
    if ax is not None:
        ax.scatter(theoretical_quantile, observed_quantile)
        ax.plot((0, 1), (0, 1), 'b--')
        ax.set_xlabel('Theoretical quantile')
        ax.set_ylabel('Observed quantile')
        ax.set_title('QQ plot')
    return theoretical_quantile, observed_quantile
