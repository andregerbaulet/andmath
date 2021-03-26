#import andmath as am
from andmath.GaussianProcessRegression import *
import numpy as np
import matplotlib.pyplot as plt
import time

n = 100
m = 100
mu = 0
sigma = np.sqrt(.1)

# SELECT X INTERVAL FOR OBSERVED AND PREDICTED POINTS
interval_observed = (0, 9)
interval_prediction = (0, 12)

# GENERATE OBSERVED POINTS
#x_observed = np.random.uniform(interval_observed[0], interval_observed[1], n)
x_observed = np.linspace(interval_observed[0], interval_observed[1], n)
f = np.tanh(2 * np.pi * x_observed / 12) - 0.1 * (x_observed- (interval_observed[1] - interval_observed[0]) / 2)
y_observed = f + np.random.normal(mu, sigma, n)

# GENERATE X-VALUES WHERE TO PREDICT
x_prediction = np.linspace(interval_prediction[0], interval_prediction[1], m)

# PLOT RESUTLS FOR DIFFERENT TUNING PARAMETERS
fig = plt.figure()
for i in range(4):
    t = 10 ** (i-2)
        # BELOW HERE IS ONLY FOR PLOTTING
    gpr = GaussianProcessRegression(x_observed , y_observed, x_prediction, tuner=t, sigma=np.sqrt(0.1))

    y_prediction = gpr.get_regression()
    ci_upper = gpr.get_upper_ci()
    ci_lower = gpr.get_lower_ci()

    # BELOW HERE IS ONLY FOR PLOTTING

    # VALUES MUST BE SORTED BEFORE PLOTTED
    ind = np.argsort(x_prediction)
    x_prediction = x_prediction[ind]
    y_prediction = y_prediction[ind]
    ci_upper = ci_upper[ind]
    ci_lower = ci_lower[ind]

    # BELOW HERE IS ONLY FOR PLOTTING
    plt.subplot(2, 2, i+1)
    plt.tight_layout()
    plt.plot(x_observed, f, 'b-', label='Actual')
    plt.plot(x_observed, y_observed, 'go', label='Observed')
    plt.plot(x_prediction, y_prediction, 'r-', label='Predicted')
    plt.fill_between(x_prediction.flatten(), ci_upper.flatten(), ci_lower.flatten(), facecolor='orange', color='blue', alpha=0.2, label='Confidence interval')
    plt.legend(loc='upper right')
    plt.title('Tuning parameter ' + str(round(t, 4)))
    plt.xlim(np.min((interval_observed[0], interval_prediction[0])), np.max((interval_observed[1], interval_prediction[1])))
    #plt.ylim(-2, 2)
    #plt.axis((np.min(interval_observed[0], interval_prediction[0]), np.max(interval_observed[1], interval_prediction[1]), -2, 2))
plt.show()
