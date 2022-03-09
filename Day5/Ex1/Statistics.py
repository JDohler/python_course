# A) Create a discrete random variable with poissonian distribution and plot its probability mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable

from scipy import stats
import numpy as np


# Create new pot
fig, ax = plt.subplots(1, 1)

# Set some value for mu
mu = 4

x = np.arange(stats.poisson.ppf(0.001, mu),
               stats.poisson.ppf(0.999, mu))

# Generate random variable
rv = stats.poisson(mu=mu)

# Plot PMF
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
         label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()