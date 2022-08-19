import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3,3,20)
y = 10*x 
x1 = np.linspace(-2,2,20)
y1 = 8*x1**2
x2 = np.linspace(-3,3,20)
y2 = x2**3
##plt.plot(x,y,x1,y1,x2,y2)
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
