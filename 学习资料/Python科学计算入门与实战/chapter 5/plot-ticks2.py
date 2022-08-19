import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.xlim([-10,10])
plt.ylim([-10,10])
ax = plt.gca()
ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
ax.xaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))
plt.show()
