import convis
import numpy as np
import matplotlib.pylab as plt
plt.figure()
plt.plot(convis.numerical_filters.exponential_filter_1d(tau=0.01))
plt.show()