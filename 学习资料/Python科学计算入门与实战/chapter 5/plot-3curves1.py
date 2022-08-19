import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3,3,20)
y = 10*x                       #y=10x
x1 = np.linspace(-2,2,20)
y1 = 8*x1**2                  #y=8x2
x2 = np.linspace(-3,3,20)
y2 = x2**3                    #y=x3
plt.plot(x,y,linestyle = "solid",linewidth = 1.5,color = "red",marker="*")
plt.plot(x1,y1,linestyle = "dashed",linewidth = 0.9,color = "green")
plt.plot(x2,y2,linestyle = "dotted",linewidth = 2.0,color = "black")
plt.show()
